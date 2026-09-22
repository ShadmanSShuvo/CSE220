# Centralized Repository Archives (`/Archives`)

This directory houses all compressed `.zip` distribution packages, starter archives, and student submission packages across the **CSE 220** curriculum.

Each assignment and practice module has its own isolated subfolder to avoid filename collisions (such as the separate assignment submissions named `2305025.zip`).

---

## Directory Organization

```text
Archives/
├── 02_Practice_Problems/
│   ├── Practice_01_Python/
│   │   ├── 2305025.zip                      # Student Practice 01 submission bundle
│   │   └── files.zip                        # Supporting files & data archive
│   └── Practice_03_Sampling/
│       └── Mahdi.zip                        # Senior Mahdi sampling resources archive
│
└── 04_Offlines/
    ├── Offline_01_Convolution/
    │   ├── CSE-220_Offline_Convolution.zip     # Offline 1 v1 submission archive
    │   ├── CSE-220_Offline_Convolution-v2.zip  # Offline 1 v2 final submission archive
    │   └── offline_convolution_submission.zip  # v1 docs submission archive
    ├── Offline_02_FS_and_CFT/
    │   ├── Jan2026_CSE220_Offline_FS_CFT.zip   # Official starter bundle (instructors)
    │   └── 2305025.zip                         # Student submission bundle (Roll 2305025)
    └── Offline_03_DFT_and_FFT/
        ├── Jan2026_CSE220_Offline_DFT_FFT.zip  # Official starter bundle (instructors)
        └── 2305025.zip                         # Student submission bundle (Roll 2305025)
```

---

## Catalog & Details

### Practice Problems (`02_Practice_Problems/`)
| Module Subfolder | Archive Name | Size | Active Working Directory Counterpart |
| :--- | :--- | :---: | :--- |
| `Practice_01_Python/` | `2305025.zip` | 2.3 KB | `02_Practice_Problems/Practice_01_Python/` |
| `Practice_01_Python/` | `files.zip` | 101.5 KB | `02_Practice_Problems/Practice_01_Python/files/` |
| `Practice_03_Sampling/` | `Mahdi.zip` | 1.3 MB | `02_Practice_Problems/Practice_03_Sampling/Mahdi/` |

### Major Offlines (`04_Offlines/`)
| Module Subfolder | Archive Name | Size | Active Working Directory Counterpart |
| :--- | :--- | :---: | :--- |
| `Offline_01_Convolution/` | `CSE-220_Offline_Convolution-v2.zip` | 1.2 MB | `04_Offlines/Offline_01_Convolution/v2_final/` |
| `Offline_01_Convolution/` | `CSE-220_Offline_Convolution.zip` | 1.2 MB | `04_Offlines/Offline_01_Convolution/v1_initial/` |
| `Offline_01_Convolution/` | `offline_convolution_submission.zip` | 1.2 MB | `04_Offlines/Offline_01_Convolution/v1_initial/docs/` |
| `Offline_02_FS_and_CFT/` | `Jan2026_CSE220_Offline_FS_CFT.zip` | 6.2 MB | `04_Offlines/Offline_02_FS_and_CFT/task1_fourier_epicycles/` |
| `Offline_02_FS_and_CFT/` | `2305025.zip` | 6.2 MB | `04_Offlines/Offline_02_FS_and_CFT/submission/2305025/` |
| `Offline_03_DFT_and_FFT/` | `Jan2026_CSE220_Offline_DFT_FFT.zip` | 6.5 MB | `04_Offlines/Offline_03_DFT_and_FFT/starter/` |
| `Offline_03_DFT_and_FFT/` | `2305025.zip` | 6.5 MB | `04_Offlines/Offline_03_DFT_and_FFT/submission/2305025/` |

---

## Extracting an Archive

To test or inspect any archive into a temporary folder:
```bash
unzip -t Archives/04_Offlines/Offline_02_FS_and_CFT/2305025.zip
```
