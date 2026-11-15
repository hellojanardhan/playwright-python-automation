# Playwright Automation Tests

Python UI and API test examples using Playwright and pytest.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
playwright install chromium
```

Run the browser tests with:

```powershell
pytest
```

GitHub API authentication tests in `apitesting/test_api_authentication.py`
are skipped unless `GITHUB_TOKEN` is set in the environment. Set it in
PowerShell before running those tests:

```powershell
$env:GITHUB_TOKEN = "<your GitHub token>"
```
