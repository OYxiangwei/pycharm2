from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
url = "http://www.baidu.com"
driver.get(url)
print(driver.title)
text = driver.find_element_by_id('wrapper').text
print(text)
driver.save_screenshot('6.4_12.png')
driver.find_element_by_id('kw').send_keys(u'龙')
driver.find_element_by_id('su').click()
time.sleep(5)
driver.save_screenshot("v6.4白.png")
print(driver.get_cookies())
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
driver.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
driver.find_element_by_id('kw').send_keys('dnf')
driver.find_element_by_id('su').send_keys(Keys.RETURN)
driver.save_screenshot('v4er.png')
driver.find_element_by_id('kw').clear()
driver.quit()