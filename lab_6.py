from selenium import webdriver
import time
import re



driver = webdriver.Firefox()
driver.get("https://prom.ua/ua")
assert "Prom" in driver.title

input_form= driver.find_element_by_name('search_term')
input_form.send_keys("панама")
content = driver.find_element_by_class_name('searchForm__button--2PLbd')
content.find_element_by_xpath("./button").click()
assert ("No results found" not in driver.page_source) and ("Результатов не найдено" not in driver.page_source)

time.sleep(5)

assert driver.current_url == "https://prom.ua/ua/search?search_term=%D0%BF%D0%B0%D0%BD%D0%B0%D0%BC%D0%B0"

header = driver.find_element_by_xpath("//div[@class=\"basePage__content--3L2HZ\"]/div[@class=\"ek-body__section\"]/div/h1").text
assert "панам" in header

box = driver.find_elements_by_xpath("//div[@class=\"style__expandable--1phVS\"]/div/span")

for i in range(25):
	text1 = box[i].text.lower()
	assert "панам" in text1 



driver.close()
