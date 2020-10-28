import csv
from time import sleep
from selenium import webdriver
from parsel import Selector

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('/Users/ffs22/Downloads/chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_class_name
username = driver.find_element_by_id('session_key')

# send_keys() to simulate key strokes
username.send_keys('ffs221@nyu.edu')

# sleep for 0.5 seconds
sleep(0.5)

# locate password form by_class_name
password = driver.find_element_by_id('session_password')

# send_keys() to simulate key strokes
password.send_keys('********')
sleep(0.5)

# locate submit button by_xpath
log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')

# .click() to mimic button click
log_in_button.click()

linkedin_urls=['https://www.linkedin.com/in/ryan-hirani']

for url in linkedin_urls:
    driver.get(url)
    sleep(1)
    sel = Selector(text=driver.page_source)

    name = sel.xpath('//*[starts-with(@class, "inline t-24 t-black t-normal break-words")]/text()').extract_first()
    name = name.strip()

    location = sel.xpath('//*[starts-with(@class, "t-16 t-black t-normal inline-block")]/text()').extract_first()
    location = location.strip()

    job_title = sel.xpath('//*[starts-with(@class, "mt1 t-18 t-black t-normal break-words")]/text()').extract_first()
    job_title = job_title.strip()

    company = sel.xpath('//*[starts-with(@class, "pv-top-card-v2-section__entity-name pv-top-card-v2-section__company-name")]/text()').extract_first()
    company = company.strip()

    #college = sel.xpath('//*[starts-with(@class, "pv-top-card-v2-section__entity-name pv-top-card-v2-section__school-name")]/text()').extract_first()
    #college = college.strip()

    #contact = sel.xpath('//*[starts-with(@class, "pv-top-card-v2-section__entity-name pv-top-card-v2-section__school-name")]/text()').extract_first()
    #contact = contact.strip()

    print('Name: ' + name)
    print('Location: ' + location)
    print('Job Title: ' + job_title)
    print('Company: ' + company)
    #print('College: ' + college)
    #print('Contact: ' + contact)

