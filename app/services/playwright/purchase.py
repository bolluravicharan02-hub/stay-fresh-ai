from playwright.sync_api import Page

from app.utils.logger import app_logger


class PurchaseService:

    def open_supplier_bills(self, page: Page):

        app_logger.info("Opening Purchase Menu...")

        # Click Purchase menu
        page.get_by_role(
            "link",
            name="Icon Purchase"
        ).click()

        page.wait_for_timeout(1000)

        app_logger.info("Opening Supplier Bills...")

        page.get_by_role(
            "link",
            name="Supplier Bills"
        ).click()

        page.wait_for_load_state("networkidle")

        app_logger.success(
            "Supplier Bills Opened Successfully."
        )

    def create_new_bill(self, page: Page):

        app_logger.info("Opening Create New...")

        page.get_by_role(
            "link",
            name="Create New"
        ).click()

        page.wait_for_load_state("networkidle")

        app_logger.success(
            "Supplier Bill Page Opened."
        )