from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.main_page import MainPage
from utilities.telegram_notifier import send_telegram_message


def create_driver():
    options = Options()

    # --- Settings for servers ---
    options.add_argument("--headless=new")  # headless
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    # Hidden automation
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)

    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--incognito")

    options.page_load_strategy = 'eager'

    # Service and Driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
              get: () => undefined
            })
          """
    })

    return driver


def test_pass_check():
    send_telegram_message("🪪 *Checking passport status, please wait.*")

    driver = None
    try:
        driver = create_driver()
        mp = MainPage(driver)
        status_text, id_text, date_text = mp.check_pass_status()

        send_telegram_message(
            f"✅️ *Checking completed!*\n"
            f"🕒 *Documents submitted:* {id_text}\n"
            f"📆 *Application ID:* {date_text}\n"
            f"📋 *Passport state:* {status_text}"
        )
    except Exception as e:
        print(f"Error occurred: {e}")
        send_telegram_message(f"❌ *Error:* {str(e)[:400]}")  # restricted the lines of errors
    finally:
        if driver:
            driver.quit()


if __name__ == "__main__":
    test_pass_check()
