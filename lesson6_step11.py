from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome(
        executable_path='C:/Users/chromedriver.exe')
    browser.get(link)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//div[@class='first_block']//input[@class='form-control second']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("form-control.third")
    input3.send_keys("Smolensk")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()



