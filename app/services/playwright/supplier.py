from playwright.sync_api import Page, expect

from app.schemas import InvoiceSchema
from app.utils.logger import app_logger


class SupplierService:

    def select_supplier(
        self,
        page: Page,
        invoice: InvoiceSchema
    ):

        supplier = invoice.supplier_name.strip()

        app_logger.info(f"Selecting Supplier: {supplier}")

        # Open supplier search
        supplier_box = page.locator("input[type='search']").nth(2)

        supplier_box.click()
        supplier_box.fill("")
        supplier_box.fill(supplier)

        # Wait for dropdown
        page.wait_for_timeout(1000)

        # Click exact supplier from dropdown
        supplier_option = page.get_by_role(
            "treeitem",
            name=supplier,
            exact=True
        )

        expect(supplier_option).to_be_visible(timeout=5000)

        supplier_option.click()

        app_logger.success("Supplier Selected Successfully.")