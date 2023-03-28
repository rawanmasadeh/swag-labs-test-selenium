from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#Open the website
driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
#Maximize thw window
driver.maximize_window()
#Asserting the the title of the wesite is correct
assert "Swag Labs" in driver.title

#Testing Standard Login
username = "standard_user"
password ="secret_sauce"

driver.find_element("id", "user-name").send_keys(username)
driver.find_element("id", "password").send_keys(password)
driver.find_element("id", "login-button").click()
time.sleep(3)

#Testing adding to cart
driver.find_element("id", "add-to-cart-sauce-labs-backpack").click()
time.sleep(3)
driver.find_element("id", "add-to-cart-test.allthethings()-t-shirt-(red)").click()
time.sleep(3)

#view cart
driver.find_element("id", "shopping_cart_container").click()
time.sleep(3)

#checkout no last name
driver.find_element("id", "checkout").click()
driver.find_element("id", "first-name").send_keys("john")
driver.find_element("id", "last-name")
driver.find_element("id", "postal-code").send_keys("0000")
time.sleep(3)
driver.find_element("id", "continue").click()
time.sleep(3)
driver.find_element(By.XPATH,"//*[contains(text(), 'Error')]")


driver.find_element("id", "react-burger-menu-btn").click()
time.sleep(3)

#Logout

driver.find_element("id", "logout_sidebar_link").click()
time.sleep(3)


driver.close()

print ("test completed successfully")