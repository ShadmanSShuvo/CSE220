# Implementation Plan - Reorganize CSE220 Repository Directory Structure

Organize all existing files and directories in `/Users/shuvo/Dev/CSE220` into logical, intuitive categories. No code inside any file will be modified.

## Proposed Directory Hierarchy

```
CSE220/
├── 01_Basics_and_Lectures/
│   ├── PythonBasics/               # Basic Python & NumPy concepts, elementary signal plots
│   ├── PythonNumpyMatplotlib/      # Introductory NumPy and Matplotlib tutorial scripts
│   ├── NumpyClass/                 # NumPy class examples & plot sampling demos
│   ├── Signals_Properties/         # Signal properties (time shifting, scaling, energy/power, etc.)
│   └── lec1/                       # Lecture 1 notes and signal transformation scripts
├── 02_Practice_Problems/
│   ├── Practice-1/                 # Practice Problem Set 1 solution scripts, PDFs & output plots
│   └── Practice2-convolution/      # Convolution practice problems & solution scripts
├── 03_Onlines/
│   ├── Online1-Practice/           # Online 1 preparation notebooks, predicted questions & solutions
│   ├── Online-1-CSE22/             # Online 1 templates & solutions for CSE 22 batch
│   └── Onlines/                    # Online 1 Set A & B submissions, solutions & specs
├── 04_Offlines/
│   └── Offline/                    # Offline 1 Convolution project (v1, v2, specs, tests)
└── 05_Reference_Materials/
    ├── akib/                       # Reference notes, PDFs & exam sets from Akib
    ├── Mahdi/                      # Reference coding problems & notebooks from Mahdi
    └── sami/                       # Reference handnotes, reference guides & tutorials from Sami
```

## User Review Required

> [!NOTE]
> All code files (`.py`, `.ipynb`, `.md`, `.pdf`, `.png`, etc.) will remain 100% untouched. Only their folder locations will be organized into logical top-level category directories. Git tracking history will be preserved using `git mv`.

## Proposed Changes

### [Directory Structure Reorganization]

#### [MOVE] [PythonBasics](file:///Users/shuvo/Dev/CSE220/PythonBasics) $\rightarrow$ `01_Basics_and_Lectures/PythonBasics`
#### [MOVE] [PythonNumpyMatplotlib](file:///Users/shuvo/Dev/CSE220/PythonNumpyMatplotlib) $\rightarrow$ `01_Basics_and_Lectures/PythonNumpyMatplotlib`
#### [MOVE] [NumpyClass](file:///Users/shuvo/Dev/CSE220/NumpyClass) $\rightarrow$ `01_Basics_and_Lectures/NumpyClass`
#### [MOVE] [Signals_Properties](file:///Users/shuvo/Dev/CSE220/Signals_Properties) $\rightarrow$ `01_Basics_and_Lectures/Signals_Properties`
#### [MOVE] [lec1](file:///Users/shuvo/Dev/CSE220/lec1) $\rightarrow$ `01_Basics_and_Lectures/lec1`

#### [MOVE] [Practice-1](file:///Users/shuvo/Dev/CSE220/Practice-1) $\rightarrow$ `02_Practice_Problems/Practice-1`
#### [MOVE] [Practice2-convolution](file:///Users/shuvo/Dev/CSE220/Practice2-convolution) $\rightarrow$ `02_Practice_Problems/Practice2-convolution`

#### [MOVE] [Online1-Practice](file:///Users/shuvo/Dev/CSE220/Online1-Practice) $\rightarrow$ `03_Onlines/Online1-Practice`
#### [MOVE] [Online-1-CSE22](file:///Users/shuvo/Dev/CSE220/Online-1-CSE22) $\rightarrow$ `03_Onlines/Online-1-CSE22`
#### [MOVE] [Onlines](file:///Users/shuvo/Dev/CSE220/Onlines) $\rightarrow$ `03_Onlines/Onlines`

#### [MOVE] [Offline](file:///Users/shuvo/Dev/CSE220/Offline) $\rightarrow$ `04_Offlines/Offline`

#### [MOVE] [akib](file:///Users/shuvo/Dev/CSE220/akib) $\rightarrow$ `05_Reference_Materials/akib`
#### [MOVE] [Mahdi](file:///Users/shuvo/Dev/CSE220/Mahdi) $\rightarrow$ `05_Reference_Materials/Mahdi`
#### [MOVE] [sami](file:///Users/shuvo/Dev/CSE220/sami) $\rightarrow$ `05_Reference_Materials/sami`

---

## Verification Plan

### Automated Tests / Structure Check
- Run `git status` to verify all moves were properly tracked by Git without unintended modifications or lost files.
- Run `find . -maxdepth 3 -not -path '*/.*'` to confirm clean directory tree structure.
