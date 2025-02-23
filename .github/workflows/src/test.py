import os
from seleniumbase import SB

PASSWORD = os.getenv("PASSWORD")

with SB(uc=True, test=True, locale_code="en") as sb:
    url = "https://prenotami.esteri.it"
    sb.activate_cdp_mode(url)
    sb.cdp.open(url)
    sb.cdp.type("#login-email", "shojibmdalamgir@gmail.com")
    sb.cdp.type("#login-password", PASSWORD)
    sb.cdp.click("button.button.primary.g-recaptcha")
    sb.cdp.click("a#advanced")
    sb.cdp.click('a[href="/Services/Booking/1133"] button.button.primary')
    sb.sleep(5)