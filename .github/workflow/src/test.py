from seleniumbase import BaseCase
import os

BaseCase.main(__name__, __file__)  # Call pytest

PASSWORD = os.getenv("PASSWORD")


class MyTestClass(BaseCase):
    def test_swag_labs(self):
        self.open("https://prenotami.esteri.it")
        self.type("#login-email", "shojibmdalamgir@gmail.com")
        self.type("#login-password", PASSWORD)
        self.click("button.button.primary.g-recaptcha")
        self.click("a#advanced")  # Using the CSS selector to click on the <a> element
        self.click(
            'a[href="/Services/Booking/1133"] button.button.primary'
        )  # Click on the button inside the <a> element

    def tearDown(self):
        # Override tearDown to prevent browser from closing
        pass
