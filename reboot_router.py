from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
driver.get("http://192.168.31.1/cgi-bin/luci/web")
password=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[1]/span/input')
password.send_keys("your admin password")
nextbtn=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/form/div[2]/a")
nextbtn.click()
sleep(5)
dropdown=driver.find_element_by_xpath('//*[@id="sysmenu"]')
dropdown.click()
sleep(2)
rebootbtn=driver.find_element_by_xpath('//*[@id="toReboot"]')
rebootbtn.click()
sleep(2)
rebootrouter=driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div/button/span")
rebootrouter.click()
sleep(2)
oktbn=driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/a[1]/span")
oktbn.click()
sleep(2)
driver.close()
