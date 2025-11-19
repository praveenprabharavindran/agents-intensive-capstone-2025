# agents-intensive-capstone-2025
Capstone project for the 5-Day AI Agents Intensive Course with Google


## Overview

This project sets up and runs the `agents_intensive_capstone` project, Agentic AI based Adaptive Course Generator 

---

## Prerequisites

Before you begin, ensure the following tools are installed:

| Tool           | Minimum Version | Check with Command             |
|----------------|------------------|-------------------------------|
| **Python**     | ≥ 3.10           | `python --version`            |
| **Git**        | (optional)       | `git --version`               |
| **Virtualenv** | (recommended)    | `python -m venv .venv`        |

---

## Clone the Repository (Optional)

You can clone the repository using either SSH or HTTPS:

```bash
# Navigate to the target directory
cd C:\Git

# SSH
git clone git@github.com:praveenprabharavindran/agents-intensive-capstone-2025.git

# HTTPS
git clone https://github.com/praveenprabharavindran/agents-intensive-capstone-2025.git
```

---

## Set Up Your Development Environment

Follow the steps below based on your operating system.

---

### PowerShell (Windows)

```powershell

# (Optional) Remove any existing virtual environment
# Remove-Item -Recurse -Force .venv

# Create a new virtual environment
python -m venv .venv

# Activate the virtual environment
.venv\Scripts\Activate.ps1

# (Optional) Upgrade pip
# python -m pip install --upgrade pip
```

---

### Linux / macOS (Bash)

```bash
# Navigate to the project directory
cd ~/Git/agents-intensive-capstone-2025

# (Optional) Remove any existing virtual environment
# rm -rf .venv

# Create a new virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# (Optional) Upgrade pip
# python -m pip install --upgrade pip
```
---

## Install package in editable mode with dev tools

Installing in editable mode allows you to make changes to the code and see them reflected immediately.

```bash
pip install -e ".[dev]"
```

---