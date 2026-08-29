# CPE494 Applied Machine Learning

Course workspace for **CPE494 Special Topic IV: Applied Machine Learning** (Semester 1/2026).

## Contents

| Path | Purpose |
| --- | --- |
| `assignment/Assignment 1/` | Assignment brief and a tracked copy of the Assignment 1 controller. |
| `assignment/Assignment 2/` | Fuzzy Logic Control (FLC) brief and hint image. |
| `assignment/Assignment 3/` | Genetic Algorithm (GA) assignment brief. |
| `assignment/cpe-aml/` | Separate fork of the group-assignment repository; intentionally kept as its own Git repository. |
| `lecture/Lecture 1_Fuzzy Logic Control/` | Fuzzy-control lecture notes, exercises, and solution references. |
| `lecture/Lecture 2_Genetic Algorithm/` | Genetic Algorithm lecture notes and reference slides. |
| `tmp/pdfs/` | Local preview images extracted while reviewing PDFs; generated previews are ignored. |

## Assignment 1: PySimbot

The Assignment 1 controller is available at [Assignment RC.py](<assignment/Assignment 1/Assignment RC.py>). Development and collaboration happen in the separate [cpe-aml repository](https://github.com/Palapluem/cpe-aml), which is excluded from this repository to keep the two Git histories independent.

The controller is deterministic: it uses the eight infrared sensors and food smell to seek food, avoid obstacles, escape narrow corridors, and recover from local loops. It does not make random control decisions.

## Assignment 2: Fuzzy Logic Control

The Assignment 2 brief and hint are in [Assignment 2](<assignment/Assignment 2/>). The related lecture examples and solution references are in [Lecture 1: Fuzzy Logic Control](<lecture/Lecture 1_Fuzzy Logic Control/>).

The current implementation is maintained in the separate [cpe-aml repository](https://github.com/Palapluem/cpe-aml), under [`asm-2_PySimbot/`](https://github.com/Palapluem/cpe-aml/tree/assignment-2-flc/asm-2_PySimbot) on the `assignment-2-flc` branch. It follows the assignment hint with deterministic fuzzification, rule firing, defuzzification, state logging, and loop/stuck recovery.

## Assignment 3: Genetic Algorithm

The Assignment 3 brief is in [Assignment 3](<assignment/Assignment 3/>). The
supporting material is in [Lecture 2: Genetic Algorithm](<lecture/Lecture 2_Genetic Algorithm/>).

The current PySimbot starter is maintained in the separate [cpe-aml
repository](https://github.com/Palapluem/cpe-aml), under
[`asm-3_PyGASimbot/`](https://github.com/Palapluem/cpe-aml/tree/assignment-3-ga/asm-3_PyGASimbot)
on the `assignment-3-ga` branch.

A fresh validation run reached all 100 generations: maximum fitness rose from
338 to 985, final average fitness was 598.16, and the final generation had
26/100 eaters. The Assignment 3 controller also clears PySimbot's geometry
sensor caches between generations, preventing the long-run memory growth that
previously made the final generation unresponsive. Since GA operators are
stochastic, an earlier seed reached 993; this difference is expected and does
not indicate a code change. The detailed result and flow are documented in the
[Assignment 3 logic design](https://github.com/Palapluem/cpe-aml/blob/assignment-3-ga/asm-3_PyGASimbot/LOGIC_DESIGN.md).
Each run records detailed per-generation behaviour in `generation_stats.csv`.

## Repository convention

- Keep lecture materials and course-level files in this repository.
- Keep group-assignment source, dependencies, and assignment-specific history inside `assignment/cpe-aml/`.
- Run and submit the PySimbot work through `Assignment RC.py`, not the removed `run.py` script.
