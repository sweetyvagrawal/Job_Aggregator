import datetime
import logging
import sys
import time

import psycopg2
from pandas import np
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

from POM.Dice_Portal import Dice
from POM.Indeed_portal import Indeed
from POM.Job_Portal_Base import JobPortal
from POM.Monster_Portal import Monster
import Utilities

if len(sys.argv) < 2:
    print("please provide 2 arg. for eg: main.py Dice|Indeed|monster")
    sys.exit()


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


conn = psycopg2.connect(
    host = 'ec2-50-17-90-177.compute-1.amazonaws.com',
    database = 'dbo53q05khphsq',
    user = 'tjwamztwfeudyf',
    password = '4016af97c725336d823c79afd14e790341ff2b3b6849ea1ed1f3260b2f4fb46b'
)
cur1 = conn.cursor()
cur1.execute('SELECT "job_title" FROM herokudjangoapp_jobs WHERE "job_title" IS NOT NULL')
job_titles = cur1.fetchall()
job_titles = np.fromiter([i[0] for i in job_titles], dtype='<U50')

logging.info("Job titles")
logging.info(job_titles)

cur1.execute('SELECT "job_location" FROM herokudjangoapp_jobs')
job_locations = cur1.fetchall()
job_locations = np.fromiter([i[0] for i in job_locations], dtype='<U50')
logging.info("Job Locations")
logging.info(job_locations)
portal = sys.argv[1]

for job_title in job_titles:
    for job_location in job_locations:

        logging.basicConfig(filename="scrapper-" + datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + ".log",
                            format='%(asctime)s %(name)s - %(levelname)s - %(funcName)s- %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

        logging.info("trying to create Driver")
        driver = Utilities.get_driver()

        try:
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
            job_portal.apply_job_filters()

            logging.info("getting all jobs link in variable")

            job_list = job_portal.get_job_list()
            logging.info("looping through all the jobs")

            while True:
                if len(job_list) == 0:
                    break

                for job in job_list:
                    try:
                        logging.info("getting job details")
                        job_details = job_portal.get_job_details(job)
                        job_details["Searched Job Title"] = job_title
                        job_details["Searched Job Location"] = job_location
                        logging.info("got job details")
                    except:
                        logging.exception("failed to get job details for job: " + job.text)

                job_list = job_portal.get_jobs_next_page()



        except:
            logging.exception("error occured during performing job search ")

        finally:
            time.sleep(1)
            driver.quit()






