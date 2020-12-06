import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.support.wait import WebDriverWait

from POM.Job_Portal_Base import JobPortal


class Indeed(JobPortal):
    SEARCH_BUTTON_LOCATOR = (By.XPATH, "//button[contains(@class, 'icl-WhatWhere-button')]")
    LOCATION_INPUT_BOX_LOCATOR = (By.ID, "text-input-where")
    TITLE_INPUT_BOX_LOCATOR = (By.ID, "text-input-what")
    JOB_LIST_LOCATOR = (By.CSS_SELECTOR, "h2[class='title']")

    def __init__(self, driver: webdriver):
        logging.info("creating Indeed class")
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
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
        return self.get_elements(self.JOB_LIST_LOCATOR)

    def apply_job_filters(self) -> webelement:
        pass

    def get_job_details(self, job: webelement):
        logging.info("opening jobs in iteration")
        job.click()

    def get_jobs_next_page(self):
        pass

    def get_job_title(self):
        pass

    def get_job_company_name(self):
        pass

    def get_job_posting_location(self):
        pass

    def get_job_posted_date(self):
        pass

    def get_job_description(self):
        pass

    def open_job(self, job):
        pass

    def close_job(self):
        pass

    def get_job_url(self):
        pass


