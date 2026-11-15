from playwright.sync_api import Locator, Page


class ProductsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.heading: Locator = page.get_by_text("Products", exact=True)

    def product_title(self, name: str) -> Locator:
        return self.page.get_by_text(name, exact=True)
