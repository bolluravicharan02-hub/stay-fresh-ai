import gspread

from rapidfuzz import fuzz
from google.oauth2.service_account import Credentials

from app.config import settings
from app.utils.logger import app_logger
from app.services.matcher.matcher import ProductMatcher

class GoogleSheetService:

    def __init__(self):

        app_logger.info("Connecting to Google Sheet...")

        scopes = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = Credentials.from_service_account_file(
            settings.GOOGLE_CREDENTIALS,
            scopes=scopes
        )

        client = gspread.authorize(creds)

        self.sheet = client.open(
            settings.GOOGLE_SHEET_NAME
        ).worksheet("Inventory")

        self.rows = self.sheet.get_all_records()

        app_logger.success(
            f"Loaded {len(self.rows)} products from Google Sheet."
        )

    ##################################################################

    def search(self, product_name: str):

        app_logger.info(
            f"Searching Product: {product_name}"
        )

        product, score = ProductMatcher.find_best_match(
            product_name,
            self.rows
        )

        if product is None:
            return None

        app_logger.success(
            f"Match Found: {product['Name']} ({score:.2f})"
        )

        return {
            "product_name": product["Name"],
            "barcode": str(product["ItemCode"]),
            "purchase_price": float(product.get("Purchase Price", 0)),
            "selling_price": float(product.get("Selling Price", 0)),
            "mrp": float(product.get("Mrp", 0)),
            "confidence": round(min(score, 100) / 100, 2)
        }

        app_logger.warning(
            "No Matching Product Found."
        )

        return None