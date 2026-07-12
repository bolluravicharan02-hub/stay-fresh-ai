from app.schemas import InvoiceSchema
from app.utils.logger import app_logger

from .browser import BrowserManager
from .login import LoginService
from .purchase import PurchaseService
from .supplier import SupplierService
from .products import ProductService
from .save import SaveService


class PlaywrightService:

    def __init__(self):

        self.browser = BrowserManager()

        self.login_service = LoginService()

        self.purchase_service = PurchaseService()

        self.supplier_service = SupplierService()

        self.product_service = ProductService()

        self.save_service = SaveService()

    def sync_invoice(
        self,
        invoice: InvoiceSchema
    ) -> bool:

        page = None

        try:

            app_logger.info("=" * 60)
            app_logger.info("STARTING VASYERP AUTOMATION")
            app_logger.info("=" * 60)

            # --------------------------------
            # Launch Browser
            # --------------------------------
            page = self.browser.start()

            # --------------------------------
            # Login
            # --------------------------------
            self.login_service.login(page)

            # --------------------------------
            # Purchase → Supplier Bills
            # --------------------------------
            self.purchase_service.open_supplier_bills(page)

            # --------------------------------
            # Create New Supplier Bill
            # --------------------------------
            self.purchase_service.create_new_bill(page)

            # --------------------------------
            # Select Supplier
            # --------------------------------
            self.supplier_service.select_supplier(
                page,
                invoice
            )

            # --------------------------------
            # Add Products
            # --------------------------------
            self.product_service.add_products(
                page,
                invoice
            )

            # --------------------------------
            # Save
            # --------------------------------
            self.save_service.save(page)

            app_logger.success(
                "ERP Synchronization Completed Successfully."
            )

            return True

        except Exception as e:

            app_logger.exception(e)

            if page:

                page.screenshot(
                    path="logs/error.png",
                    full_page=True
                )

            return False

        finally:

            self.browser.stop()