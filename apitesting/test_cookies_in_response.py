from playwright.sync_api import Playwright, expect

def test_cookies_in_response(playwright : Playwright):
    request_context = playwright.request.new_context()

    response = request_context.get("https://google.com")

    assert response.status_text == "OK"
    assert response.status == 200

    # Extract all the cookies
    cookies = request_context.storage_state()["cookies"]
    print(cookies)

    for cookie in cookies:
        print(cookie['name'] , cookie['value'] , cookie['domain'])