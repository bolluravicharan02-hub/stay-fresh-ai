import json
from pathlib import Path

from google import genai
from google.genai import types
from pydantic import ValidationError

from app.config import settings
from app.prompts import INVOICE_EXTRACTION_PROMPT
from app.schemas import InvoiceSchema
from app.utils.logger import app_logger


class GeminiService:

    def __init__(self):

        self.client = genai.Client(
            api_key=settings.GOOGLE_API_KEY
        )

    def extract_invoice_data(
        self,
        image_paths: list[str]
    ) -> InvoiceSchema:

        app_logger.info(
            "Sending invoice to Gemini..."
        )

        parts = [
            types.Part.from_text(
                text=INVOICE_EXTRACTION_PROMPT
            )
        ]

        for image_path in image_paths:

            path = Path(image_path)

            with open(path, "rb") as f:

                image_bytes = f.read()

            parts.append(
                types.Part.from_bytes(
                    data=image_bytes,
                    mime_type="image/png"
                )
            )

        response = self.client.models.generate_content(
            model="gemini-2.5-pro",
            contents=[
                types.Content(
                    role="user",
                    parts=parts
                )
            ],
            config=types.GenerateContentConfig(
                temperature=0,
                response_mime_type="application/json"
            )
        )

        app_logger.success(
            "Gemini response received."
        )

        try:

            data = json.loads(
                response.text
            )

            invoice = InvoiceSchema.model_validate(
                data
            )

            app_logger.success(
                "Invoice validated successfully."
            )

            return invoice

        except ValidationError as e:

            app_logger.error(e)

            raise Exception(
                "Gemini returned invalid invoice format."
            )

        except json.JSONDecodeError:

            app_logger.error(
                response.text
            )

            raise Exception(
                "Gemini did not return valid JSON."
            )