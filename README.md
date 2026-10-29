# CPE494 Applied Machine Learning

Course workspace for **CPE494 Special Topic IV: Applied Machine Learning** (Semester 1/2026).

## Contents

| Path | Purpose |
| --- | --- |
| `assignment/Assignment 1/` | Assignment brief and a tracked copy of the Assignment 1 controller. |
| `assignment/Assignment 2/` | Fuzzy Logic Control (FLC) brief and hint image. |
| `assignment/Assignment 3/` | Genetic Algorithm (GA) assignment brief. |
| `assignment/Assignment 4/` | Artificial Life assignment brief (kept on root `main`). |
| `assignment/Assignment 5/` | Official Artificial Neural Networks (ANN) assignment brief and starter links. |
| `assignment/cpe-aml/` | Separate fork of the group-assignment repository; intentionally kept as its own Git repository. |
| `lecture/Lecture 1_Fuzzy Logic Control/` | Fuzzy-control lecture notes, exercises, and solution references. |
| `lecture/Lecture 2_Genetic Algorithm/` | Genetic Algorithm lecture notes and reference slides. |
| `lecture/Lecture 3_Artificial Life/` | Artificial Life lecture notes and slides (kept on root `main`). |
| `lecture/Lecture 4_Introduction to Neural Networks/` | ANN lecture slides, PDF export, and a sample ANN exercise. |
| `lecture/Lecture 5_Decision Making/` | Decision-making under uncertainty slides and spreadsheet exercises. |
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
git clone --branch main --single-branch https://github.com/Palapluem/cpe-aml.git .\assignment\cpe-aml

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
git clone --branch main --single-branch https://github.com/Palapluem/cpe-aml.git assignment/cpe-aml

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
`ALIFE_MAX_TICK`, `ALIFE_SEED`, `ALIFE_AUTO_CLOSE`, `ALIFE_WINDOW_TICKS`,
`ALIFE_TICKS_PER_FRAME`, `ALIFE_OUTPUT_DIR`, `ALIFE_PLOT_SNAPSHOT_INTERVAL`,
and experiment switches for selection, crossover, mutation, energy costs/reward,
and maximum energy. The current A4 preset is energy-ranked top-25% random-parent
selection, single-point crossover, per-gene mutation `0.020`, and random newborn
`0.05`. The test history, parameter rationale, and caveats are in the nested
repository's [A4 submission parameter sheet](https://github.com/Palapluem/cpe-aml/blob/main/asm-4_PyLifeSimbot/SUBMISSION_PARAMETERS.md);
earlier single-run results in archived notes are not the latest comparison.
Assignment 4 also opens a separate live learning chart;
set `ALIFE_OUTPUT_DIR` to keep its result CSV/PNG files outside the repository,
and `ALIFE_PLOT_SNAPSHOT_INTERVAL=25000` to save chart snapshots during a run.
`ALIFE_WINDOW_TICKS` is useful when a short smoke run would otherwise contain
fewer than one 5,000-tick result window.

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

The current implementation is maintained in the separate [cpe-aml repository](https://github.com/Palapluem/cpe-aml), under [`asm-2_PySimbot/`](https://github.com/Palapluem/cpe-aml/tree/main/asm-2_PySimbot) on `main`. It follows the assignment hint with deterministic fuzzification, rule firing, defuzzification, state logging, and loop/stuck recovery.

## Assignment 3: Genetic Algorithm

The Assignment 3 brief is in [Assignment 3](<assignment/Assignment 3/>). The
supporting material is in [Lecture 2: Genetic Algorithm](<lecture/Lecture 2_Genetic Algorithm/>).

The current PySimbot starter is maintained in the separate [cpe-aml
repository](https://github.com/Palapluem/cpe-aml), under
[`asm-3_PyGASimbot/`](https://github.com/Palapluem/cpe-aml/tree/main/asm-3_PyGASimbot)
on `main`.

The Assignment 3 controller keeps the complete 110-byte chromosome crossover,
the branch's GA parameter set, deterministic blocked-move recovery, and
repeat-eating statistics. GA operators are stochastic, so eater counts and
fitness vary between runs; use the detailed [Assignment 3 logic design](https://github.com/Palapluem/cpe-aml/blob/main/asm-3_PyGASimbot/LOGIC_DESIGN.md)
and `generation_stats.csv` to compare runs. Set `PYSIMBOT_PLOT=1` and
`PYSIMBOT_LIVE_PLOT=1` for the live red-best/blue-average learning curve
beside the simulator, as shown in the supplied videos.

## Assignment 4: Artificial Life

Artificial Life materials are kept in the course repository on `main`:

- assignment brief: `assignment/Assignment 4/AML Assignment 04 ALife 2026.pdf`
- lecture files: `lecture/Lecture 3_Artificial Life/`
- PySimbot workspace: `asm-4_PyLifeSimbot/` in the nested `cpe-aml` repository

The nested `cpe-aml` repository remains separate and its `main` branch contains
the shared A1-A4 baseline. Assignment-specific work is kept on a feature branch;
the new ANN starter is on `assignment-5-ann`. The root repository's `main`
contains the course-level Assignment 4 brief and lecture materials listed above.

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

## Assignment 5: Artificial Neural Networks

The official brief is [AML Assignment 05 ANN 2026.pdf](<assignment/Assignment 5/AML Assignment 05 ANN 2026.pdf>).
Lecture 4 materials are in
[`Lecture 4: Introduction to Neural Networks`](<lecture/Lecture 4_Introduction to Neural Networks/>);
Lecture 5 slides and spreadsheet exercises are in
[`Lecture 5: Decision Making Under Uncertainty`](<lecture/Lecture 5_Decision Making/>).
The ANN exam example in Lecture 4 is lecture material, separate from the
Assignment 5 specification.

The assignment asks students to collect demonstration data, train an ANN from
the 9 sensor inputs (8 IR readings and smell angle) to 2 movement outputs
(turn and move), then evaluate the controller in PyNNSimbot. The supplied
starter is in the separate fork on the
[`assignment-5-ann` branch](https://github.com/Palapluem/cpe-aml/tree/assignment-5-ann/asm-5_PyNNSimbot).
The fork now provides collection, corrected scaling/filenames, training with
episode holdout and measured simulator evaluation. Its
[Assignment 5 guide](https://github.com/Palapluem/cpe-aml/blob/assignment-5-ann/asm-5_PyNNSimbot/README.md)
includes reproducible commands and results.

The [ANN research report](https://github.com/Palapluem/cpe-aml/blob/assignment-5-ann/asm-5_PyNNSimbot/RESEARCH_IMPROVEMENTS.md)
records eight primary papers, failed ablations, a model frozen before final
testing, and 30 fresh paired episodes. On the same seeds, mean food improved
from 129.60 to 140.67 and collisions fell from 34.73 to 28.13. The separate
randomized-start food result is inconclusive; results are specific to this map.

The instructor requires modified Python sources only for submission. Keep
datasets/model weights local for a possible TA request; post the clip and
learning graph to the FB group separately.

If the nested clone is currently on `main`, check out the ANN starter branch:

```bash
cd assignment/cpe-aml
git fetch origin refs/heads/assignment-5-ann:refs/remotes/origin/assignment-5-ann
git switch --track -c assignment-5-ann origin/assignment-5-ann
```
