from rapidfuzz import fuzz

from .extractor import ProductExtractor


class ProductScorer:

    @classmethod
    def score(cls, invoice_name: str, sheet_name: str) -> float:

        invoice = ProductExtractor.extract(invoice_name)
        sheet = ProductExtractor.extract(sheet_name)

        # Base fuzzy score
        score = fuzz.token_sort_ratio(
            invoice_name,
            sheet_name
        )

        # ----------------------------
        # Size Matching
        # ----------------------------
        if (
            invoice["size"] is not None and
            sheet["size"] is not None
        ):

            if invoice["size"] == sheet["size"]:
                score += 30
            else:
                score -= 40

        # ----------------------------
        # Unit Matching
        # ----------------------------
        if (
            invoice["unit"] and
            sheet["unit"]
        ):

            if invoice["unit"] == sheet["unit"]:
                score += 10
            else:
                score -= 20

        # ----------------------------
        # Color Matching
        # ----------------------------
        if (
            invoice["color"] and
            sheet["color"]
        ):

            if invoice["color"] == sheet["color"]:
                score += 10
            else:
                score -= 20

        return score