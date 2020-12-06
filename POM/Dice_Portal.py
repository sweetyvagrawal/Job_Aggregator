import logging
import re
import time
from datetime import datetime
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote import webelement
from POM.Job_Portal_Base import JobPortal


class Dice(JobPortal):
    SEARCH_BUTTON_LOCATOR = (By.ID, "submitSearch-button")
    LOCATION_INPUT_BOX_LOCATOR = (By.ID, "google-location-search")
    TITLE_INPUT_BOX_LOCATOR = (By.CSS_SELECTOR, "div [data-cy='typeahead-input']")
    JOB_LIST_LOCATOR = (By.XPATH, "//div[contains(@class,'title-container')]/div/h5/a")

    def __init__(self, driver: webdriver):
        logging.info("creating dice class")
        self.driver = driver
        logging.info("dice site opening")
        self.driver.get("https://www.dice.com/")
        self.action_chain = ActionChains(driver)

    def get_job_search_button(self):
        logging.info("getting dice search button")
        return self.get_element(self.SEARCH_BUTTON_LOCATOR)

    def get_job_location_input_box(self):
        logging.info("getting dice job location box ")
        return self.get_element(self.LOCATION_INPUT_BOX_LOCATOR)

    def get_job_title_input_box(self):
        logging.info("getting dice job title box")
        return self.get_element(self.TITLE_INPUT_BOX_LOCATOR)

    def get_job_list(self):
        logging.info("creating list of dice search job title")
        time.sleep(2)
        return self.get_elements(self.JOB_LIST_LOCATOR)

    def close_job(self):
        logging.info("closing new window")
        self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])

    def open_job(self, job):
        logging.info("opening job in new tab")
        job.send_keys(Keys.CONTROL, Keys.RETURN)
        #time.sleep(2)
        self.driver.switch_to_window(self.driver.window_handles[1])

    def get_job_title(self):
        try:
            logging.info("getting job title")
            return self.get_element((By.CSS_SELECTOR, "h1[id='jt']")).text
        except:
            return ""

    def get_job_company_name(self):
        try:
            logging.info("getting job company name")
            return self.get_element((By.CSS_SELECTOR, "[id='hiringOrganizationName']")).text
        except:
            return ""

    def get_job_posting_location(self):
        try:
            logging.info("getting job location ")
            return self.get_element((By.CSS_SELECTOR, "[class='location']")).text
        except:
            return ""

    def get_job_posted_date(self):
        try:
            logging.info("getting job posting date")
            return self.get_element((By.CSS_SELECTOR, "li[class='posted '] span")).text
        except:
            return ""

    def get_job_description(self):
        try:
            logging.info("getting job description")
            return self.get_element((By.CSS_SELECTOR, "[id='jobdescSec']")).text
        except:
            return ""

    def get_job_url(self):
        try:
            logging.info("getting job company url")
            return self.driver.current_url
        except:
            logging.exception(" error in fetching job url")
            return ""

    def apply_job_filters(self):
        logging.info("get all the jobs posted today")
        self.get_element((By.XPATH, "//button[text()=' Today ']")).click()
        self.get_element((By.XPATH, "//li/span[contains(text(), 'Exclude Remote')]")).click()

    def get_jobs_next_page(self):
        logging.info("getting next page button ")
        next_page_links = self.get_elements((By.XPATH, "//ul[@class='pagination']/li"))
        next_page_link = next_page_links[-1]
        logging.info("checking next button is disable or not")
        if "disabled" in next_page_link.get_attribute("class"):
            logging.info("next button is disabled as next page is unavailable")
            return []
        logging.info("clicking the next button")
        next_page_link.click()
        return self.get_job_list()




















