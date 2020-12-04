import logging

from selenium import webdriver
from selenium.webdriver.common.by import By

from POM.Job_Portal_Base import JobPortal


class Monster (JobPortal):
    SEARCH_BUTTON_LOCATOR = (By.ID, "doQuickSearch2")
    LOCATION_INPUT_BOX_LOCATOR = (By.ID, "where2")
    TITLE_INPUT_BOX_LOCATOR = (By.ID, 'q2')
    JOB_LIST_LOCATOR = (By.XPATH, "//div[contains(@class,'title-container')]")

    def __init__(self, driver: webdriver):
        logging.info("creating monster class")
        self.driver = driver
        logging.info("Monster site opening")
        self.driver.get("https://www.monster.com//")

    def get_job_search_button(self):
        logging.info("getting monster search button")
        return self.get_element(self.SEARCH_BUTTON_LOCATOR)

    def get_job_location_input_box(self):
        logging.info("getting monster job location box ")
        return self.get_element(self.LOCATION_INPUT_BOX_LOCATOR)

    def get_job_title_input_box(self):
        logging.info("getting monster job title box")
        return self.get_element(self.TITLE_INPUT_BOX_LOCATOR)

    def get_job_list(self):
        logging.info("getting monster job list")
        pass


