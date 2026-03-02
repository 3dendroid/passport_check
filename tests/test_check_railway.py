from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from pages.main_page import MainPage
from utilities.telegram_notifier import send_telegram_message


def create_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    # Railway Path (Nixpacks)
    options.binary_location = "/usr/bin/chromium"

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)

    try:
        driver = webdriver.Chrome(options=options)
    except:
        service = Service(executable_path="/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=options)

    return driver


def test_pass_check():
    driver = None
    try:
        driver = create_driver()
        mp = MainPage(driver)
        status_text, id_text, date_text = mp.check_pass_status()

        # Send message in telegram
        send_telegram_message(
            f"✅️ *Checking completed!*\n"
            f"🕒 *Documents submitted:* {id_text}\n"
            f"📆 *Application ID:* {date_text}\n"
            f"📋 *Passport state:* {status_text}"
        )
    except Exception:
        pass
    finally:
        if driver:
            driver.quit()


if __name__ == "__main__":
    test_pass_check()