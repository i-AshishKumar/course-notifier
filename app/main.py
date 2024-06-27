from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options 
from selenium.common.exceptions import NoSuchElementException

import time

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
email_sender = 'xxxxx@gmail.com'
email_receiver = 'xxxxx@gmail.com'
email_password = 'xxxxx'
smtp_server = 'smtp.gmail.com'
smtp_port = 587



options = Options()
options.add_argument('--headless')

driver = webdriver.Firefox(options=options)
driver.maximize_window()
driver.get("https://self-service.dal.ca/BannerExtensibility/customPage/page/dal.stuweb_academicTimetable")
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='pbid-termSelectDetailcontainer-2']/div[@id='pbid-termCheckbox-container-2']/div[@class='xe-container']/span")))
driver.execute_script("arguments[0].click();", element)

dropdown = "//div[@id='s2id_pbid-subjectCode']"
element=WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,dropdown)))
element.location_once_scrolled_into_view
element.click()

search_field = driver.find_element(By.XPATH, "//div[@id='select2-drop']/div[@class='select2-search']/input")
search_field.send_keys('csci')

search_result = driver.find_element(By.XPATH, "//div[@id='select2-drop']/ul[@class='select2-results']/li/div")
search_result.click()

time.sleep(8)

xpath_pagination ="//div[@id='pbid-queryTablePageSize-container']/select/option[@value='string:9999']"
pagination = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, xpath_pagination)))
pagination.location_once_scrolled_into_view
pagination.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='pbid-timetable-container']/span/table/tbody/tr[@valign]/td/b")))

isCourseFound = True

while isCourseFound:
    try:
        # Locate the desired text '5408' within the course title element
        desired_course = "5411"
        course_title_xpath = "//div[@id='pbid-timetable-container']/span/table/tbody/tr[@valign]/td/b[contains(text(),'"+desired_course+"')]"
        course_title_element = driver.find_element(By.XPATH, course_title_xpath)

        # Print the text content of the element
        print(course_title_element.get_attribute('innerHTML'))
        course = course_title_element.get_attribute('innerHTML')

        # Send email notification
        subject = 'Desired Course Found: ' + desired_course
        body = f'The desired course "{course}" has been found.'
        
        msg = MIMEMultipart()
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, msg.as_string())
        server.quit()
        isCourseFound = False


    except NoSuchElementException as e:
        subject = 'Desired Course Not Found: ' + desired_course
        body = f'The desired course was not found.'
        
        msg = MIMEMultipart()
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, msg.as_string())
        server.quit()
        break