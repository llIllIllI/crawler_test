from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ch_options = webdriver.ChromeOptions()
#ch_options.add_argument('headless')
#ch_options.add_argument('disable-gpu')
#ch_options.add_argument('window-size=1920x1680')

driver = webdriver.Chrome('./chromedriver', options=ch_options)
driver.implicitly_wait(3)

driver.get("https://etk.srail.co.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000")

def changeAttributeNameValue (attr_name, attr_value, clear, submit):
	try:
		elem = driver.find_element_by_name(attr_name)
		prvValue = elem.get_attribute('value')
		if(clear):
			elem.clear()
		elem.send_keys(attr_value)
		print ("Changed " + prvValue + " to " + elem.get_attribute('value'))
		if(submit):
			elem.submit()
	except NoSuchElementException:
		print("Cannot find element " + attr_name)
		
def changeAttributeOptionValue (attr_name, attr_value):
		elem = driver.find_element_by_name(attr_name)
		for option in elem.find_elements_by_tag_name('option'):
			if option.text != attr_value:
				print (option.text + ", Go Down")
				ARROW_DOWN = u'\ue015'
				elem.send_keys(ARROW_DOWN)
			else:
				ENTER = u'\ue007'
				elem.send_keys(ENTER)
				break

changeAttributeNameValue('dptRsStnCdNm', "신경주", 1, 0)
changeAttributeNameValue('arvRsStnCdNm', "동탄", 1, 0)
changeAttributeOptionValue('psgInfoPerPrnb1', "어른 2명")
changeAttributeOptionValue('dptDt', "2018/12/16(일)")
changeAttributeNameValue('dptTm', "120000", 0, 1)

driver.implicitly_wait(3)
driver.save_screenshot('./test.png')
print("Quit")
#driver.quit()