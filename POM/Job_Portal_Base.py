import logging
from abc import abstractmethod
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.remote import webelement


class JobPortal:
    driver: webdriver = None

    @abstractmethod
    def get_job_title_input_box(self) -> webelement:
        pass

    @abstractmethod
    def get_job_location_input_box(self) -> webelement:
        pass

    @abstractmethod
    def get_job_search_button(self) -> webelement:
        pass

    @abstractmethod
    def get_job_list(self) -> webelement:
        pass

    @abstractmethod
    def get_job_details(self, job: webelement):
        pass

    def get_element(self, locator: ()) -> webelement:
        try:
            logging.info("searching for webelement with \"" + locator[1] + "\"")
            return self.driver.find_element(locator[0], locator[1])
        except:
            filename = "..\\Screenshot\\error-" + datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + ".png"
            logging.exception("failed to get webelement \"" + locator[1] + "\" .screenshot captured at " + filename)
            self.driver.get_screenshot_as_file(filename)
            raise

    def get_elements(self, locator: ()) -> list:
        try:
            logging.info("searching for webelements with \"" + locator[1] + "\"")
            return self.driver.find_elements(locator[0], locator[1])
        except:
            filename = "..\\Screenshot\\error-" + datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + ".png"
            logging.exception("failed to get webelements \"" + locator[1] + "\" .screenshot captured at " + filename)
            self.driver.get_screenshot_as_file(filename)
            raise







