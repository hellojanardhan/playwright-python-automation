import calendar as calendar_module

from playwright.sync_api import Page, expect


def select_date(page: Page, date: str, month: str, year: str) -> None:
    current_month = page.locator(".ui-datepicker-month")
    current_year = page.locator(".ui-datepicker-year")

    target = (int(year), list(calendar_module.month_name).index(month))
    for _ in range(120):
        current = (
            int(current_year.inner_text()),
            list(calendar_module.month_name).index(current_month.inner_text()),
        )
        if current == target:
            break
        navigation = page.locator(
            ".ui-datepicker-next" if current < target else ".ui-datepicker-prev"
        )
        navigation.click()
    else:
        raise AssertionError(f"Unable to navigate to {month} {year}")

    calendar_grid = page.locator(".ui-datepicker-calendar")
    month_index = target[1] - 1
    date_link = calendar_grid.locator(
        f'td[data-month="{month_index}"][data-year="{year}"] '
        f'a[data-date="{date}"]'
    )
    expect(date_link).to_be_visible()
    date_link.click()


def test_select_date(page: Page) -> None:
    page.goto("https://testautomationpractice.blogspot.com/")
    date_input = page.locator("#datepicker")
    date_input.click()

    select_date(page, "11", "December", "2026")

    expect(date_input).to_have_value("12/11/2026")




