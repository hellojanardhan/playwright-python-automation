from playwright.sync_api import Page


def test_cookies_can_be_added_and_cleared(page: Page) -> None:
    context = page.context
    context.add_cookies(
        [
            {"name": "James", "value": "James", "url": "https://example.com"},
            {"name": "John", "value": "John", "url": "https://example.com"},
            {
                "name": "session_id",
                "value": "abc123",
                "url": "https://example.com",
            },
        ]
    )

    assert {cookie["name"] for cookie in context.cookies()} == {
        "James",
        "John",
        "session_id",
    }

    context.clear_cookies(name="James")
    assert {cookie["name"] for cookie in context.cookies()} == {"John", "session_id"}

    context.clear_cookies()
    assert context.cookies() == []