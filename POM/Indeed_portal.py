import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from POM.Job_Portal_Base import JobPortal


class Indeed(JobPortal):

    SEARCH_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'icl-WhatWhere-button')]")
    LOCATION_INPUT_BOX_LOCATOR = (By.ID, "-input-where")
    TITLE_INPUT_BOX_LOCATOR = (By.ID, "text-input-what")
    JOB_LIST_LOCATOR = (By.XPATH, "//div[contains(@class,'title-container')]")

    def __init__(self, driver: webdriver):
        logging.info("creating Indeed class")
        self.driver = driver
        logging.info("Indeed site opening")
        self.driver.get("https://www.indeed.com/")

    def get_job_search_button(self):
        logging.info("getting indeed search button")
        return self.get_element(self.SEARCH_BUTTON_LOCATOR)

    def get_job_location_input_box(self):
        logging.info("getting indeed job location box ")
        return self.get_element(self.LOCATION_INPUT_BOX_LOCATOR)

    def get_job_title_input_box(self):
        logging.info("getting Indeed job title box")
        return self.get_element(self.TITLE_INPUT_BOX_LOCATOR)

    def get_job_list(self):
        logging.info("getting indeed job list")
        pass



