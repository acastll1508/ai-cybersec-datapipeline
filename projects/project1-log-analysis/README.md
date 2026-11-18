# Project 1 - Cyberattack Log Analysis

This project focuses on the analysis of synthetic cybersecurity log
datasets, currently centered on SSH authentication events, to identify
suspicious activity patterns and analyze temporal trends.

It is the first project of the **AI & Data Analytics for Offensive Cybersecurity**
portfolio and serves as a foundation for later Machine Learning-based detection.

---

## Objectives

- Analyze authentication and network logs related to cyberattacks
- Identify malicious IP addresses and attack patterns
- Perform temporal analysis of attack activity
- Build a clean and reproducible data analysis pipeline
- Apply data analysis skills in a cybersecurity context

---

## Dataset Description

The project includes synthetic security log datasets designed to mimic
different types of security events, including:

- Linux SSH authentication logs (e.g. `auth.log`)
- Brute-force attack traces from honeypots
- Firewall or web server logs (future extensions)

> The current preprocessing and pattern detection modules focus on SSH
> authentication events. Support for other log sources is planned for
> future extensions.

> They do not contain real user data and are intended
  for educational and analytical purposes only.

---

## Data Notice

Public IP addresses appearing in the logs are randomly used
for simulation realism and do not imply real malicious activity.

---

## Project Structure

~~~text

project1-log-analysis/
├── Makefile
├── README.md
├── data/                          # Raw and processed datasets
│   ├── processed/
│   │   └── README.md
│   └── raw/                       # Original simulated log files
│       ├── README.md
│       ├── apache_access.log
│       ├── auth.log
│       ├── empty.csv
│       ├── empty.log
│       ├── firewall.log
│       ├── non_supported_ext.img
│       ├── sample.csv
│       ├── ssh_bruteforce.log
│       └── web_access.log
├── notebooks/                     # Exploratory and analysis notebooks
│   └── 01_exploratory_analysis.ipynb
├── pyproject.toml
├── reports/
│   └── figures/
│       └── README.md
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   ├── legacy.txt
│   ├── lock.txt
│   ├── notebook.txt
│   └── viz.txt
├── src/                           # Data ingestion, preprocessing and pattern detection
│   ├── __init__.py
│   ├── load_data.py               # Data loading utilities
│   ├── preprocess/                # Log parsing and cleaning
│   │   ├── __init__.py
│   │   ├── general_processor.py
│   │   ├── main_function.py
│   │   ├── parsers.py
│   │   └── specific_processor.py
│   ├── detect_patterns/                # Authentication event pattern detection
│   │   ├── __init__.py
│   │   ├── brute_force.py
│   │   ├── event_frequency.py
│   │   ├── main_function.py
│   │   ├── multiple_users.py
│   │   ├── success_after_failures.py
│   │   └── validation.py
│   └── visualize.py               # Exploratory analysis and visualization
└── tests/                         # Unit tests for all implemented modules
    ├── load_data/                 # Load data tests
    │   ├── test_load_csv.py
    │   ├── test_load_invalid.py
    │   ├── test_load_log.py
    │   └── test_load_NonSupportedFile.py
    ├── preprocess/                  # Preprocess tests
    │   ├── test_preprocess_basic.py
    │   ├── test_preprocess_invalid.py
    │   └── test_preprocess_ip.py
    └── detect_patterns/             # Pattern detection tests
        ├── test_brute_force.py
        ├── test_event_frequency.py
        ├── test_multiple_users.py
        ├── test_success_after_failures.py
        └── test_validation.py
~~~

---

## Current Status

✔  Module 1: Data Loading (completed)
✔  Module 2: Preprocessing (completed)
✔  Module 3: Pattern Detection (completed)
⬜ Module 4: Visualization and analysis (Planned)

---

## Pattern Detection

The pattern detection module analyzes preprocessed SSH authentication events
to identify suspicious activity based on IP addresses, usernames and time windows.

It currently implements four detection mechanisms:

| Detection | Default threshold | Time window |
|---|---:|---:|
| SSH brute-force attempts | 5 failed attempts | 5 minutes |
| Successful login after failures | 3 failed attempts | 5 minutes |
| Multiple usernames from one IP | 5 distinct usernames | 5 minutes |
| Anomalous event frequency | 21 authentication events | 1 minute |

The detectors generate structured alerts containing relevant information
about the detected activity, such as source IP addresses, event counts,
usernames and timestamps.

These alerts identify potentially suspicious behavior and should not
be interpreted as definitive confirmation of a cyberattack.

---

## Running this project

All commands must be executed from the project root:

~~~bash
projects/project1-log-analysis
~~~

---

## Environment setup

~~~bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements/base.txt
python -m pip install -r requirements/dev.txt
python -m pip install -r requirements/viz.txt
python -m pip install -r requirements/notebook.txt
~~~

For convenience, these steps can also be performed using the Makefile commands described below.

---

## Example execution

~~~
python -m src.load_data
~~~

> This command loads the raw log file and validates that the data ingestion
pipeline works correctly.

---

## Testing Strategy

Initial testing was performed using manual execution of test scripts to validate
data ingestion and preprocessing logic.

Once the behavior was validated, all tests were migrated to an automated
pytest-based testing suite to ensure reproducibility and maintainability.

---

## Running Tests

All tests are executed using `pytest`.

From the project root:

~~~bash
cd projects/project1-log-analysis
source .venv/bin/activate
python -m pytest
~~~

> This command automatically discovers and executes all tests
> under the tests/ directory.

---

## Makefile Usage

This project includes a `Makefile` to manage the development environment
and common tasks.

All commands must be executed from the project root:


~~~bash
cd projects/project1-log-analysis
~~~


### Available Commands

#### 🔹 Setup environment

~~~bash
make venv
source .venv/bin/activate
make install
~~~

Creates and activates a virtual environment, then installs dependencies.

---

~~~bash
make check
~~~

Validate environment

---

~~~bash
make freeze
~~~

Saves a snapshot of installed package versions to

~~~text
requirements/lock.txt
~~~

This is useful for:

Reproducibility of the environment, debugging dependency issues, and
tracking exact package versions used in the project.

Note: This file complements the dependency specification files;
it does not replace them.

---

#### 🔹 List installed packages

~~~bash
make list
~~~

View installed packages in the current virtual environment.

---

#### 🔹 Run tests

~~~bash
make test
~~~

Executes all unit tests using pytest.

---

#### 🔹 Launch Jupyter Notebook

~~~bash
make notebook
~~~

---

#### 🔹 Register kernel

~~~bash
make kernel
~~~

This allows to select the project environment inside Jupyter
Notebook or JupyterLab in order to ensure the correct dependencies
and interpreter are being used.

#### 🔹 Clean environment

~~~bash
make clean
~~~

Removes the project's virtual environment.

---


## Planned Makefile Commands

The data loading, preprocessing and pattern detection modules have been
implemented and tested independently.

However, their corresponding Makefile execution targets and the full
pipeline orchestration are still pending.

#### 🔹 Run data loading

~~~bash
make load
~~~

> ⚠️  Planned command for data ingestion; not yet available in Makefile.

---

#### 🔹 Run preprocessing

~~~bash
make preprocess
~~~

> ⚠️ Planned Makefile target. The preprocessing module is already
> implemented and tested independently.

---

#### 🔹 Run pattern detection

~~~bash
make detect
~~~

> ⚠️ Planned Makefile target. The pattern detection module is already
> implemented and tested independently.

---

#### 🔹 Run full pipeline

The following command is planned but not implemented yet:

~~~bash
make all
~~~

The planned pipeline will execute:

1. Load data  ✅
2. Preprocess logs  ✅
3. Detect attack patterns  ✅

> ⚠️ Full pipeline orchestration is not yet implemented.

---

## Pipeline Overview

The project follows a modular pipeline design:

~~~text
load_data → preprocess → detect_patterns → visualize
~~~

Each module is developed and tested independently. Full pipeline orchestration is planned for
a future stage.

---
