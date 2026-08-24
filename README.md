# Python IT Automation Toolkit

A hands-on Python project focused on building practical IT automation and system diagnostic capabilities.

This project is being developed incrementally to strengthen my Python fundamentals while applying them to real-world IT infrastructure and automation use cases.

## 🎯 Project Goal

The goal of this project is to build a lightweight IT automation toolkit that can collect system information, perform basic diagnostics, monitor system health, analyze system data, and eventually automate common infrastructure tasks.

I'm using this project to develop practical Python skills that complement my existing experience with IT support, PowerShell, Windows administration, and infrastructure technologies.

## 🚧 Current Status

### Version 1.1 — System Health Monitoring

Version 1.1 builds on the original system diagnostics foundation by adding system resource monitoring and Python dependency management.

### Version 1.0 — System Diagnostics Foundation

The initial version established the foundation of the toolkit and demonstrated basic Python system-information gathering.

Capabilities:

- Detects the operating system
- Retrieves the OS release/version
- Uses Python's `platform` module
- Organizes diagnostic functionality into a reusable function
- Provides structured command-line output

### Version 1.1 — System Health Monitoring

The latest version expands the diagnostic functionality to monitor system resource utilization.

New capabilities:

- Monitors CPU usage
- Monitors memory usage
- Monitors disk usage
- Uses the `psutil` library for system resource information
- Adds Python dependency management through `requirements.txt`
- Tests system health information from the command line
- Provides structured system health output
- Uses a dedicated Git feature branch and pull request workflow

## 🛠️ Technologies

- Python 3
- psutil
- Git
- GitHub
- Visual Studio Code

## 🐍 Python Concepts Used

- Modules and imports
- Functions
- Variables
- f-strings
- Conditional execution
- Command-line output
- System information gathering
- External Python packages
- Dependency management
- Basic system resource monitoring

## 📊 Current System Diagnostics

The toolkit currently collects:

- Operating system
- OS release/version
- CPU usage
- Memory usage
- Disk usage

Example output:

```text
--- System Diagnostics ---
Operating System: Darwin
OS Release: 25.6.0
CPU Usage: 24.5%
Memory Usage: 71.6%
Disk Usage: 6.6%
