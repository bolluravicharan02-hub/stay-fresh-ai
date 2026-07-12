import json
from pathlib import Path

from google import genai
from google.genai import types

from app.config import settings
from app.utils.logger import app_logger


class InvoiceExtractor:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GOOGLE_API_KEY
        )

        prompt_path = (
            Path(__file__).parents[2]
            / "prompts"
            / "extraction_prompt.txt"
        )

        self.prompt = prompt_path.read_text(
            encoding="utf-8"
        )

    def extract(
        self,
        file_path: str
    ) -> dict:

        app_logger.info(
            f"Extracting Invoice : {file_path}"
        )

        uploaded_file = self.client.files.upload(
            file=file_path
        )

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                uploaded_file,
                self.prompt
            ],
            config=types.GenerateContentConfig(
                temperature=0,
                response_mime_type="application/json"
            )
        )

        data = json.loads(response.text)

        app_logger.success(
            "Invoice Extracted Successfully."
        )

        return data