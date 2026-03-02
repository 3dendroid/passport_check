import datetime


class Base:
    """Init driver class"""
    def __init__(self, driver):
        self.driver = driver

    """Method current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("CURRENT URL: " + get_url)

    """Method assert word"""
    @staticmethod
    def assert_word(word, result):
        value_word = word.text
        assert value_word == result
        print("GOOD VALUE WORD")

    """Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        path = 'C:\\Users\\SUPERDEN\\PycharmProjects\\free_reward_claimer\\screenshots\\'
        name_screenshot = 'screenshot_' + now_date + '.png'
        self.driver.save_screenshot(path + name_screenshot)
        print("SCREENSHOT SAVED")

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("GOOD VALUE URL")

    """Method refresh"""
    def refresh(self):
        self.driver.refresh()

    """Method to get title of the page"""
    def get_title(self):
        return self.driver.title
