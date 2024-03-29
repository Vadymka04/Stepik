from selenium import webdriver
import math
import time

def calc(x):
	return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)



x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input = browser.find_element_by_id("answer")	
input.send_keys(y)

checkbox = browser.find_element_by_css_selector('input[type="checkbox"]')
checkbox.click()

radiobutton = browser.find_element_by_css_selector('label[for="robotsRule"]')	
radiobutton.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()