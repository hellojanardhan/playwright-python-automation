from playwright.sync_api import Playwright
from jsonschema import validate

def validate_json_schema(response_json, schema):
    try:
        validate(instance = response.json , schema = schema)
        print("Schema validation successful")
        return True
    except ValidationError as e:
        print("Schema validation is failed")
        return False
    
def test_validate_schema(playwright : Playwright):

    request_context = playwright.request.new_context()
    response = request_context.get("https://mocktarget.apigee.net/json")

    assert response.ok

    response_body = response.json()
    print(response_body)

    json_schema = {
    "$schema": "http://json-schema.org/draft-06/schema#",
    "$ref": "#/definitions/Welcome6",
    "definitions": {
        "Welcome6": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "firstName": {
                    "type": "string"
                },
                "lastName": {
                    "type": "string"
                },
                "city": {
                    "type": "string"
                },
                "state": {
                    "type": "string"
                }
            },
            "required": [
                "city",
                "firstName",
                "lastName",
                "state"
            ],
            "title": "Welcome6"
        }
    }
}
    
    is_valud = validate_json_schema(response_body, json_schema)
    assert is_valid
    request_context.dispose()
