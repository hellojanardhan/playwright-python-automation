from playwright.sync_api import Page, expect

def test_shadow_web_elements(page: Page) -> None:
    page.goto("https://www.playwrightautomation.com/shadow-dom-lab.html")
    
    page.get_by_role("textbox", name="admin@playwrightlab.com").fill("admin@playwrightlab.com")
    page.locator("input[type='password']").fill("Playwright@123")
    page.get_by_test_id("shadow-remember").check()
    page.locator("#sd-login-btn").click()
    
    result = page.get_by_text("Login Successful", exact=True)
    expect(result).to_be_visible()
    expect(result).to_have_text("Login Successful")