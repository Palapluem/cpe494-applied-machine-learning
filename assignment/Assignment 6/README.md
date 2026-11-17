# Assignment 6: Reinforcement Learning

This folder keeps the instructor's assignment brief and the supplied starter file. The runnable implementation, simulator changes, experiment results, models, and plots are maintained in the `assignment-6-rl` branch of the `cpe-aml` fork:

- [Implementation and complete experiment report](../cpe-aml/asm-6_PyRLSimbot/README.md)
- [GitHub branch](https://github.com/Palapluem/cpe-aml/tree/assignment-6-rl)
- [GitHub Actions: macOS and Windows Q-learning checks](https://github.com/Palapluem/cpe-aml/actions/runs/42783367553)

## Course files

- `AML Assignment 06 RL 2026.pdf` — assignment brief.
- `Assignment 6 (to start with).py.txt` — original starter, kept unchanged.
- `../lecture/Lecture 6_Reinforcement Learning/` — the source material. Only the PDF files were used to study the lecture; the PowerPoint files were not used.

## Running the implementation

The implementation lives in the fork rather than this course-material folder. From this directory, enter `../cpe-aml/asm-6_PyRLSimbot/` and follow its README for setup, training, evaluation, and reproducing the plots. To run the selected Q-table on the GUI after setting up the environment:

```bash
python assignmentRL.py --mode eval --load models/q_table_seed_11.json \
  --eval-epsilon 0.2 --steps 5000 --seed 42
```

The selected policy uses 20% exploration at evaluation time. Greedy-only evaluation (`epsilon=0`) became stuck in the held-out runs; see the experiment report for full results and limitations.

The assignment PDF does not specify the exact submission file list or format. Confirm that with the instructor or TA. The implementation README identifies the files needed to run the code and the optional trained Q-table.

## Parameter check

The brief's Q-learning outline initializes Q to zero, sets α = 0.5 and γ =
0.9, and chooses a greedy action 90% of the time with exploration 10% of the
time. The single-run graph uses those values (`epsilon = 0.1`). The controller
also adds implementation choices for sensor state, reward shaping, movement,
and a fourth action (backward); the brief's C-like example shows three actions.
The assignment asks students to define states, actions, and rewards, so these
extensions should be described as our design choices rather than instructor-
specified parameter values.
