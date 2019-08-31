from selenium import webdriver
import time
k = "https://web.whatsapp.com/"
fox_path = r''
browser = webdriver.Firefox(executable_path=fox_path)
browser.get(k)
time.sleep(10)
elem = browser.find_element_by_xpath('//*[@title="KK"]')
elem.click()
time.sleep(10)
# while true:
for i in range(1):
	elem1 = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
	elem1.send_keys("nice")
	time.sleep(1)
	elem2 = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
	elem2.click()
	time.sleep(3)
# browser.quit()