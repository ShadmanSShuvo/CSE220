# CSE 220: Signals and Linear Systems (Sessional)

Department of Computer Science and Engineering
**Bangladesh University of Engineering and Technology (BUET)**
**Semester:** January 2026 | **Student Roll:** `2305025`

---

## Course Overview

CSE 220 Sessional covers foundational and computational aspects of continuous-time and discrete-time signals, linear time-invariant (LTI) systems, transformations (Fourier Series, Continuous/Discrete Fourier Transforms, FFT, Laplace, Z-transform), and practical signal processing applications in Python.

### Assessment Structure
- **Attendance**: 10%
- **Assignments (Onlines, Offlines & Term Project)**: 70%
- **Final Quiz Exam**: 20%

---

## Directory Architecture

```text
CSE220/
├── 00_Course_Outlines/                      # Syllabus, lecture schedule, grading scheme
│   ├── CSE220_Course_Outline.md
│   └── Jan 26 _ CSE 220 Course Outline.docx.pdf
│
├── 01_Basics_and_Lectures/                  # Foundations & lecture demonstrations
│   ├── 01_Python_Basics/                    # Core Python & NumPy basics notebooks
│   │   └── online1_prep_experiments/        # Online 1 signal transformation experiments
│   ├── 02_Python_Numpy_Matplotlib_Tutorials/# 45 progressive NumPy & Matplotlib scripts
│   ├── 03_Numpy_Class_Demos/                # Class demonstration scripts
│   ├── 04_Signals_Properties/               # 20 standalone fundamental signal properties scripts
│   └── 05_Lecture_01_Signals/               # Lecture 1 notes, masks, and signal operations
│
├── 02_Practice_Problems/                    # Lab practice sets & reference solutions
│   ├── Practice_01_Python/                  # Practice Set 1 (Python, signal arrays, outputs)
│   └── Practice_02_Convolution/             # Practice Set 2 (Discrete convolution & solutions)
│   ├── Practice_02_Convolution/             # Practice Set 2 (Discrete convolution & solutions)
│   └── Practice_03_Sampling/                # Practice Set 3 (24-section DSP toolkit & visual suite)
│
├── 03_Onlines/                              # Lab exam sets & past preparations
│   ├── Online_01_Signals_and_Properties/    # Online 1: Signals & properties (sec_A, sec_B, sec_C)
│   ├── Online_02_Convolution/               # Online 2: LTI systems & convolution (sec_A, sec_B, sec_C)
│   ├── Online_03_FS_and_CFT/                # Online 3: Fourier Series & CFT (sec_A, sec_B)
│   ├── Online_04_DFT_and_FFT/               # Online 4: DFT & FFT image processing (sec_A, sec_B)
│   ├── Online_04_DFT_and_FFT/               # Online 4: DFT & FFT image processing (sec_A, sec_B, sec_C)
│   ├── Online_05_Sampling/                  # Online 5: Sampling, ZOH droop & oversampling (Sec_A, Sec_B, Sec_C)
│   └── Past_Batches_and_Prep/               # CSE 22 batch archives & predicted lab questions
│
├── 04_Offlines/                             # Major programming assignments
│   ├── Offline_01_Convolution/              # LTI system simulation & 1D/2D convolution
│   │   ├── v1_initial/                      # Version 1 implementation
│   │   ├── v2_final/                        # Version 2 with refined LTI engine
│   │   └── archives/                        # Submission archives (.zip)
│   ├── Offline_02_FS_and_CFT/               # Fourier Series & Continuous Fourier Transform
│   │   ├── task1_fourier_epicycles/         # Epicycle drawing animation from SVG paths
│   │   ├── task2_cft_edge_detector/         # Continuous Fourier transform 2D edge detection
│   │   ├── submission/                      # Roll 2305025 submission files & archive
│   │   └── archives/                        # Starter package archive (.zip)
│   └── Offline_03_DFT_and_FFT/              # Discrete & Fast Fourier Transforms
│       ├── starter/                         # Official starter package & specifications
│       ├── dev_workspace/                   # Development scripts, drivers & benchmarks
│       ├── test_results_full/               # Verified test suite runs & output comparisons
│       ├── submission/                      # Roll 2305025 submission folder & zip
│       └── archives/                        # Starter package archive (.zip)
│
├── 05_Reference_Materials/                  # Senior notes, handnotes & cheat sheets
│   ├── akib/                                # Lab question bank, cheatsheets & sample sets
│   ├── Mahdi/                               # Theory slides, problems, solutions & reference PDFs
│   └── sami/                                # Handnotes, DSP lab exam guides & reference notebooks
│
└── 06_Project/                              # Term project workspace & documentation
    ├── CSE 220 Project Ideas - Project Ideas.csv  # 50+ project ideas catalog
    └── README.md                            # Project timeline, milestones & tracking
```

---

## Course Schedule & Curriculum Map

| Week | Topic | Assignments & Milestones |
| :---: | :--- | :--- |
| **1** | Python Basics (Environment setup, data structures, loops) | `01_Basics_and_Lectures/01_Python_Basics` |
| **2** | Advanced NumPy, Matplotlib & Basic Signal Plotting | `01_Basics_and_Lectures/02_Python_Numpy_Matplotlib_Tutorials` |
| **3–4** | Signal Representation, Shifting, Scaling & Transformations | **Online 1**: Signals & Properties (`03_Onlines/Online_01_Signals_and_Properties`) |
| **5** | Continuous & Discrete Convolution, LTI Properties | **Offline 1**: Convolution (`04_Offlines/Offline_01_Convolution`) |
| **6–7** | 2D Convolution & Fourier Series Introduction | **Online 2**: Convolution; **Offline 2 Assigned**; **Project Ideas Assigned** (`06_Project`) |
| **8** | Continuous Fourier Transform (CFT) & Frequency Filtering | **Online 3**: FS & CFT (`03_Onlines/Online_03_FS_and_CFT`) |
| **9** | Discrete Fourier Transform (DFT), Radix-2 FFT, BigInt Mul | **Offline 3**: DFT & FFT (`04_Offlines/Offline_03_DFT_and_FFT`) |
| **10** | Frequency Domain Image Processing (Hybrid Images, Phase Swap) | **Online 4**: DFT & FFT (`03_Onlines/Online_04_DFT_and_FFT`) |
| **11** | Project Progress & Demonstration | **Project Update Milestone** (`06_Project`) |
| **12** | Buffer / Review Week | Comprehensive Review & Exam Preparation |
| **13** | Sampling Theorem, Filtering, Laplace & Z-Transform | **Online 5** |
| **13** | Sampling Theorem, Filtering, Laplace & Z-Transform | **Online 5**: Sampling & Reconstruction (`03_Onlines/Online_05_Sampling`) |
| **14** | Final Comprehensive Assessment | **Sessional Quiz Exam** |

---

## Environment Setup & Requirements

```bash
# Recommended Python environment: Python 3.10+
pip install numpy matplotlib scipy pillow imageio
```
