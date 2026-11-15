from playwright.sync_api import Browser, Page


def test_browser_contexts_do_not_share_cookies(
    browser: Browser,
    page: Page,
) -> None:
    isolated_context = browser.new_context()
    try:
        page.context.add_cookies(
            [{"name": "session_id", "value": "context-one", "url": "https://example.com"}]
        )

        cookies = page.context.cookies("https://example.com")
        assert [(cookie["name"], cookie["value"]) for cookie in cookies] == [
            ("session_id", "context-one")
        ]
        assert isolated_context.cookies("https://example.com") == []
    finally:
        isolated_context.close()
