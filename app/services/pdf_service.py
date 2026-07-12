from pathlib import Path

import fitz  # PyMuPDF

from app.utils.logger import app_logger


class PDFService:

    @staticmethod
    def convert_to_images(pdf_path: str) -> list[str]:
        """
        Convert every page of a PDF into PNG images.

        Returns:
            List of image paths.
        """

        app_logger.info(f"Converting PDF: {pdf_path}")

        pdf = fitz.open(pdf_path)

        image_paths = []

        output_folder = (
            Path(pdf_path).parent
            / Path(pdf_path).stem
        )

        output_folder.mkdir(
            exist_ok=True
        )

        for page_number in range(len(pdf)):

            page = pdf.load_page(page_number)

            pix = page.get_pixmap(
                dpi=300
            )

            image_path = (
                output_folder
                / f"page_{page_number + 1}.png"
            )

            pix.save(str(image_path))

            image_paths.append(
                str(image_path)
            )

        pdf.close()

        app_logger.success(
            f"Converted {len(image_paths)} page(s)"
        )

        return image_paths