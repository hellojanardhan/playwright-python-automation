from playwright.sync_api import Playwright,expect
import json
bookingid = None
def test_create_booking(playwright:Playwright):
    global bookingid
    base_url = "https://restful-booker.herokuapp.com"
    request_context = playwright.request.new_context()
    request_body = {
        "firstname" : "Jim",
        "lastname" : "Brown",
        "totalprice" : 111,
        "depositpaid" : True,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }
    response = request_context.post(f"{base_url}/booking",data = request_body)
    response_body = response.json()
    assert response.status == 200
    assert response.ok
    print(response_body)

    bookingid = response_body["bookingid"]
    print("Booking id is :",bookingid)
    request_context.dispose()


def test_get_bookingid(playwright:Playwright):
    base_url = "https://restful-booker.herokuapp.com"
    request_context = playwright.request.new_context()
    response = request_context.get("f{base_url}/booking/{bookingid}")
    response_body = response.json()
    print(response_body)
