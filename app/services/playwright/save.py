from playwright.sync_api import Page, expect

from app.utils.logger import app_logger
from .selectors import Selectors


class SaveService:

    def save(self, page: Page):

        app_logger.info("Saving Supplier Bill...")

        save_button = page.locator(Selectors.SAVE_BUTTON)

        expect(save_button).to_be_visible(timeout=10000)

        save_button.click()

        page.wait_for_load_state("networkidle")

        app_logger.success("Supplier Bill Saved Successfully.")