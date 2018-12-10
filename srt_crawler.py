from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

#driver = webdriver.PhantomJS('./phantomjs')

ch_options = webdriver.ChromeOptions()
ch_options.add_argument('headless')
ch_options.add_argument('disable-gpu')
ch_options.add_argument('window-size=1920x1680')

driver = webdriver.Chrome('./chromedriver', options=ch_options)
driver.implicitly_wait(3)

driver.get("https://etk.srail.co.kr/hpg/hra/01/selectScheduleList.do?pageId=TK0101010000")

try:
	elem = driver.find_element_by_name('dptRsStnCdNm')
	print (elem.get_attribute('value'))
except NoSuchElementException:
	print("Cannot find")

driver.save_screenshot('./test.png')
print("Quit")
driver.quit()