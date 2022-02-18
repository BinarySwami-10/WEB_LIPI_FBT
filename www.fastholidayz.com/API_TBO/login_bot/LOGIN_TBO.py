import modulex as mx
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("disable-infobars")
# options.add_argument('headless')


def login(entity):
	driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options)
	driver.get(entity['url'])
	typeuserid = WebDriverWait(driver, 5).until(
		EC.presence_of_element_located((By.ID, 'LoginName'))).send_keys(entity['username'])
	typepassword = WebDriverWait(driver, 5).until(
		EC.presence_of_element_located((By.ID, 'Password'))).send_keys(entity['password'])
	presslogin = driver.find_element_by_id('Button1').click()
	time.sleep(10000)


if __name__ == '__main__':
	tbodetails = mx.jload('./credentials_portals.json')[0]
	login(tbodetails)

	# print('success')
	# myElem.click()
