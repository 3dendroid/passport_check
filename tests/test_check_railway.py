from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from pages.main_page import MainPage
from utilities.telegram_notifier import send_telegram_message


def create_driver():
    options = Options()

    # 1. Обязательные настройки для Railway
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    # Указываем путь к бинарному файлу Chromium (из вашей ошибки видно, что он там)
    options.binary_location = "/usr/bin/chromium"

    # 2. Маскировка автоматизации
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
    options.add_experimental_option('useAutomationExtension', False)

    # 3. Настройка Service
    # В Railway драйвер обычно лежит по этому пути, если установлен через nixpacks
    service = Service(executable_path="/usr/bin/chromedriver")

    try:
        # Пытаемся запустить с системным драйвером
        driver = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        print(f"Ошибка при поиске драйвера в /usr/bin: {e}")
        # Если не вышло, пробуем запустить без указания пути (Selenium Manager сам найдет)
        driver = webdriver.Chrome(options=options)

    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    })

    return driver

def test_pass_check():
    send_telegram_message("🪪 *Checking passport status, please wait.*")

    driver = create_driver()
    try:
        mp = MainPage(driver)
        status_text, id_text, date_text = mp.check_pass_status()
        send_telegram_message(f"✅️ *Checking completed!*\n"
                              f"🕒 *Documents submitted:* {id_text}\n"
                              f"📆 *Application ID:* {date_text}\n"
                              f"📋 *Passport state:* {status_text}"
                              )
    except Exception as e:
        print(f"Error occurred: {e}")
        send_telegram_message(f"❌ *Error:* {e}")
    finally:
        # Используем quit(), чтобы закрыть все окна и завершить процесс драйвера
        driver.quit()


# Обязательный блок для запуска скрипта
if __name__ == "__main__":
    test_pass_check()
