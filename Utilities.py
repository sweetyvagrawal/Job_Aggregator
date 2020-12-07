import logging
import sys

from selenium import webdriver
from selenium.webdriver import ActionChains


def get_driver() -> webdriver:
    try:
        logging.info("creating chrome driver")
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificates-errors')
        options.add_argument("--test-type")
        driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe", options=options)
        driver.maximize_window()
        driver.implicitly_wait(10)
        logging.info("driver created successfully")

        return driver
    except:
        logging.exception("failed to create driver")
        sys.exit()















