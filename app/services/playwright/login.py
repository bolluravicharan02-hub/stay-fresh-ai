from playwright.sync_api import Page

from app.config import settings
from app.utils.logger import app_logger


class LoginService:

    def login(self, page: Page):

        app_logger.info("Opening Login Page...")

        page.goto(
            f"{settings.VASYERP_URL}/login"
        )

        # Wait until username textbox appears
        page.get_by_role(
            "textbox",
            name="Username"
        ).wait_for(timeout=30000)

        app_logger.info("Entering Username...")

        page.get_by_role(
            "textbox",
            name="Username"
        ).fill(settings.VASYERP_USERNAME)

        app_logger.info("Entering Password...")

        page.get_by_role(
            "textbox",
            name="Password"
        ).fill(settings.VASYERP_PASSWORD)

        app_logger.info("Clicking Login...")

        app_logger.info("Submitting Login...")

        page.get_by_role(
            "textbox",
            name="Password"
        ).press("Enter")

        page.wait_for_url(
            "**/dashboard",
            timeout=30000
        )

        app_logger.success("Login Successful")