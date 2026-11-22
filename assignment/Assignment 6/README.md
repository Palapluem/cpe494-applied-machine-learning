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
| Safety handling | Sensor-based margin 4.5 units; a near-corner guard; four recovery turns after a blocked move |

The contextual reward terms from Example 6 use the robot's sensor readings and
action. They are hand-designed guidance, while food and collision rewards use
observed events. The policy is frozen during evaluation. The safety filter uses
the existing distance sensors and does not read hidden food coordinates.

## Results and graphs

The instructor's latest targets are Eat > 0.005 and Hit < 0.002 events per
action, equivalent to Eat > 5 and Hit < 2 per 1,000 actions. After the corner
fix, a paired check used 20 new scenes for each start type and 5,000 actions
per scene:

| Start | Eat / 1,000 actions | Hit / 1,000 actions |
| --- | ---: | ---: |
| Official | 8.38 | 0.04 |
| Random | 8.48 | 0.07 |

The fix addresses two known corner cases; its comparison with the old filter
has trade-offs and does not establish a general performance gain. The final
policy graph is a separate 100,000-tick trace: 856 foods and 10 blocked moves,
or Eat 8.560 and Hit 0.100 per 1,000 ticks. Both graphs mark (0, 0) as a
display reference, then show measured cumulative rates every 1,000 ticks; a
rate at zero actions is undefined. The axes show events per action, with no
smoothing. The training graph records the earlier training run that produced
the selected Q-table.

- [Final frozen-policy graph](../cpe-aml/asm-6_PyRLSimbot/assets/final_policy_eat_hit_rates.png)
- [Online training graph](../cpe-aml/asm-6_PyRLSimbot/assets/single_run_eat_hit_rates.png)
- [Full evaluation report](../cpe-aml/asm-6_PyRLSimbot/EXAMPLE6_OPTIMIZATION.md)
- [Review evidence](../cpe-aml/asm-6_PyRLSimbot/evidence/review/)

The single-run graph illustrates one run. The earlier 60-scene result in the
report used the previous filter. Example 6's clip uses different scenes and
seeds, so its endpoint is a visual reference rather than a controlled comparison.

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
