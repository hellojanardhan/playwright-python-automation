from playwright.sync_api import Playwright, expect
import json
import pytest

base_url = "https://restful-booker.herokuapp.com"
def create_token(playwright : Playwright):
    pass    

def read_json_file(file_path):
    file = open(file_path, "r")
    return json.load(file)

@pytest.fixture(scope = "function")
def request_context(playwright : Playwright):
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()


# @pytest.fixture(scope = "function")
def access_token(request_context):
    headers = {
        "Content-Type": "application/json"
    }

    data = read_json_file("../apitesting/token_request_data.json")

    response = request_context.post(
        f"{base_url}/auth",
        data=data,
        headers=headers
    )

    # print("Access token is ",response.json())

    assert response.status == 200

    response_body = response.json()
    assert "token" in response_body

    return response_body["token"]


# Create booking
def test_create_booking(request_context):
    global bookingId
    data = read_json_file("../apitesting/post_request.json")
    response = request_context.post(f"{base_url}/booking" , data = data)
    assert response.ok, "Post request failed"
    assert response.status == 200

    response_body = response.json()
    print("Created booking successfully",response_body)
    assert "bookingid" in response_body
    
    booking = response_body["booking"]
    assert booking["firstname"] == data["firstname"]
    assert booking["lastname"] == data["lastname"]
    assert booking["bookingdates"]["checkin"] == data["bookingdates"]["checkin"]
    assert booking["bookingdates"]["checkout"] == data["bookingdates"]["checkout"]

    bookingId = response_body["bookingid"]
    print("Booking Id is", bookingId)



# GET Booking details
def test_get_by_booking_id(request_context):
    response = request_context.get(f"{base_url}/booking/{bookingId}")
    print("response is ", response, response.json())
    response_body = response.json()
    print(f"Booking details fetched by {bookingId}",response_body)
    assert response.ok
    assert response.status == 200
    assert "firstname" in response_body
    assert "lastname" in response_body


# Get Booking details by firstname
def test_get_by_firstname(request_context):
    params = {
        "firstname" : "James",
        "lastname" : "Chloe"
    }
    response = request_context.get(f"{base_url}/booking",params = params)    
    response_body = response.json()
    print(f'Booking details fetched by {params["firstname"]} and {params["lastname"]}',response_body)

    assert response.ok    
    assert response.status == 200
    assert len(response_body) > 0

    
# Test token is created
def test_token_is_created(request_context):
    token = access_token(request_context)

    print("Access token is:", token)

    assert token


# Partial update
def test_partial_update_booking(request_context):
    token = access_token(request_context)
    headers = {
        "Content-Type" : "application/json",
        "Cookie" : f"token={token}"
    }
    data = read_json_file("../apitesting/patch_request.json")

    response = request_context.patch(
        f"{base_url}/booking/{bookingId}", 
        data = data,
        headers = headers
    )

    response_body = response.json()
    print("Response is",response_body)

    assert response.ok
    assert response.status == 200



# Full update
def test_update_booking_details(request_context):
    token = access_token(request_context)
    headers = {
        "Content-Type" : "application/json",
        "Cookie" : f"token={token}"
    }

    data = read_json_file("../apitesting/put_request.json")

    response = request_context.put(
        f"{base_url}/booking/{bookingId}",
        headers = headers,
        data = data
    )

    response_body = response.json()
    print("Response body is",response_body)

    assert response.ok
    assert response.status == 200

    assert response_body["firstname"] == data["firstname"]
    assert response_body["lastname"] == data["lastname"]
    assert response_body["bookingdates"]["checkin"] == data["bookingdates"]["checkin"]
    assert response_body["bookingdates"]["checkout"] == data["bookingdates"]["checkout"]


# Delete booking by ID
def test_delete_booking_by_id(request_context):

    token = access_token(request_context)
    headers = {
        "Content-Type" : "application/json",
        "Cookie" : f"token={token}"
    }

    response = request_context.delete(
        f"{base_url}/booking/{bookingId}",
        headers = headers
    )       
    # response_body = response.json()
    assert response.ok
    assert response.status == 201