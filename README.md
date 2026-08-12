# CPE494 Applied Machine Learning

Course workspace for **CPE494 Special Topic IV: Applied Machine Learning** (Semester 1/2026).

## Contents

| Path | Purpose |
| --- | --- |
| `assignment/Assignment 1/` | Assignment brief and a tracked copy of the Assignment 1 controller. |
| `assignment/cpe-aml/` | Separate fork of the group-assignment repository; intentionally kept as its own Git repository. |
| `tmp/pdfs/` | Reference image extracted from the assignment brief. |

## Assignment 1: PySimbot

The Assignment 1 controller is available at [Assignment RC.py](<assignment/Assignment 1/Assignment RC.py>). Development and collaboration happen in the separate [cpe-aml repository](https://github.com/Palapluem/cpe-aml), which is excluded from this repository to keep the two Git histories independent.

The controller is deterministic: it uses the eight infrared sensors and food smell to seek food, avoid obstacles, escape narrow corridors, and recover from local loops. It does not make random control decisions.

## Repository convention

- Keep lecture materials and course-level files in this repository.
- Keep group-assignment source, dependencies, and assignment-specific history inside `assignment/cpe-aml/`.
- Run and submit the PySimbot work through `Assignment RC.py`, not the removed `run.py` script.
