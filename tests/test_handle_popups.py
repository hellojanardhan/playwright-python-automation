import re

from playwright.sync_api import Page, expect


PRACTICE_URL = "https://www.playwrightautomation.com/practice.html"


def test_popup_opens_and_is_registered_in_context(page: Page) -> None:
    page.goto(PRACTICE_URL)

    with page.expect_popup() as popup_info:
        page.get_by_text("Open Mobilewright Window", exact=True).click()

    popup = popup_info.value
    assert popup in page.context.pages
    expect(popup).to_have_url(re.compile(r"^https?://"))

