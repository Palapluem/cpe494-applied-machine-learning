# Assignment 6: Reinforcement Learning

This folder keeps the instructor's assignment brief and supplied starter
unchanged. The runnable controller, simulator changes, experiment records, and
graphs are maintained separately in the `assignment-6-rl` branch of the
[`cpe-aml` fork](https://github.com/Palapluem/cpe-aml/tree/assignment-6-rl/asm-6_PyRLSimbot).

## Course files

- `AML Assignment 06 RL 2026.pdf` — assignment brief.
- `Assignment 6 (to start with).py.txt` — original starter, kept unchanged.
- `../lecture/Lecture 6_Reinforcement Learning/` — lecture source material.
  The PDFs were used as the course reference.

## Selected controller

The final controller uses tabular Q-learning. Its Q-table has 192 states and
four actions, starts at zero, and is trained for 100,000 updates with seed 11.
The Q-learning update keeps the assignment's α = 0.5 and γ = 0.9.

| Setting | Value |
| --- | --- |
| Training exploration | ε = 0.10 for 20,000 updates, then ε = 0.05 |
| Distance-sensor threshold | 22 units |
| Food-bearing range | −10° to +10° |
| Actions | Forward, left, right, backward; backward is an implementation choice beyond the brief's three-action example |
| Main event rewards | Eat +15; blocked move −10 |
| Evaluation exploration | ε = 0.15, using non-greedy actions when available |
| Safety handling | Sensor-based margin 4.5 units; four recovery turns after a blocked move |

The directional reward terms from Example 6 are computed from the robot's
binned sensor readings. The policy is frozen during evaluation. The safety
filter uses the same existing distance sensors and does not read hidden food
coordinates.

## Results and graphs

The instructor's latest targets are Eat > 0.005 and Hit < 0.002, with rates
defined as event counts per 1,000 actions. A paired final evaluation used 60
held-out scenes for each start type and 5,000 actions per scene:

| Start | Eat / 1,000 actions (95% CI) | Hit / 1,000 actions (95% CI) |
| --- | ---: | ---: |
| Official | 8.743 (8.473–9.020) | 0.103 (0.063–0.153) |
| Random | 8.880 (8.587–9.170) | 0.103 (0.067–0.143) |

The final policy graph is a separate 100,000-tick trace: 842 foods and 10
blocked moves, or Eat 8.420 and Hit 0.100 per 1,000 ticks. Both graphs begin at
(0, 0), then show measured cumulative rates every 1,000 ticks; the rate axes
are raw counts divided by elapsed actions, shown to three decimals, with no
smoothing.

- [Final frozen-policy graph](../cpe-aml/asm-6_PyRLSimbot/assets/final_policy_eat_hit_rates.png)
- [Online training graph](../cpe-aml/asm-6_PyRLSimbot/assets/single_run_eat_hit_rates.png)
- [Full evaluation report](../cpe-aml/asm-6_PyRLSimbot/EXAMPLE6_OPTIMIZATION.md)
- [Protocol and earlier comparisons](../cpe-aml/asm-6_PyRLSimbot/RATE_TARGET_STUDY.md)

The single-run graph illustrates one run; the multi-scene evaluation is the
main performance estimate. Example 6's clip uses different scenes and seeds,
so its endpoint is a visual reference rather than a controlled comparison.

## Running the selected policy

Check out the `assignment-6-rl` branch in the nested `assignment/cpe-aml/`
repository, then run from `asm-6_PyRLSimbot/` with the assignment environment
active:

```bash
python assignmentRL.py --mode eval \
  --load models/q_table_seed_11_example6_100k.json \
  --eval-epsilon 0.15 --safety-margin 4.5 \
  --steps 100000 --seed 706001
```

See the implementation README for setup and experiment reproduction details.
The original assignment starter remains available in this folder.
