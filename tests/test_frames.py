from playwright.sync_api import Page, expect


FRAMES_URL = "https://ui.vision/demo/webtest/frames/"


def test_frame_input(page: Page) -> None:
    page.goto(FRAMES_URL)
    frame1 = page.frame_locator('frame[src="frame_1.html"]')
    text_input = frame1.locator("input[name='mytext1']")
    text_input.fill("Hello")
    expect(text_input).to_have_value("Hello")


def test_inner_frames(page: Page) -> None:
    page.goto(FRAMES_URL)
    inner_frame = page.frame_locator(
        'frame[src="frame_3.html"]'
    ).frame_locator("iframe")
    radio = inner_frame.get_by_label("Hi, I am the UI.Vision IDE")
    radio.click()
    expect(radio).to_be_checked()

    checkbox = inner_frame.get_by_label("Form Autofilling")
    checkbox.click()
    expect(checkbox).to_be_checked()

    next_button = inner_frame.get_by_text("Next")
    next_button.click()
    expect(
        inner_frame.get_by_role("progressbar", name="Page 2 of 2")
    ).to_be_visible()

    answer_input = inner_frame.locator(
        "//div[contains(text(),'Your answer')]/preceding::input[1]"
    )
    answer_input.fill("Hey, bro")
    answer_textarea = inner_frame.locator('textarea[aria-label="Your answer"]')
    answer_textarea.fill("Hiii, Hello welcome to india")
    expect(answer_input).to_have_value("Hey, bro")
    expect(answer_textarea).to_have_value("Hiii, Hello welcome to india")

    submit_button = inner_frame.get_by_role("button", name="Submit", exact=True)
    submit_button.click()

