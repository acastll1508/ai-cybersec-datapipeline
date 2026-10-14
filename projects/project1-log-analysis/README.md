# Project 1 - Cyberattack Log Analysis 

This project focuses on the analysis and visualization of real-world 
cyberattack logs in order to identify malicious patterns, attacker behavior 
and temporal trends.

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

The datasets included in this project are synthetic but realistic
security log simulations designed to mimic:

- Linux SSH authentication logs (e.g. `auth.log`)
- Brute-force attack traces from honeypots
- Firewall or web server logs (future extensions) 

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
│   ├── processed/
│   │   └── README.md
│   └── raw/                       # Original simulated log files
│       ├── README.md
│       ├── apache_access.log
│       ├── auth.log
│       ├── empty.csv
│       ├── empty.log
│       ├── firewall.log
│       ├── non_supported_ext.img
│       ├── sample.csv
│       ├── ssh_bruteforce.log
│       └── web_access.log
├── notebooks/                     # Exploratory and analysis notebooks
│   └── 01_exploratory_analysis.ipynb
├── pyproject.toml
├── reports/
│   └── figures
│       └── README.md
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   ├── legacy.txt
│   ├── lock.txt
│   ├── notebook.txt
│   └── viz.txt
├── src/                           # Core data ingestion and preprocessing logic
│   ├── __init__.py
│   ├── detect_patterns.py
│   ├── load_data.py               # Data loading utilities
│   ├── preprocess/                # Log parsing and cleaning
│   │   ├── __init__.py
│   │   ├── general_processor.py
│   │   ├── main_function.py
│   │   ├── parsers.py
│   │   └── specific_processor.py
│   └── visualize.py               # Exploratory analysis and visualization
└── tests/                         # Unit tests for ingestion and preprocessing
    ├── load_data/                  # Load data tests
    │    ├── test_load_csv.py
    │    ├── test_load_invalid.py
    │    ├── test_load_log.py
    │    └── test_load_NonSupportedFile.py
    ├── preprocess/                  # Preprocess tests
    │    ├── test_preprocess_basic.py
    │    ├── test_preprocess_invalid.py
    │    └── test_preprocess_ip.py
    └── test_detect_patterns.py     # Placeholder: implementation pending.
~~~

---

## Current Status

✔  Module 1: Data Loading (completed)
✔  Module 2: Preprocessing (completed)
🔜 Module 3: Pattern Detection (next)
⬜ Module 4: Visualization (Planned)

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
pytest 
~~~

> This will automatically discover and execute all tests under the tests/ directory.

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

Creates and activate a virtual environment, and installs dependencies.

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


## Planned Commands

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

> ⚠️ Not yet implemented (planned module)

---

#### 🔹 Run pattern detection

~~~bash
make detect
~~~

> ⚠️ Not yet implemented (planned module)

---

#### 🔹 Run full pipeline

~~~bash
make all
~~~

Run the complete pipeline:

1. Load data  ✅
2. Preprocess logs  ✅
3. Detect attack patterns  🔜

> ⚠️ Not yet implemented (planned module)

---

## Pipeline Overview

The project follows a modular pipeline design:

~~~text
load_data → preprocess → detect_patterns → visualize
~~~

Each step is independently executable but can also be chained 
using `make all`.

> ⚠️ Not yet implemented (planned module)

---
