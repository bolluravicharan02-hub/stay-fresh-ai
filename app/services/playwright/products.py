from playwright.sync_api import Page, expect

from app.schemas import InvoiceSchema, InvoiceItemSchema
from app.utils.logger import app_logger


class ProductService:

    def add_products(
        self,
        page: Page,
        invoice: InvoiceSchema
    ):

        app_logger.info(f"Adding {len(invoice.items)} products...")

        for index, item in enumerate(invoice.items):

            app_logger.info(
                f"Adding Product {index + 1}: {item.product_name}"
            )

            self.search_product(page, item.barcode)

            self.fill_quantity(
                page,
                index,
                item
            )

            self.fill_purchase_price(
                page,
                index,
                item
            )

            self.fill_selling_price(
                page,
                index,
                item
            )

        app_logger.success("All Products Added Successfully.")

    ####################################################################

    def search_product(
        self,
        page: Page,
        barcode: str
    ):

        app_logger.info(
            f"Searching Barcode: {barcode}"
        )

        barcode_box = page.locator("#searchItemBarcode")

        expect(barcode_box).to_be_visible(timeout=10000)

        barcode_box.click()

        barcode_box.fill("")

        barcode_box.fill(barcode)

        page.wait_for_timeout(500)

        page.keyboard.press("Enter")

        page.wait_for_timeout(1500)

        app_logger.success("Product Selected.")

    ####################################################################

    def fill_quantity(
        self,
        page: Page,
        row: int,
        item: InvoiceItemSchema
    ):

        qty_box = page.locator(
            f'input[name="purchaseItemVos[{row}].qty"]'
        )

        expect(qty_box).to_be_visible(timeout=5000)

        qty_box.click()

        qty_box.fill(str(item.quantity))

        page.wait_for_timeout(300)

    ####################################################################

    def fill_purchase_price(
        self,
        page: Page,
        row: int,
        item: InvoiceItemSchema
    ):

        price_box = page.locator(
            f"#price{row}"
        )

        expect(price_box).to_be_visible(timeout=5000)

        price_box.click()

        price_box.fill(str(item.purchase_price))

        page.wait_for_timeout(300)

    ####################################################################

    def fill_selling_price(
        self,
        page: Page,
        row: int,
        item: InvoiceItemSchema
    ):

        selling_box = page.locator(
            f"#sellingPrice{row}"
        )

        expect(selling_box).to_be_visible(timeout=5000)

        selling_box.click()

        selling_box.fill(str(item.selling_price))

        page.wait_for_timeout(500)