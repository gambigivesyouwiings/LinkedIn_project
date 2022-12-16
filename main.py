from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import time

path = 'C:/development/chromedriver.exe'
USER_EMAIL = 'Your Email address'
USER_PASSWORD = 'Your password'

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.implicitly_wait(20)
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3395378127&f_AL=true&f_C=%5B%5D&f_E=%5B%5D&f_EA=%5B%5D&f_F=%5B%5D&f_I=%5B%5D&f_JIYN=%5B%5D&f_JT=%5B%5D&f_PP=%5B%5D&f_T=%5B%5D&f_WT=%5B%5D&keywords=python%20developer&sortBy=R')
sign_in = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()

email_username = driver.find_element(By.XPATH, '//*[@id="username"]')
email_username.send_keys(USER_EMAIL, Keys.ENTER)

email_password = driver.find_element(By.XPATH, '//*[@id="password"]')
email_password.send_keys(USER_PASSWORD, Keys.ENTER)

time.sleep(20)
job_list = driver.find_elements(By.CSS_SELECTOR, '.job-card-container__link')
list_of_roles = []
for job in job_list:
    try:
        job.click()
        list_of_roles.append(job.text)
        item = driver.find_element(By.CSS_SELECTOR, '.jobs-save-button')
        item.click()
    except ElementClickInterceptedException:
        print('not clickable')
    except NoSuchElementException:
        print("That job seems to be filled")
        continue
#
# print(list_of_roles)
# driver.quit()
# company = driver.find_element(By.XPATH, '//*[@id="ember4739"]')
