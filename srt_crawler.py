from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

ch_options = webdriver.ChromeOptions()
ch_options.add_argument('headless')
ch_options.add_argument('disable-gpu')
ch_options.add_argument('window-size=1920x1680')

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
		ARROW_DOWN = u'\ue015'
		ENTER = u'\ue007'
		elem = driver.find_element_by_name(attr_name)
		for option in elem.find_elements_by_tag_name('option'):
			if option.text != attr_value:
				#print (option.text + ", Go Down")
				elem.send_keys(ARROW_DOWN)
			else:
				elem.send_keys(ENTER)
				break

def setUpConditionsforTravel ():
	changeAttributeNameValue('dptRsStnCdNm', "신경주", 1, 0)
	changeAttributeNameValue('arvRsStnCdNm', "동탄", 1, 0)
	changeAttributeOptionValue('psgInfoPerPrnb1', "어른 2명")
	changeAttributeOptionValue('dptDt', "2018/12/29(토)")
	changeAttributeNameValue('dptTm', "120000", 0, 1)

def dumpPageSource () :
	with open('./resultPage.txt', 'w', encoding='utf-8') as text_file:
		text_file.write(driver.page_source)
	text_file.close()

setUpConditionsforTravel ()
driver.implicitly_wait(3)
#dumpPageSource ()

actions = ActionChains(driver)
elem = driver.find_element_by_xpath("//*[@id='result-form']/fieldset/table/tbody/tr[1]/td[6]/a[1]")
#print(elem.get_attribute('text'))
actions.move_to_element(elem).click().perform()

driver.save_screenshot('./test.png')
print("Quit")
driver.quit()