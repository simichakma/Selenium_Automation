import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--incognito")
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    yield driver
    driver.quit()

#login_saucedemo
def login_with_attribute(driver, username, password):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

# Login using short XPath
def login_with_xpath(driver, username, password):
    driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@id='login-button']").click()

#sorting_products: A-Z, High-Low, Low-High
def sort_products(driver, sort_type):
    dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    dropdown.select_by_value(sort_type)
    time.sleep(2)

def add_to_cart(driver):
    time.sleep(2)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

#Add_to_specific_product
def add_specific_product_to_cart(driver, product_name):
    xpath = f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
    driver.find_element(By.XPATH, xpath).click()
    print(f"Added: {product_name}")
    time.sleep(2)

#Add_to_multiple_products
def add_multiple_products(driver):
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    time.sleep(2)

def go_to_cart(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

#Remove_to_cart
def remove_products_from_cart(driver):
    driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "remove-sauce-labs-bolt-t-shirt").click()
    time.sleep(2)

def checkout(driver):
    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)

def customer_info(driver, first_name, last_name, postal_code):
    driver.find_element(By.ID, "first-name").send_keys(first_name)
    driver.find_element(By.ID, "last-name").send_keys(last_name)
    driver.find_element(By.ID, "postal-code").send_keys(postal_code)
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

def payment_cart(driver):
    assert driver.find_element(By.CLASS_NAME, "title").text()
    print("Payment_cart page confirmed")
    time.sleep(2)

#Logout
def logout(driver):
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(2)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(2)


 #Pytest Dependency Test Flow:

@pytest.mark.dependency()
def test_full_saucedemo_flow(driver):
    login_with_attribute(driver, "standard_user", "secret_sauce")
    #sort_products(driver, "az")
    #sort_products(driver, "lohi")
    #sort_products(driver, "hilo")
    add_to_cart(driver)
    #add_specific_product_to_cart(driver, "Sauce Labs Bolt T-Shirt")
    #add_multiple_products(driver)
    go_to_cart(driver)
    #remove_products_from_cart(driver)
    checkout(driver)
    customer_info(driver, "simi", "chakma", "124simichakma")
    payment_cart(driver)
    #logout(driver)
