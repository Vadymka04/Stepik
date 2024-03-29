from selenium import webdriver
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

box = browser.find_element_by_css_selector("img")
boxFindA = box.get_attribute("valuex")

x = boxFindA
y = calc(x)	

input = browser.find_element_by_id("answer")	
input.send_keys(y)

checkbox = browser.find_element_by_css_selector('input[type="checkbox"]')
checkbox.click()

radiobutton = browser.find_element_by_css_selector('input[id="robotsRule"]')	
radiobutton.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()	