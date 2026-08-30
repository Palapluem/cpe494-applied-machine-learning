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

The Assignment 3 controller now follows the complete 110-byte crossover shown
in the assignment example, keeps both child orientations, and retains the
starter's 10% random-new (`MR_count`) group alongside 10% elitism. Fuzzy
actions are normalized by active rule strength, and a deterministic sensor-based
recovery handles blocked/zero-step moves. The food is treated as one fixed goal
per generation: a robot stops after its first contact while the other robots
continue, so each robot can contribute at most one successful eat. Fitness also
records the closest food distance reached during a run, while actual food
contacts remain visible in `generation_stats.csv`. The controller clears
PySimbot's geometry sensor caches between generations, preventing long-run
memory growth. GA operators are
stochastic, so eater counts and fitness can vary between runs; use the detailed [Assignment 3 logic design](https://github.com/Palapluem/cpe-aml/blob/assignment-3-ga/asm-3_PyGASimbot/LOGIC_DESIGN.md) and
`generation_stats.csv` to compare runs.

## Repository convention

- Keep lecture materials and course-level files in this repository.
- Keep group-assignment source, dependencies, and assignment-specific history inside `assignment/cpe-aml/`.
- Run and submit the PySimbot work through `Assignment RC.py`, not the removed `run.py` script.
