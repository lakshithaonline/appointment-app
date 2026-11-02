# Appointment App: QA and CI Workflow Demo

A small Python example for practising unit testing, defect detection, Git version control, GitHub Actions, pull requests, baselines, and controlled changes.

## Requirements
- Python 3.10 or later (GitHub Actions uses Python 3.12)
- Git
- A GitHub account and a repository you can push to
- Visual Studio Code is recommended

## Run locally
```powershell
py -m unittest -v
py app.py
```

Expected test result: three tests pass. Expected app output: `Cancelled`.

GitHub Actions runs the unit tests on pushes and pull requests using `.github/workflows/tests.yml`.
