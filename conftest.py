import os
import re
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def saucedemo_base_url() -> str:
    return os.environ.get(
        "SAUCEDEMO_BASE_URL",
        "https://www.saucedemo.com",
    ).rstrip("/")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed or call.excinfo is None:
        return

    page = item.funcargs.get("page")
    if page is None or page.is_closed():
        return

    screenshot_dir = Path(item.config.rootpath) / "test-results" / "screenshots"
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    filename = re.sub(r"[^A-Za-z0-9_.-]+", "_", item.nodeid)
    screenshot_path = screenshot_dir / f"{filename}.png"
    page.screenshot(path=str(screenshot_path), full_page=True)
    report.sections.append(("Failure screenshot", str(screenshot_path)))