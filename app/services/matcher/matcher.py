from .normalizer import ProductNormalizer
from .scorer import ProductScorer


class ProductMatcher:

    @classmethod
    def find_best_match(cls, invoice_name: str, products):

        invoice_name = ProductNormalizer.normalize(invoice_name)

        best_product = None
        best_score = -999

        for product in products:

            sheet_name = ProductNormalizer.normalize(
                str(product.get("Name", ""))
            )

            score = ProductScorer.score(
                invoice_name,
                sheet_name
            )

            if score > best_score:
                best_score = score
                best_product = product

        return best_product, best_score