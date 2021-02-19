from selenium import webdriver
import time
import math

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('input_value')
    y = math.log(abs(12*math.sin(int(x.text))))
    zapolnyaem = browser.find_element_by_id('answer')
    zapolnyaem.send_keys(str(y))

    button = browser.find_element_by_class_name("btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()
    option2 = browser.find_element_by_css_selector("[value='robots']")
    option2.click()
    
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()