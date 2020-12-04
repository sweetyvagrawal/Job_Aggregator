import datetime
import logging
import sys
import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

from POM.Dice_Portal import Dice
from POM.Indeed_portal import Indeed
from POM.Job_Portal_Base import JobPortal
from POM.Monster_Portal import Monster
import Utilities

if len(sys.argv) < 4:
    print("please provide 4 arg. for eg: main.py Dice|Indeed|monster <Job Title> <Job Location>")
    sys.exit()

logging.basicConfig(filename="scrapper-" + datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + ".log",
                    format='%(asctime)s %(name)s - %(levelname)s - %(funcName)s- %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

logging.info("trying to create Driver")
driver = Utilities.get_driver()


def get_job_portal(portal_name: str, driver: webdriver) -> JobPortal:
    if portal_name.lower() == "dice":
        logging.info("creating dice portal")
        return Dice(driver)
    elif portal_name.lower() == "monster":
        logging.info("creating monster portal")
        return Monster(driver)
    elif portal_name.lower() == "indeed":
        logging.info("creating indeed portal")
        return Indeed(driver)
    else:
        print(" please provide portal name. for eg: dice|monster|Indeed")
        sys.exit()



try:
    portal = sys.argv[1]
    job_title = sys.argv[2]
    job_location = sys.argv[3]

    # concept of Polymorphism-> same like my conftest fundas(Travolook)
    job_portal = get_job_portal(portal, driver)

    job_title_input_box = job_portal.get_job_title_input_box()
    job_title_input_box.clear()
    logging.info("sending job title " + "\"" +job_title + "\"")
    job_title_input_box.send_keys(job_title)
    job_location_input_box = job_portal.get_job_location_input_box()
    job_location_input_box.send_keys(Keys.CONTROL, "a", Keys.DELETE)
    logging.info("sending job location " + "\"" + job_location + "\"")
    job_location_input_box.send_keys(job_location)
    job_portal.get_job_search_button().click()
    logging.info("getting all jobs link in variable")
    job_list = job_portal.get_job_list()
    logging.info("looping through all the jobs")
    for job in job_list:
        logging.info("getting job details")
        job_portal.get_job_details(job)

except:
    logging.exception("error occured during performing job search ")

finally:
    time.sleep(8)
    driver.quit()






