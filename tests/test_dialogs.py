from playwright.sync_api import Page, expect


PRACTICE_URL = "https://www.playwrightautomation.com/practice.html"


def test_simple_alert(page: Page) -> None:
    page.goto(PRACTICE_URL)

    with page.expect_event("dialog") as dialog_info:
        page.once("dialog", lambda dialog: dialog.accept())
        page.locator("#btn-alert").click()

    assert dialog_info.value.type == "alert"


def test_confirmation_alert(page: Page) -> None:
    page.goto(PRACTICE_URL)

    with page.expect_event("dialog") as dialog_info:
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.locator("#btn-confirm").click()

    assert dialog_info.value.type == "confirm"
    expect(page.locator("#confirm-result")).to_have_text("You pressed Cancel!")


def test_prompt_alert(page: Page) -> None:
    page.goto(PRACTICE_URL)
    name = "Janardhan"

    with page.expect_event("dialog") as dialog_info:
        page.once("dialog", lambda dialog: dialog.accept(name))
        page.locator("#btn-prompt").click()

    assert dialog_info.value.type == "prompt"
    expect(page.locator("#prompt-result")).to_have_text(
        f"Hello {name}! How are you today?"
    )