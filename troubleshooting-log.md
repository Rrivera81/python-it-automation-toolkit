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
