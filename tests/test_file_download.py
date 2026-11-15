from pathlib import Path

from playwright.sync_api import Page


def test_download_file(page: Page, tmp_path: Path) -> None:
    page.goto("https://www.playwrightautomation.com/practice.html")

    with page.expect_download() as download_info:
        page.locator("#btn-download-pdf").click()

    download = download_info.value
    destination = tmp_path / download.suggested_filename
    download.save_as(destination)

    assert destination.is_file()
