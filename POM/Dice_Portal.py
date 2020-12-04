import logging
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
    JOB_LIST_LOCATOR = (By.XPATH, "//div[contains(@class,'title-container')]")

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
        logging.info("getting dice job list")
        return self.get_elements(self.JOB_LIST_LOCATOR)

    def get_job_details(self, job: webelement):
        job_link_ele = job.find_element_by_xpath("div/a")

        job_link = job_link_ele.get_attribute("href")
        self.driver.execute_script("window.open('" + job_link + "');")
        print(job_link)

