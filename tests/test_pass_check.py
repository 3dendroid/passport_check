import os
import uuid

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from pages.main_page import MainPage
from utilities.telegram_notifier import send_telegram_message


def create_driver():
    """CREATE DRIVER FOR LOCAL OR RAILWAY ENVIRONMENT"""
    run_env = (os.getenv("RUN_ENV") or "").lower()

    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-extensions")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--password-store=basic")
    options.add_argument("--enable-automation")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-web-security")
    options.add_argument("--incognito")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.page_load_strategy = 'eager'

    unique_dir = None

    if run_env == "railway":
        unique_dir = f"/tmp/chrome_user_data_{uuid.uuid4().hex}"

        options.add_argument(f"--user-data-dir={unique_dir}")

        options.add_argument("--headless=new")

        driver = webdriver.Chrome(
            service=Service("/usr/local/bin/chromedriver"),
            options=options
        )
    else:
        driver = webdriver.Chrome(service=Service(), options=options)

    driver._temp_user_data_dir = unique_dir
    return driver


def test_pass_check():
    send_telegram_message(f"🚀 *Checking status...*")

    driver = create_driver()

    mp = MainPage(driver)
    mp.check_pass_status()

    send_telegram_message(f"✅ *Checking completed!*")

    driver.close()
