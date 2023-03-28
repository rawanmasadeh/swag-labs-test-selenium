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

#view description of backpack
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[1]/div[3]/div[2]/a/div").click()

time.sleep(3)

#back to cart
driver.find_element("id", "back-to-products").click()
time.sleep(3)

