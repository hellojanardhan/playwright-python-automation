from playwright.sync_api import Page, expect


def test_dynamic_table_rows_and_columns(page: Page) -> None:
    page.goto("https://www.playwrightautomation.com/practice.html")
    table = page.locator("#dynamic-table")
    expect(table).to_be_visible()
    rows = table.locator("tbody tr")
    expect(rows).to_have_count(5)
    columns = table.locator("thead tr th")
    expect(columns).to_have_count(6)
    header_names = [name.strip() for name in columns.all_text_contents()]
    assert "Club" in header_names

    for club_name in ("Manchester City", "Liverpool", "Barcelona", "Real Madrid"):
        expect(rows.filter(has_text=club_name)).to_have_count(1)

    bayern_row = rows.filter(has_text="Bayern Munich")
    expect(bayern_row).to_have_count(1)
    club_column = header_names.index("Club")
    expect(bayern_row.locator("td").nth(club_column)).to_have_text("Bayern Munich")

