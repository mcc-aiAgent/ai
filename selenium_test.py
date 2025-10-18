from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.save_screenshot("baidu.jpg")
print(driver.page_source)
