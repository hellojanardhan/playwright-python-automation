import os
import pytest
import base64
from playwright.sync_api import Playwright, expect

# Basic Authentication
#user : admin
#password : admin
def test_basic_authentication(playwright : Playwright):
    request_context = playwright.request.new_context()
    creds = base64.b64encode(b"admin:admin").decode("utf-8")
    headers = {
        "Authorization" : f"Basic {creds}" 
    }
    response = request_context.get(
        "https://the-internet.herokuapp.com/basic_auth",
        headers = headers
    )
    assert response.ok
    assert response.status == 200
    response_body = response.text()
    print("response body",response_body)
    
    request_context.dispose()
    

# BEARER TOKEN AUTHENTICATION
# url : https://api.github.com/user/repos
def test_bearer_token_authentication(playwright : Playwright):
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        pytest.skip("Set GITHUB_TOKEN to run GitHub API authentication tests")

    request_context = playwright.request.new_context()
    response = request_context.get(
        "https://api.github.com/user/repos",
        headers = {"Authorization" : f"Bearer {token}"}
    )
    
    assert response.ok
    assert response.status
    
    response_body = response.json()
    print("Response is ",response_body)
    
# BEARER TOKEN AUTHENTICATION
# https://api.github.com/user  
def test_get_github_user_details(playwright : Playwright):
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        pytest.skip("Set GITHUB_TOKEN to run GitHub API authentication tests")

    request_context = playwright.request.new_context()
    response = request_context.get(
        "https://api.github.com/user",
        headers = {"Authorization" : f"Bearer {token}"}
    )
    
    assert response.ok
    assert response.status
    
    response_body = response.json()
    print("Respons body",response_body)
    
    
# API KEY AUTHENTICATION






# OAUTH AUTHENTICATION
