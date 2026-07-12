import re


class ProductExtractor:

    SIZE_PATTERN = re.compile(
        r"(\d+(?:\.\d+)?)\s*(ML|L|G|KG)"
    )

    COLORS = [
        "BLUE",
        "GREEN",
        "RED",
        "PINK",
        "WHITE",
        "BLACK",
        "YELLOW",
        "ORANGE"
    ]

    @classmethod
    def extract(cls, text: str):

        text = text.upper()

        result = {
            "size": None,
            "unit": None,
            "color": None
        }

        match = cls.SIZE_PATTERN.search(text)

        if match:
            result["size"] = float(match.group(1))
            result["unit"] = match.group(2)

        for color in cls.COLORS:
            if color in text:
                result["color"] = color
                break

        return result