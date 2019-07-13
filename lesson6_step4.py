from selenium import webdriver
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))


link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input = browser.find_element_by_id("answer")	
input.send_keys(y)

checkbox = browser.find_element_by_css_selector('input[type="checkbox"]')
checkbox.click()

browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)

radiobutton = browser.find_element_by_css_selector('input[id="robotsRule"]')	
radiobutton.click()


button = browser.find_element_by_css_selector("button.btn")
button.click()	