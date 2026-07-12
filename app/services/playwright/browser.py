from playwright.sync_api import sync_playwright

from app.utils.logger import app_logger


class BrowserManager:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start(self):

        app_logger.info("Launching Browser...")

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=False,
            slow_mo=500
        )

        self.context = self.browser.new_context(
            viewport={
                "width": 1600,
                "height": 900
            }
        )

        self.page = self.context.new_page()

        self.page.set_default_timeout(30000)

        app_logger.success("Browser Started.")

        return self.page

    def stop(self):

        app_logger.info("Closing Browser...")

        if self.context:
            self.context.close()

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()

        app_logger.success("Browser Closed.")