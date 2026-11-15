from pathlib import Path
from playwright.sync_api import Page, expect


def test_upload_single_file(page: Page) -> None:

    page.goto("https://www.playwrightautomation.com/practice.html")

    page.get_by_role("button", name="File Handling").click()

    file_path = (
        Path(__file__).resolve().parent
        / "test_data"
        / "Playwright_Python_Phase_4_Browser_Scenarios_Complete_Notes.pdf"
    )
    assert file_path.is_file()

    file_inputs = page.locator("input[type='file']")
    expect(file_inputs.first).to_be_attached()
    file_inputs.first.set_input_files(str(file_path))

    result = page.locator("#upload-single-result")

    expect(result).to_contain_text(file_path.name)