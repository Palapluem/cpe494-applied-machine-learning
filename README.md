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

## Cross-platform migration setup

The course materials and runnable assignment code are intentionally kept in
two independent repositories. Clone the public course repository first, then
clone the private group repository into its ignored nested path. Do not copy a
Windows `.venv` to macOS; create one fresh environment at the root of each
repository.

### Windows PowerShell

```powershell
New-Item -ItemType Directory -Force D:\Developer | Out-Null
Set-Location D:\Developer
git clone --branch main --single-branch https://github.com/Palapluem/cpe494-applied-machine-learning.git
Set-Location .\cpe494-applied-machine-learning
git clone --branch assignment-4-alife --single-branch https://github.com/Palapluem/cpe-aml.git .\assignment\cpe-aml

py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
deactivate

Set-Location .\assignment\cpe-aml
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r .\asm-1_PySimbot\requirements.txt
python -m pip install -r .\asm-3_PyGASimbot\requirements_GA_windows.txt
python -m pip install -r .\asm-4_PyLifeSimbot\requirements_windows.txt
```

### macOS (Intel or Apple Silicon)

```bash
mkdir -p ~/Developer
cd ~/Developer
git clone --branch main --single-branch https://github.com/Palapluem/cpe494-applied-machine-learning.git
cd cpe494-applied-machine-learning
git clone --branch assignment-4-alife --single-branch https://github.com/Palapluem/cpe-aml.git assignment/cpe-aml

python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
deactivate

cd assignment/cpe-aml
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r asm-1_PySimbot/requirements.txt
python -m pip install -r asm-3_PyGASimbot/requirements_GA_macos.txt
python -m pip install -r asm-4_PyLifeSimbot/requirements_macos.txt
```

The selected baseline is Python 3.11. The pinned Kivy and ffpyplayer versions
have macOS universal2 wheels for CPython 3.11, so the same requirements cover
Intel and Apple Silicon. `kivy.deps.sdl2` and `kivy.deps.glew` remain Windows
extras only. The outer environment is for the course-material repository; the
nested environment is the one used to run the assignments.

## Run Assignments 1–4

Run these commands from the nested `cpe-aml` repository root after activating
its `.venv`. Quoted paths are intentional because the Assignment 1 and 2 file
names contain spaces.

```powershell
python ".\asm-1_PySimbot\Assignment RC.py"
python ".\asm-2_PySimbot\assignment FLC.py"
python ".\asm-3_PyGASimbot\assignmentGA.py"
python ".\asm-4_PyLifeSimbot\assignmentALife.py"
```

```bash
python "./asm-1_PySimbot/Assignment RC.py"
python "./asm-2_PySimbot/assignment FLC.py"
python "./asm-3_PyGASimbot/assignmentGA.py"
python "./asm-4_PyLifeSimbot/assignmentALife.py"
```

The same entry points also work when launched from their own assignment
directory. Assignment 3 writes generated CSV/PNG files under
`asm-3_PyGASimbot/results/`; Assignment 4 writes under
`asm-4_PyLifeSimbot/results/`.

For short smoke runs, Assignment 1 and 2 accept `PYSIMBOT_MAX_TICK`, Assignment
3 accepts `PYSIMBOT_TICKS` and `PYSIMBOT_GENERATIONS`, and Assignment 4 accepts
`ALIFE_MAX_TICK`, `ALIFE_SEED`, and `ALIFE_AUTO_CLOSE`. These are test-only
overrides; the submitted assignment defaults remain unchanged.

## Verification

Syntax and non-GUI contract checks can be run from the nested repository root:

```bash
python -m py_compile \
  "asm-1_PySimbot/Assignment RC.py" \
  "asm-2_PySimbot/assignment FLC.py" \
  asm-3_PyGASimbot/assignmentGA.py \
  asm-4_PyLifeSimbot/assignmentALife.py
python -m unittest discover -s tests -v
```

The nested repository also runs these checks and dependency installation on
`macos-latest` through GitHub Actions. A CI pass is not the same as physically
verifying every interactive Kivy window on both Mac architectures.

## Assignment 1: PySimbot

The Assignment 1 controller is available at [Assignment RC.py](<assignment/Assignment 1/Assignment RC.py>). Development and collaboration happen in the separate [cpe-aml repository](https://github.com/Palapluem/cpe-aml), which is excluded from this repository to keep the two Git histories independent.

The controller is deterministic: it uses the eight infrared sensors and food smell to seek food, avoid obstacles, escape narrow corridors, and recover from local loops. It does not make random control decisions.

## Assignment 2: Fuzzy Logic Control

The Assignment 2 brief and hint are in [Assignment 2](<assignment/Assignment 2/>). The related lecture examples and solution references are in [Lecture 1: Fuzzy Logic Control](<lecture/Lecture 1_Fuzzy Logic Control/>).

The current implementation is maintained in the separate [cpe-aml repository](https://github.com/Palapluem/cpe-aml), under [`asm-2_PySimbot/`](https://github.com/Palapluem/cpe-aml/tree/assignment-4-alife/asm-2_PySimbot) on the `assignment-4-alife` branch. It follows the assignment hint with deterministic fuzzification, rule firing, defuzzification, state logging, and loop/stuck recovery.

## Assignment 3: Genetic Algorithm

The Assignment 3 brief is in [Assignment 3](<assignment/Assignment 3/>). The
supporting material is in [Lecture 2: Genetic Algorithm](<lecture/Lecture 2_Genetic Algorithm/>).

The current PySimbot starter is maintained in the separate [cpe-aml
repository](https://github.com/Palapluem/cpe-aml), under
[`asm-3_PyGASimbot/`](https://github.com/Palapluem/cpe-aml/tree/assignment-4-alife/asm-3_PyGASimbot)
on the `assignment-4-alife` branch.

The Assignment 3 controller keeps the complete 110-byte chromosome crossover,
the branch's GA parameter set, deterministic blocked-move recovery, and
repeat-eating statistics. GA operators are stochastic, so eater counts and
fitness vary between runs; use the detailed [Assignment 3 logic design](https://github.com/Palapluem/cpe-aml/blob/assignment-4-alife/asm-3_PyGASimbot/LOGIC_DESIGN.md)
and `generation_stats.csv` to compare runs. Set `PYSIMBOT_PLOT=1` and
`PYSIMBOT_LIVE_PLOT=1` for the live red-best/blue-average learning curve
beside the simulator, as shown in the supplied videos.

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
nested repository. With the nested repository's own `.venv` activated, install
the matching platform requirements and run it from either repository root or
the assignment directory.

Windows PowerShell:

```powershell
cd D:\cpe494-applied-machine-learning\assignment\cpe-aml
python -m pip install -r .\asm-4_PyLifeSimbot\requirements_windows.txt
python .\asm-4_PyLifeSimbot\assignmentALife.py
```

macOS:

```bash
cd ~/Developer/cpe494-applied-machine-learning/assignment/cpe-aml
python -m pip install -r ./asm-4_PyLifeSimbot/requirements_macos.txt
python ./asm-4_PyLifeSimbot/assignmentALife.py
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
