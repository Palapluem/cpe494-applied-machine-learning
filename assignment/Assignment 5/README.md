# Assignment 5: Artificial Neural Networks

The official brief is [AML Assignment 05 ANN 2026.pdf](<AML Assignment 05 ANN 2026.pdf>).
It assigns students to collect demonstration data, train an ANN, and test the
resulting robot controller in PyNNSimbot.

The brief describes 9 inputs (8 infrared sensors and the smell angle) and 2
outputs (turn and move). It says to combine collected history into
`history_all.csv`, train and save `assignmentANN_model.h5`, then evaluate
the model in a 5,000-step simulation.

Lecture materials:

- [Lecture 4: Introduction to Neural Networks](<../../lecture/Lecture 4_Introduction to Neural Networks/>)
- [Lecture 5: Decision Making Under Uncertainty](<../../lecture/Lecture 5_Decision Making/>)

The PyNNSimbot starter is maintained in the separate fork on the
[`assignment-5-ann` branch](https://github.com/Palapluem/cpe-aml/tree/assignment-5-ann/asm-5_PyNNSimbot).
See its README for setup, data collection, training, evaluation and submission
commands.

The fork now implements collection, consistent scaling, ANN training with
episode holdout, simulator evaluation and learning curves. Reproduction
commands and measured results are in its
[experiment record](https://github.com/Palapluem/cpe-aml/blob/assignment-5-ann/asm-5_PyNNSimbot/EXPERIMENTS.md).

The subsequent [research and improvement report](https://github.com/Palapluem/cpe-aml/blob/assignment-5-ann/asm-5_PyNNSimbot/RESEARCH_IMPROVEMENTS.md)
compares corrective data, noise, model capacity, weighting and Dense-head
calibration. A fresh 30-seed paired benchmark improves mean food 129.60 -> 140.67
and collisions 34.73 -> 28.13, with uncertainty and failed runs included.
The original result is retained separately rather than compared across seed sets.

## Instructor's submission update

Submit only modified Python files. Do not submit CSV/history datasets or large
model files. Keep those locally in case the TA asks; post the clip and learning
graph to the FB group separately.

The fork's assignmentANN_package.py prepares the source-only submission.
