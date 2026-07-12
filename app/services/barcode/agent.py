import json
from pathlib import Path

from google import genai
from google.genai import types

from app.config import settings
from app.utils.logger import app_logger


class BarcodeAgent:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GOOGLE_API_KEY
        )

        prompt_path = (
            Path(__file__).parent
            / "prompt.txt"
        )

        self.prompt = prompt_path.read_text(
            encoding="utf-8"
        )

    def search(
        self,
        product_name: str
    ) -> dict:

        app_logger.info(
            f"Searching Barcode : {product_name}"
        )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                self.prompt,
                product_name
            ],
            config=types.GenerateContentConfig(
                temperature=0,
                response_mime_type="application/json"
            )
        )

        data = json.loads(response.text)

        app_logger.success(
            f"Barcode Found : {data}"
        )

        return data