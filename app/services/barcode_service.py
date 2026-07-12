from app.schemas import InvoiceSchema
from app.utils.logger import app_logger


class BarcodeService:

    def __init__(self):
        pass

    def search_barcode(self, product_name: str) -> str | None:
        """
        Search barcode for a single product.

        TODO:
        Replace this placeholder implementation with:
        - Google Search
        - GS1 Database
        - Product APIs
        - Internal barcode database

        Returns:
            Barcode string or None
        """

        app_logger.info(
            f"Searching barcode for: {product_name}"
        )

        # Placeholder
        return None

    def enrich_invoice(
        self,
        invoice: InvoiceSchema
    ) -> InvoiceSchema:
        """
        Add barcodes to every product in the invoice.
        """

        app_logger.info(
            "Starting barcode enrichment..."
        )

        for item in invoice.items:

            barcode = self.search_barcode(
                item.product_name
            )

            item.barcode = barcode

        app_logger.success(
            "Barcode enrichment completed."
        )

        return invoice