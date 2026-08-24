# Troubleshooting & Lessons Learned

## V1: System Diagnostics Automation

### 1. Python Indentation (Whitespace is Syntax)
* **Issue:** The script would not run the function at the bottom of the file.
* **Cause:** In Python, indentation dictates code blocks. The `if __name__ == "__main__":` block was accidentally indented with spaces, making Python think it was trapped inside the function above it.
* **Fix:** Removed the spaces so the `if` statement touched the absolute left margin of the document.
* **Lesson Learned:** Unlike PowerShell or Bash, Python relies entirely on whitespace rather than brackets. Spacing is strictly enforced.

### 2. Terminal Directory Context
* **Issue:** Running `python3 main.py` resulted in a "file not found" error.
* **Cause:** A new terminal window defaulted to the Mac root home directory (`~`) instead of the project folder.
* **Fix:** Used `cd ~/Documents/python-it-automation-toolkit` to navigate to the correct path, and reactivated the virtual environment using `source .venv/bin/activate`.
* **Lesson Learned:** Always verify your current directory path in the command prompt before executing environment-specific scripts.

### 3. Basic Authentication Deprecation (Git)
* **Issue:** `git push` threw a fatal authentication error when using my GitHub password.
* **Cause:** GitHub (and most enterprise IT environments) no longer supports basic password authentication for terminal commands due to security risks. 
* **Fix:** Generated a Personal Access Token (PAT) in GitHub Developer Settings with `repo` scopes to act as a secure, temporary password.
* **Lesson Learned:** Modern command-line tools require token-based authentication (PATs) instead of standard passwords.

### 4. Git Syntax & Typos
* **Issue:** Received terminal errors like `command not found: gti` and `pathspec 'main.psy' did not match`.
* **Cause:** Rapid typing in the CLI led to minor typos during the staging phase.
* **Fix:** Carefully re-ran the commands with the correct syntax (`git add main.py`).
* **Lesson Learned:** The command line is completely unforgiving with typos and file extensions. Always double-check before hitting Enter.

# Troubleshooting Log — V1.1 System Health Monitoring

This document records troubleshooting issues encountered while developing Version 1.1 of the Python IT Automation Toolkit.

---

## Issue 1 — Python Command Not Found

### Problem

Running:

    python --version

returned:

    zsh: command not found: python

### Cause

macOS was configured to use `python3` instead of `python`.

### Resolution

Used:

    python3 --version

Python was successfully detected.

The project was then executed using:

    python3 main.py

---

## Issue 2 — Virtual Environment Not Activated

### Problem

Attempting to activate the virtual environment from the wrong directory returned:

    source: no such file or directory: .venv/bin/activate

### Cause

The terminal was not currently inside the project directory.

### Resolution

Changed to the project directory:

    cd ~/Documents/python-it-automation-toolkit

Then activated the virtual environment:

    source .venv/bin/activate

The terminal prompt confirmed activation by displaying:

    (.venv)

---

## Issue 3 — main.py Could Not Be Found

### Problem

Running:

    python3 main.py

from the home directory produced an error indicating that the file could not be found.

### Cause

The terminal was executing the command from the wrong directory.

### Resolution

Navigated to the project directory:

    cd ~/Documents/python-it-automation-toolkit

Then ran:

    python3 main.py

The script executed successfully.

---

## Issue 4 — psutil Dependency Was Not Initially Installed

### Problem

The project required the `psutil` Python library for system resource monitoring.

An initial check using:

    python -m pip show psutil

returned:

    WARNING: Package(s) not found: psutil

### Cause

The dependency had not yet been installed in the project's Python environment.

### Resolution

Installed the dependency using:

    python -m pip install psutil

The installation completed successfully.

The dependency was then recorded in:

    requirements.txt

with:

    psutil

This allows the required package to be recreated when setting up the project on another system.

---

## Issue 5 — Attempting to Run psutil Directly

### Problem

Attempting to execute:

    psutil

directly from the terminal returned:

    zsh: command not found: psutil

### Cause

`psutil` is a Python library and is not intended to be executed as a standalone terminal command.

### Resolution

The package was used by importing it into the Python script:

    import psutil

The project then accessed the library through Python code.

### Lesson Learned

Python packages installed through pip are generally used by importing them into a Python program rather than executing the package name directly from the shell.

---

## Issue 6 — NameError During System Health Check

### Problem

After adding system resource threshold checking, the script returned:

    NameError: name 'cpu_usage' is not defined

### Cause

The threshold-checking logic referenced `cpu_usage`, `memory_usage`, and `disk_usage` before those values had been properly assigned to variables.

### Resolution

Updated the script so the resource values were first assigned to variables:

    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

The variables were then used for both output and threshold checking.

The script was tested again and executed successfully.

---

## Issue 7 — Adding System Resource Monitoring

### Problem

The original V1.0 version only collected basic operating system information.

### Resolution

Expanded the system diagnostic function using `psutil`.

The toolkit now collects:

- Operating system
- OS release
- CPU usage
- Memory usage
- Disk usage

Example output:

    --- System Diagnostics ---
    Operating System: Darwin
    OS Release: 25.6.0
    CPU Usage: 24.5%
    Memory Usage: 71.6%
    Disk Usage: 6.6%

---

## Issue 8 — Adding System Health Threshold Logic

### Problem

The toolkit initially displayed resource usage but did not interpret the results.

### Resolution

Added conditional logic to identify high resource utilization.

The script checks whether CPU, memory, or disk usage reaches or exceeds the configured threshold.

Example logic:

    if cpu_usage >= 80 or memory_usage >= 80 or disk_usage >= 80:
        print("WARNING: System resource usage is high!")

This introduced practical use of Python conditional statements and variables for basic automation.

---

## Issue 9 — Git Feature Branch Had No Upstream Branch

### Problem

After committing the system health monitoring changes, attempting to push the feature branch initially returned an error indicating that the branch did not have an upstream branch.

### Cause

The local `feature/system-health` branch had not yet been connected to its corresponding remote branch on GitHub.

### Resolution

Used:

    git push --set-upstream origin feature/system-health

The branch was successfully pushed to GitHub and configured to track the remote branch.

---

## Issue 10 — Git Remote / Repository Error

### Problem

Git initially returned an error indicating that `origin` did not appear to be a Git repository.

### Cause

The local Git configuration or repository context was not being recognized correctly when the push was attempted.

### Resolution

Verified the current directory using:

    pwd

Verified the repository status using:

    git status

Verified the configured GitHub remote using:

    git remote -v

The remote was confirmed as:

    https://github.com/Rrivera81/python-it-automation-toolkit.git

After correcting the repository context and Git configuration, the feature branch was successfully pushed to GitHub.

---

## Issue 11 — requirements.txt Not Initially Visible on GitHub

### Problem

The `requirements.txt` file existed locally in the project but was not initially visible on GitHub.

### Cause

The file had been created locally but had not yet been tracked and committed by Git.

Git identified the file as an untracked file.

### Resolution

Added the file to Git:

    git add requirements.txt

Committed the change:

    git commit -m "Add Python dependencies"

Then pushed the commit:

    git push

The `requirements.txt` file subsequently appeared on the GitHub feature branch.

---

## Issue 12 — Verifying the Feature Branch on GitHub

### Problem

The updated files initially appeared to be missing when viewing the default `main` branch.

### Cause

The development work was completed on the separate:

    feature/system-health

branch.

The `main` branch had not yet received the changes.

### Resolution

Switched the GitHub repository view to:

    feature/system-health

The updated files were confirmed to be present, including:

- `main.py`
- `requirements.txt`
- `README.md`
- `screenshots/`
- `troubleshooting-log.md`

---

## GitHub Pull Request Workflow

After completing and testing the feature, a pull request was created from:

    feature/system-health

into:

    main

The pull request was verified as:

    Able to merge

The pull request documents the development and testing of the system health monitoring functionality before merging the feature into the main branch.

---

## Final Result

Version 1.1 successfully expanded the Python IT Automation Toolkit from basic system diagnostics into basic system health monitoring.

The toolkit can now:

- Detect the operating system
- Retrieve the OS release
- Monitor CPU usage
- Monitor memory usage
- Monitor disk usage
- Identify high system resource utilization
- Use an external Python dependency through `psutil`
- Manage dependencies through `requirements.txt`

The development process also provided practical experience with:

- Python virtual environments
- Python package installation
- Python modules and imports
- Variables
- Conditional logic
- Git branches
- Git commits
- Git remotes
- GitHub repositories
- Pull requests
- Dependency management
- Troubleshooting development environments

The V1.1 feature was developed using a dedicated Git feature branch:

    feature/system-health

and tested locally before being pushed to GitHub.

---

## Lessons Learned

This version reinforced that troubleshooting is an important part of development.

Several issues were caused not by the Python code itself, but by the development environment, including the current working directory, virtual environment activation, dependency installation, and Git configuration.

The troubleshooting process helped reinforce the importance of:

1. Verifying the current working directory.
2. Confirming the active Python environment.
3. Checking dependencies before debugging application code.
4. Reading error messages carefully.
5. Verifying Git repository status before pushing changes.
6. Using feature branches for isolated development.
7. Testing changes before committing them.
8. Documenting problems and resolutions for future reference.
