#!/usr/bin/env python3
"""Deterministic reactive controller using only eight IR distances and food smell."""

import os, platform

if platform.system() in ("Linux", "Darwin"):
    os.environ["KIVY_VIDEO"] = "ffpyplayer"

from kivy.config import Config
from kivy.logger import Logger
from pysimbotlib.core import PySimbotApp, Robot

Config.set("kivy", "log_level", "info")

class RCRobot(Robot):
    # Hint safety baselines plus a tested corridor margin for wall/corner traps.
    SAFETY_DISTANCE, CLOSED_DISTANCE = 30, 5
    CORRIDOR_DISTANCE, STEP, AVOID_STEP = 14, 10, 6
    # Food steering strength, gentle side correction, and decisive escape turn.
    FOOD_GAIN, SIDE_TURN, BLOCKED_TURN = 0.28, 20, 60

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Small runtime memory: current stage, repeated IR patterns, and recovery progress.
        self._stage, self._tick = "", 0
        self._history, self._last_eat = [], 0
        self._stuck_ticks, self._escape_attempt = 0, 0

    def _log_stage(self, stage):
        # Log only a stage change (or every 20 ticks) so the console stays readable.
        if stage == self._stage and self._tick % 20: return
        self._stage = stage
        Logger.info("RCRobot: %s | tick=%d | pos=(%.0f, %.0f) | eat=%d" % (stage, self._tick, self.center_x, self.center_y, self.eat_count))

    @staticmethod
    def _turn_to_open(right, left, angle):
        # Choose the roomier side; equal readings always use the same tie-break rule.
        return -angle if right < left else angle

    def _blocked_escape(self, readings):
        # Use a three-ray gap to avoid aiming one clear ray straight into a corner.
        gaps = [min(readings[i - 1], readings[i], readings[(i + 1) % 8]) for i in range(8)]
        choices = sorted(range(8), key=lambda i: (gaps[i], readings[i]), reverse=True)
        sensor = choices[min(self._escape_attempt, 2)]
        self._log_stage("BLOCKED_ESCAPE")
        self.turn(sensor * 45)
        self.move(self.AVOID_STEP)

    def _loop_seen(self, readings):
        # The same quantized 8-IR signature three times signals a local navigation loop.
        pattern = tuple(min(20, int(value // 5)) for value in readings)
        self._history.append(pattern)
        if len(self._history) > 12: self._history.pop(0)
        return self._history.count(pattern) >= 3

    def update(self):
        self._tick += 1
        # IR0 is forward; IR1/IR2 and IR7/IR6 represent the two front-side areas.
        IR0, IR1, IR2, IR3, IR4, IR5, IR6, IR7 = self.distance()
        right = min(IR1, IR2)
        left = min(IR7, IR6)
        food_angle = self.smell()

        # Eating means a new food target, so old loop/recovery history is no longer useful.
        if self.eat_count != self._last_eat:
            self._last_eat = self.eat_count
            self._history.clear(); self._stuck_ticks = 0; self._log_stage("EAT")
        readings = (IR0, IR1, IR2, IR3, IR4, IR5, IR6, IR7)
        # Exact collision: select the widest sensor gap, then try the next gap if needed.
        if self.stuck:
            self._stuck_ticks = 3
            self._blocked_escape(readings)
            self._escape_attempt = min(self._escape_attempt + 1, 2)
            return
        # Continue a few short steps after recovery so the robot clears the obstacle boundary.
        if self._stuck_ticks:
            self._stuck_ticks -= 1
            self._log_stage("ESCAPE_FORWARD"); self.move(self.AVOID_STEP); return
        self._escape_attempt = 0
        # Repeated sensor pattern: leave the loop by turning toward the roomier side.
        if self._loop_seen(readings):
            self._history.clear()
            self._log_stage("LOOP_ESCAPE")
            self.turn(self._turn_to_open(right, left, self.BLOCKED_TURN))
            self.move(self.AVOID_STEP); return

        # Hint safety priority: narrow corridor, front obstacle, close side, cautious forward.
        if right < self.CORRIDOR_DISTANCE and left < self.CORRIDOR_DISTANCE:
            self._log_stage("NARROW_ESCAPE")
            self.turn(self._turn_to_open(right, left, self.BLOCKED_TURN))
            self.move(self.AVOID_STEP); return
        if IR0 < self.SAFETY_DISTANCE:
            self._log_stage("FRONT_HIT" if IR0 <= 0 else "FRONT_AVOID")
            self.turn(self._turn_to_open(right, left, self.BLOCKED_TURN))
            self.move(self.AVOID_STEP); return
        if right < self.CLOSED_DISTANCE or left < self.CLOSED_DISTANCE:
            self._log_stage("SIDE_AVOID")
            self.turn(self._turn_to_open(right, left, self.SIDE_TURN))
            self.move(self.AVOID_STEP); return
        if right < self.SAFETY_DISTANCE or left < self.SAFETY_DISTANCE:
            self._log_stage("FORWARD"); self.move(self.STEP); return

        # Open space: steer toward food proportionally; clamp avoids abrupt full turns.
        self._log_stage("SEEK")
        self.turn(max(-30, min(30, food_angle * self.FOOD_GAIN)))
        self.move(self.STEP)

if __name__ == "__main__":
    PySimbotApp(robot_cls=RCRobot, max_tick=3000, num_robots=1).run()