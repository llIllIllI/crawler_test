from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

ch_options = webdriver.ChromeOptions()
ch_options.add_argument('headless')
ch_options.add_argument('disable-gpu')
ch_options.add_argument('window-size=1920x1680')

driver = webdriver.Chrome('./chromedriver', options=ch_options)
driver.implicitly_wait(3)

driver.get("https://etk.srail.co.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000")

def changeAttributeValue (attr_name, attr_value):
	try:
		elem = driver.find_element_by_name(attr_name)
		prvValue = elem.get_attribute('value')
		elem.clear()
		elem.send_keys(attr_value)
		elem.send_keys(Keys.RETURN)
		print ("Changed " + prvValue + " to " + elem.get_attribute('value'))
		driver.implicitly_wait(1)
	except NoSuchElementException:
		print("Cannot find element " + attr_name)
		
		
changeAttributeValue('dptRsStnCdNm', "신경주")
changeAttributeValue('arvRsStnCdNm', "동탄")
changeAttributeValue('dptDt', "20181216")
changeAttributeValue('dptTm', "120000")

driver.save_screenshot('./test.png')
print("Quit")
driver.quit()