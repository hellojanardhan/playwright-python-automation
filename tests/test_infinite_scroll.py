from playwright.sync_api import (
    Locator,
    Page,
    TimeoutError as PlaywrightTimeoutError,
    expect,
)


BOOKS_URL = "https://www.playwrightautomation.com/infinite-scroll.html"


def scroll_until_book_found(page: Page, target_book: str) -> Locator:
    book = page.get_by_text(target_book, exact=True)
    sentinel = page.locator("[data-testid='scroll-sentinel']")

    for _ in range(10):
        if book.count() > 0:
            return book
        previous_count = page.locator("[data-book-index]").count()
        sentinel.scroll_into_view_if_needed()
        try:
            page.wait_for_function(
                "previous => document.querySelectorAll('[data-book-index]').length > previous",
                arg=previous_count,
                timeout=5_000,
            )
        except PlaywrightTimeoutError:
            if page.locator("[data-book-index]").count() == previous_count:
                break

    return book


def test_find_blue_eye(page: Page) -> None:
    page.goto(BOOKS_URL)
    expect(page.get_by_text("The Blue Eye", exact=True)).to_be_visible()


def test_find_playwright_mastery(page: Page) -> None:
    page.goto(BOOKS_URL)
    book = scroll_until_book_found(page, "Playwright Mastery: Advanced Edition")
    expect(book).to_be_visible()