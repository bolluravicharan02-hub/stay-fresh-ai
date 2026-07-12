from app.services.gemini.extractor import InvoiceExtractor
from app.services.barcode.google_sheet_service import GoogleSheetService
from app.schemas import InvoiceSchema
from app.services.database_service import DatabaseService


class InvoiceProcessor:

    def __init__(self):

        self.extractor = InvoiceExtractor()
        self.sheet = GoogleSheetService()
        self.database = DatabaseService()

    def process(self, file_path: str) -> InvoiceSchema:

        # Extract JSON from Gemini
        data = self.extractor.extract(file_path)

        # Convert JSON -> InvoiceSchema
        invoice = InvoiceSchema(**data)

        # Search products in Google Sheet
        for item in invoice.items:

            result = self.sheet.search(item.product_name)

            if result:

                item.barcode = result["barcode"]
                item.purchase_price = result["purchase_price"]
                item.selling_price = result["selling_price"]
                item.mrp = result["mrp"]
                item.confidence = result["confidence"]
                item.barcode_source = "google_sheet"

            else:

                item.barcode = None
                item.confidence = 0.0
                item.barcode_source = "not_found"

        db_invoice = self.database.save_invoice(
            file_path.split("/")[-1],
            invoice
        )

        return db_invoice.id, invoice