import re


class ProductNormalizer:

    REPLACEMENTS = {
        "FAB": "FABRIC",
        "CON": "CONDITIONER",
        "COND": "CONDITIONER",
        "PKT": "PACKET",
        "PCH": "POUCH",
        "GM": "G",
        "GRAMS": "G",
        "GRAM": "G",
        "KGS": "KG",
        "LTR": "L",
        "LTRS": "L"
    }

    @classmethod
    def normalize(cls, text: str) -> str:

        text = text.upper()

        for old, new in cls.REPLACEMENTS.items():
            text = re.sub(rf"\b{old}\b", new, text)

        text = re.sub(r"[^A-Z0-9 ]", " ", text)
        text = re.sub(r"\s+", " ", text)

        return text.strip()