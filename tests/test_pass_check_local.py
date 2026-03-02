from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # Добавили менеджер

from pages.main_page import MainPage
from utilities.telegram_notifier import send_telegram_message


def create_driver():
    options = Options()

    # Основные настройки для обхода детекции автоматизации
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    options.add_argument("--start-maximized")
    options.add_argument("--disable-infobars")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")

    # Опционально: если не хочешь видеть логи в консоли
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Стратегия загрузки (eager загружает DOM, не дожидаясь картинок)
    options.page_load_strategy = 'eager'

    # Автоматическая установка и запуск драйвера
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
