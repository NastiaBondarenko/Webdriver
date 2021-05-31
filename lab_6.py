from selenium import webdriver
import time
import re

# Create webdriver instance

def startDriver(link):
	driver = webdriver.Firefox()
	driver.get(link)	
	return driver

#check the title of the site

def CheckSite(NameWebsite, driver):
	assert NameWebsite in driver.title

# search for a relevant query

def searhWorld(world, driver):
	input_form= driver.find_element_by_name('search_term')
	input_form.send_keys(world)
	content = driver.find_element_by_class_name('searchForm__button--2PLbd')
	content.find_element_by_xpath("./button").click()
	assert ("No results found" not in driver.page_source) and ("Результатов не найдено" not in driver.page_source)

#check if the page matches the search page

def GoToPage( driver):
	assert "https://prom.ua/ua/search?search_term=" in driver.current_url

#check if the title contains our request

def headerIsRight(world, driver):
	header = driver.find_element_by_xpath("//div[@class=\"basePage__content--3L2HZ\"]/div[@class=\"ek-body__section\"]/div/h1").text
	assert world in header

#check whether the first 10 elements contain the name of the searched element

def CheckBox(world, driver):
	box = driver.find_elements_by_xpath("//div[@class=\"style__expandable--1phVS\"]/div/span")
	newWorld = world[:len(world)-1]
	for i in range(10):
		text1 = box[i].text.lower()
		assert newWorld in text1 

#sequential execution of all code

def main(link, nameWebsite, world):
	driver = startDriver(link)
	CheckSite(nameWebsite, driver)
	searhWorld(world, driver)
	time.sleep(5)
	GoToPage(driver)
	headerIsRight(world, driver)
	CheckBox(world, driver)
	time.sleep(5)
	driver.close()

main("https://prom.ua/ua", "Prom",  "панама")