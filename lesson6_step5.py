from selenium import webdriver
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector('input[name = "firstname"]')
input1.send_keys("Имя")

input2 = browser.find_element_by_css_selector('input[name = "lastname"]')
input2.send_keys("Фамилия")

input3 = browser.find_element_by_css_selector('input[name = "email"]')
input3.send_keys("mail")

FileButton = browser.find_element_by_id("file")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
FileButton.send_keys(file_path)

print(file_path)


button = browser.find_element_by_css_selector("button.btn")
button.click()	