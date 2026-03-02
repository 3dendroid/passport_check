from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


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