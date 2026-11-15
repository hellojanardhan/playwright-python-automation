# PLAYWRIGHT INTERVIEW QUESTIONS AND ANSWERS
## Experience: 1 Year | Python – playwright.sync_api

# PHASE 1: PLAYWRIGHT FUNDAMENTALS

## 1. What is Playwright?

**Answer:**

Playwright is an open-source browser automation framework developed by Microsoft. It is used for end-to-end testing and browser automation of web applications.

It supports Chromium, Firefox, and WebKit browsers. It also provides features like auto-waiting, cross-browser testing, browser context isolation, and parallel execution.

## 2. Why do you prefer Playwright over Selenium?

**Answer:**

I prefer Playwright because it provides built-in auto-waiting, reliable locators, browser context isolation, and easy handling of multiple tabs and browser interactions.

It reduces the need for unnecessary explicit waits and helps us write more reliable automation scripts.

**Comparison:**

- Selenium uses the WebDriver protocol, whereas Playwright uses browser-specific automation protocols.
- Playwright provides built-in auto-waiting.
- Playwright supports browser context isolation.
- Playwright supports Chromium, Firefox, and WebKit.
- Both support multiple tabs and windows.

## 3. Explain Playwright architecture.

**Answer:**

Playwright follows a client-server architecture.

The test script communicates with the Playwright driver through the language-specific client. The driver communicates with the browser using browser-specific protocols and executes browser operations such as clicking, typing, navigation, and validation.

**Architecture:**

Python Test Script → Playwright Client → Playwright Driver → Browser → Web Application.

## 4. Which browsers does Playwright support?

**Answer:**

Playwright supports three major browser engines:

1. Chromium – Used by Chrome and Edge.
2. Firefox – Mozilla Firefox.
3. WebKit – Used by Safari.

We can execute automation scripts across these browsers to validate cross-browser compatibility.

**Example:**

```python
browser = p.chromium.launch()
browser = p.firefox.launch()
browser = p.webkit.launch()
```

## 5. What are the advantages of Playwright?

**Answer:**

The main advantages of Playwright are:

1. Built-in auto-waiting.
2. Cross-browser testing.
3. Browser context isolation.
4. Multiple tabs and windows handling.
5. Network interception.
6. Screenshot and video recording.
7. Trace Viewer and debugging tools.
8. Parallel test execution.
9. Support for multiple programming languages.

# BROWSER, CONTEXT AND PAGE

## 6. What is the difference between Browser, BrowserContext, and Page?

**Answer:**

Browser represents the browser instance.

BrowserContext represents an isolated browser session, similar to an independent incognito session.

Page represents an individual browser tab within a browser context.

**Example:**

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    page.goto("https://example.com")

    browser.close()
```

## 7. What is BrowserContext? Why do we use it?

**Answer:**

BrowserContext provides an isolated browser session. Each context maintains its own cookies, local storage, and session storage.

We use it to test multiple users independently without sharing session data.

**Example:**

```python
context1 = browser.new_context()
page1 = context1.new_page()

context2 = browser.new_context()
page2 = context2.new_page()
```

Here, both pages belong to separate browser sessions.

## 8. What is the difference between Headless and Headed mode?

**Answer:**

Headed mode launches the browser with a visible user interface, whereas headless mode runs the browser in the background without displaying the UI.

I use headed mode for debugging and headless mode for CI/CD execution.

**Example:**

```python
# Headed mode
browser = p.chromium.launch(headless=False)

# Headless mode
browser = p.chromium.launch(headless=True)
```

## 9. What is the difference between sync_api and async_api?

**Answer:**

Playwright provides synchronous and asynchronous APIs.

The sync API executes commands sequentially using normal Python functions, whereas the async API uses async and await to handle asynchronous operations.

I prefer sync_api because it is simpler to implement and understand for my automation framework.

**Comparison:**

- Sync API uses normal functions.
- Async API uses async def.
- Sync API uses with.
- Async API uses async with.
- Async API requires await for asynchronous operations.

## 10. How do you create your first Playwright script?

**Answer:**

First, I initialize Playwright, launch the browser, create a page, navigate to the application, perform actions, validate the expected result, and close the browser.

**Example:**

```python
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    expect(page).to_have_title("Swag Labs")

    print(page.url)

    browser.close()
```

# PYTEST AND DEBUGGING

## 11. How do you execute Playwright tests using Pytest?

**Answer:**

I write test cases as Python functions with names starting with test_. I execute them using Pytest commands.

Pytest identifies the test functions and runs them.

**Example:**

```python
from playwright.sync_api import sync_playwright, expect

def test_homepage():

    with sync_playwright() as p:

        browser = p.chromium.launch()

        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        expect(page).to_have_title("Swag Labs")

        browser.close()
```

**Execution command:**

```bash
pytest -v
```

## 12. What are Playwright Inspector and Codegen?

**Answer:**

Playwright Inspector is a debugging tool that helps us inspect locators, execute actions step by step, and debug automation scripts.

Codegen records browser interactions and generates Playwright automation code.

**Commands:**

```bash
# Inspector
PWDEBUG=1 pytest -s

# Codegen
playwright codegen https://www.saucedemo.com/
```

# PHASE 2: LOCATORS

## 13. What is a Locator in Playwright?

**Answer:**

A locator is a mechanism used to identify web elements on a page.

Playwright locators are lazy, meaning the element is resolved when we perform an action or assertion.

Locators also support auto-waiting and retryability.

**Example:**

```python
username = page.locator("#user-name")

username.fill("standard_user")
```

## 14. What are the different types of Playwright locators?

**Answer:**

Playwright provides several built-in locator methods to identify elements based on roles, text, labels, placeholders, titles, alternative text, and test IDs.

**Examples:**

```python
page.get_by_role("button", name="Login")

page.get_by_text("Welcome")

page.get_by_label("Username")

page.get_by_placeholder("Enter email")

page.get_by_title("Close")

page.get_by_alt_text("Company logo")

page.get_by_test_id("login-button")
```

## 15. Why is get_by_role() the first choice?

**Answer:**

get_by_role() is generally my first choice because it identifies elements based on their ARIA role and accessible name.

It improves readability, maintainability, and helps us interact with the application from an accessibility perspective.

**Example:**

```python
page.get_by_role("button", name="Login").click()
```

## 16. What is the difference between get_by_text() and get_by_role()?

**Answer:**

get_by_text() locates elements based on visible text, whereas get_by_role() identifies elements based on their accessible role and accessible name.

**Example:**

```python
# Text locator
page.get_by_text("Welcome")

# Role locator
page.get_by_role("button", name="Login")
```

## 17. What is get_by_label()?

**Answer:**

get_by_label() locates form controls using their associated label text.

I prefer it when a proper accessible label is available because labels provide a stable and meaningful way to identify form fields.

**HTML:**

```html
<label for="email">Email address</label>
<input id="email" type="email">
```

**Python:**

```python
page.get_by_label("Email address").fill("test@gmail.com")
```

## 18. What is get_by_placeholder()? Why should we not always prefer it?

**Answer:**

get_by_placeholder() locates input fields using placeholder text.

However, placeholders are temporary hints and disappear visually when users enter data. They are not a replacement for proper labels.

So, I prefer get_by_label() when an accessible label is available.

**Example:**

```python
page.get_by_placeholder("Enter email").fill("test@gmail.com")
```

## 19. What are get_by_title() and get_by_alt_text()?

**Answer:**

get_by_title() locates elements using their title attribute, whereas get_by_alt_text() locates images using their alternative text.

**HTML:**

```html
<img src="logo.png" alt="Company logo">

<button title="Close window">X</button>
```

**Python:**

```python
page.get_by_alt_text("Company logo")

page.get_by_title("Close window").click()
```

## 20. What is get_by_test_id()?

**Answer:**

get_by_test_id() identifies elements using a dedicated test attribute such as data-testid.

It is useful when accessible locators are not suitable or when we need stable automation-specific identifiers.

**HTML:**

```html
<button data-testid="login-button">Login</button>
```

**Python:**

```python
page.get_by_test_id("login-button").click()
```

## 21. What is set_test_id_attribute()?

**Answer:**

set_test_id_attribute() is used to configure a custom attribute for test ID locators.

By default, Playwright uses data-testid. If our application uses a different attribute, such as data-cy, we can configure it.

**Example:**

```python
p.selectors.set_test_id_attribute("data-cy")

page.get_by_test_id("login-button").click()
```

# CSS SELECTORS AND XPATH

## 22. What are CSS selectors? Give examples.

**Answer:**

CSS selectors are used to identify HTML elements based on tag names, IDs, classes, attributes, and relationships between elements.

**Examples:**

```python
# Tag
page.locator("input")

# ID
page.locator("#username")

# Class
page.locator(".login-button")

# Attribute
page.locator('[type="submit"]')

# Attribute starts with
page.locator('[id^="user"]')

# Attribute ends with
page.locator('[id$="name"]')

# Attribute contains
page.locator('[class*="error"]')

# Descendant
page.locator("form input")

# Direct child
page.locator("ul > li")

# Adjacent sibling
page.locator("h2 + p")

# Following sibling
page.locator("h2 ~ p")

# Nth child
page.locator("li:nth-child(2)")

# Not selector
page.locator("button:not(.disabled)")

# Has selector
page.locator("div:has(button)")
```

## 23. What is the difference between CSS and XPath?

**Answer:**

CSS selectors are generally simpler and more readable for locating elements using IDs, classes, and attributes.

XPath is useful when we need complex DOM traversal, such as locating parent, child, following sibling, or preceding sibling elements.

**Comparison:**

- CSS uses CSS selector syntax.
- XPath uses XML path expressions.
- CSS supports open Shadow DOM piercing in Playwright.
- XPath does not pierce Shadow DOM boundaries.
- XPath supports parent and sibling navigation.

## 24. How do you handle XPath in Playwright?

**Answer:**

I use XPath when CSS selectors or user-facing locators are not sufficient, especially for complex DOM relationships.

**Examples:**

```python
# By ID
page.locator("//input[@id='username']")

# By text
page.locator("//button[text()='Login']")

# Parent
page.locator("//input[@id='email']/parent::div")

# Following sibling
page.locator("//td[text()='John']/following-sibling::td[1]")

# Preceding sibling
page.locator("//td[text()='Email']/preceding-sibling::td")
```

## 25. What is Locator Chaining?

**Answer:**

Locator chaining means identifying a parent element first and then locating its child element within that parent.

It helps avoid ambiguity when multiple elements have the same name.

**Example:**

```python
page.locator("#admin-login").get_by_role(
    "button", name="Login"
).click()
```

## 26. Why do we need to refine locators?

**Answer:**

We refine locators when multiple elements match the same locator.

Refining helps us identify the exact element, avoid strict mode violations, and improve test reliability.

**Example:**

```python
page.locator(".product").filter(
    has_text="Samsung"
).get_by_role(
    "button", name="Add to Cart"
).click()
```

# LOCATOR REFINEMENT AND STRICT MODE

## 27. What is the difference between filter(has_text=...) and filter(has=...)?

**Answer:**

has_text filters elements based on their text content, whereas has filters elements based on the presence of a matching child locator.

**Using has_text:**

```python
page.locator(".product").filter(
    has_text="Samsung"
)
```

**Using has:**

```python
page.locator(".product").filter(
    has=page.get_by_role(
        "button", name="Add to Cart"
    )
)
```

## 28. What is the difference between nth(), first, and last?

**Answer:**

These methods select a specific element when multiple elements match the same locator.

nth() selects an element based on its zero-based index, first selects the first matching element, and last selects the last matching element.

**Example:**

```python
# First element
page.locator("button").first.click()

# Second element
page.locator("button").nth(1).click()

# Last element
page.locator("button").last.click()
```

## 29. What is the difference between Locator and ElementHandle?

**Answer:**

A Locator is a lazy way of identifying elements. It resolves the element when an action or assertion is performed and re-resolves it against the current DOM.

ElementHandle represents a specific DOM element reference. It does not automatically re-resolve if the DOM changes.

I prefer Locator for regular automation because it supports auto-waiting and retryability.

**Example:**

```python
# Locator
username = page.locator("#username")

# ElementHandle
username_handle = page.query_selector("#username")
```

## 30. Why are Playwright locators called lazy?

**Answer:**

Locators are called lazy because Playwright does not immediately resolve the element when the locator is created.

It resolves the element when we perform an action or assertion. This helps handle dynamically changing DOM elements.

**Example:**

```python
username = page.locator("#username")

# Element is resolved here
username.fill("Janardhan")
```

## 31. What is Strict Mode in Playwright?

**Answer:**

Strict mode ensures that a locator used for a single-element action matches exactly one element.

If multiple elements match, Playwright throws a strict mode violation error.

**Example:**

```python
page.get_by_role(
    "button", name="Login"
).click()
```

If two Login buttons exist, it throws a strict mode violation.

**How do you resolve it?**

```python
page.locator("#admin-login").get_by_role(
    "button", name="Login"
).click()
```

We can also use filter() or nth() when appropriate.

# ADVANCED LOCATOR SCENARIOS

## 32. How do you handle dynamic elements in Playwright?

**Answer:**

Dynamic elements are elements that appear, disappear, or change based on user interactions or application responses.

I handle them using Playwright's auto-waiting, locator assertions, and explicit waits when necessary.

**Example:**

```python
page.get_by_role(
    "button", name="Load More"
).click()

expect(
    page.get_by_text("Product 11")
).to_be_visible()
```

## 33. What is Shadow DOM? How do you handle it in Playwright?

**Answer:**

Shadow DOM is used in web components to encapsulate their internal HTML structure and styles.

Playwright supports locating elements inside open Shadow DOM using regular CSS and role-based locators. Closed Shadow DOM internals cannot be directly accessed using normal Playwright locators.

**Example:**

```python
page.locator(
    "user-login #username"
).fill("Janardhan")
```

## 34. How do you handle duplicate elements?

**Answer:**

When multiple elements have the same text, role, or locator, I refine the locator using parent-child relationships, filter(), has_text, has, or positional methods like nth().

I prefer meaningful locators over positional selection whenever possible.

**Example:**

```python
samsung = page.locator(".product").filter(
    has_text="Samsung"
)

samsung.get_by_role(
    "button", name="Add to Cart"
).click()
```

## 35. What are the best practices for writing Playwright locators?

**Answer:**

My locator best practices are:

1. Prefer get_by_role() when accessible role and name are available.
2. Use get_by_label() for properly labelled form fields.
3. Prefer stable test IDs when necessary.
4. Avoid unnecessary XPath.
5. Avoid hardcoded positional locators.
6. Use locator chaining to handle duplicate elements.
7. Avoid unnecessary time.sleep().
8. Validate locators with assertions.

## 36. What is the difference between auto-waiting and explicit waiting?

**Answer:**

Auto-waiting is a built-in Playwright feature that waits for elements to meet the required actionability conditions before performing actions.

Explicit waiting means we manually wait for a particular condition or state using methods such as wait_for() or locator assertions.

**Auto-waiting example:**

```python
page.get_by_role(
    "button", name="Login"
).click()
```

**Explicit waiting example:**

```python
page.locator("#loading").wait_for(
    state="hidden"
)
```

**Assertion example:**

```python
expect(
    page.locator("#success")
).to_be_visible()
```

# REAL-TIME SCENARIO-BASED QUESTIONS

## 37. Your locator matches three buttons. How do you click only the required button?

**Answer:**

First, I identify why multiple elements are matching. Then I refine the locator using a unique parent element or filter(). If the element position is stable and known, I can use nth().

**Example:**

```python
page.locator("#registration-form").get_by_role(
    "button", name="Submit"
).click()
```

## 38. An element is visible, but Playwright is unable to click it. What will you do?

**Answer:**

First, I check whether the element is visible, enabled, stable, and receiving pointer events.

Then I check whether another element is overlapping it or whether an animation is in progress.

I inspect the locator and use appropriate waits or fix the application condition before clicking.

**Example:**

```python
button = page.get_by_role(
    "button", name="Submit"
)

expect(button).to_be_visible()
expect(button).to_be_enabled()

button.click()
```

## 39. Your test passes locally but fails in Jenkins. How will you debug it?

**Answer:**

First, I check the failure logs, browser configuration, and execution environment.

Then I inspect screenshots and traces to understand where the failure occurred.

I also check timing issues, test data, environment variables, and browser dependencies.

Finally, I reproduce the issue locally using the same configuration.

## 40. How do you debug a locator that is not identifying an element?

**Answer:**

First, I inspect the element in browser developer tools.

Then I verify the locator, check whether the element is inside an iframe or Shadow DOM, and confirm that the element is available in the current page.

I can also use Playwright Inspector to inspect and test the locator.

**Example:**

```python
page.pause()
```

## 41. How do you ensure your locators are stable and maintainable?

**Answer:**

I prefer user-facing locators such as get_by_role() and get_by_label().

When those are not suitable, I use stable attributes or test IDs.

I avoid dynamic CSS classes, long XPath expressions, and unnecessary positional locators.

I also validate uniqueness and use locator chaining when duplicate elements exist.
