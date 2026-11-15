from playwright.sync_api import Playwright, expect
def test_headers_in_response(playwright : Playwright):
    request_context = playwright.request.new_context()

    response = request_context.get("https://google.com")
    assert response.status == 200
    assert response.status_text == "OK"

    # extract all the headers

    headers = response.headers
    for key , value in headers.items():
        print(f"{key} ---> {value}")

    # validate specific headers
    print(headers.get("content-type"))
    assert "text/html" in headers.get("content-type")


    assert "gzip" == headers.get("content-encoding")


    # Validate specific header in headers
    assert "server" in  headers
    assert "x-xss-protection" in headers

