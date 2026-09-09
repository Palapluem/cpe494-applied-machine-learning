# CPE494 Applied Machine Learning

Course workspace for **CPE494 Special Topic IV: Applied Machine Learning** (Semester 1/2026).

## Contents

| Path | Purpose |
| --- | --- |
| `assignment/Assignment 1/` | Assignment brief and a tracked copy of the Assignment 1 controller. |
| `assignment/Assignment 2/` | Fuzzy Logic Control (FLC) brief and hint image. |
| `assignment/Assignment 3/` | Genetic Algorithm (GA) assignment brief. |
| `assignment/Assignment 4/` | Artificial Life assignment brief (kept on root `main`). |
| `assignment/cpe-aml/` | Separate fork of the group-assignment repository; intentionally kept as its own Git repository. |
| `lecture/Lecture 1_Fuzzy Logic Control/` | Fuzzy-control lecture notes, exercises, and solution references. |
| `lecture/Lecture 2_Genetic Algorithm/` | Genetic Algorithm lecture notes and reference slides. |
| `lecture/Lecture 3_Artificial Life/` | Artificial Life lecture notes and slides (kept on root `main`). |
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
per generation: a robot may leave the food rectangle and re-enter it, and each
new entry counts as another successful eat. PySimbot's `just_eat` flag prevents
the same stationary overlap from being counted once per frame. Fitness records
the closest food distance and the repeat-eating contribution, while
`generation_stats.csv` reports eater count, repeat-eater count, maximum entries
by one robot, and total food contacts. The controller clears PySimbot's
geometry sensor caches between generations, preventing long-run memory growth.
GA operators are
stochastic, so eater counts and fitness can vary between runs; use the detailed [Assignment 3 logic design](https://github.com/Palapluem/cpe-aml/blob/assignment-3-ga/asm-3_PyGASimbot/LOGIC_DESIGN.md) and
`generation_stats.csv` to compare runs.

## Assignment 4: Artificial Life

Artificial Life materials are kept in the course repository on `main`:

- assignment brief: `assignment/Assignment 4/AML Assignment 04 ALife 2026.pdf`
- lecture files: `lecture/Lecture 3_Artificial Life/`
- PySimbot workspace: `asm-4_PyLifeSimbot/` in the nested `cpe-aml` repository

The nested `cpe-aml` repository remains separate: its `assignment-3-ga` and
`main` branches contain the GA workspace, while its `assignment-4-alife`
branch contains `asm-4_PyLifeSimbot`. The root repository's `main` contains
the course-level Assignment 4 brief and lecture materials listed above.

The Assignment 4 entry point is `asm-4_PyLifeSimbot/assignmentALife.py` in the
nested repository. Install its platform requirements in the shared virtual
environment, then run it from that folder:

```powershell
cd D:\cpe494-applied-machine-learning\assignment\cpe-aml
git switch assignment-4-alife
python -m pip install -r .\asm-4_PyLifeSimbot\requirements_windows.txt
python .\asm-4_PyLifeSimbot\assignmentALife.py
```

Repository boundaries are intentional: this root repository stores course
briefs and lecture material directly on `main`; the nested `cpe-aml`
repository stores runnable assignment work on one branch per assignment. The
nested repository is ignored by the root `.gitignore`, so commits made in one
repository cannot silently modify the other.

## Repository convention

- Keep lecture materials and course-level files in this repository.
- Keep group-assignment source, dependencies, and assignment-specific history inside `assignment/cpe-aml/`.
- Run and submit the PySimbot work through `Assignment RC.py`, not the removed `run.py` script.
