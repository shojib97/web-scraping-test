import os
from seleniumbase import SB

PASSWORD = os.getenv("PASSWORD")

with SB(uc=True, test=True, locale_code="en") as sb:
    url = "https://prenotami.esteri.it"
    sb.activate_cdp_mode(url)
    sb.open(url)
    sb.type("#login-email", "shojibmdalamgir@gmail.com")
    sb.type("#login-password", PASSWORD)
    sb.uc_gui_click_captcha()
    sb.click("button.button.primary.g-recaptcha")
    sb.click("a#advanced")
    sb.click('a[href="/Services/Booking/1133"] button.button.primary')