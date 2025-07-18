from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import pytest


@pytest.fixture(scope="module")
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
    return driver

# Login the page
@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce")])
@pytest.mark.order(1)
@pytest.mark.dependency(name="login")
def test_login(driver, username, password):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url


# Sorting to ["a-z","low-high","high-low"]
@pytest.mark.parametrize("sort_type", ["az", "lohi", "hilo"])
@pytest.mark.order(2)
@pytest.mark.dependency(depends=["login"])
def test_sort_products(driver, sort_type):
    sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    sort_dropdown.select_by_value(sort_type)  # "az","lohi", "hilo"
    time.sleep(2)

#add to cart
@pytest.mark.order(3)
@pytest.mark.dependency(depends=["login"])
def test_add_to_cart(driver):
    time.sleep(2)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()


# Add to specific product
@pytest.mark.parametrize("product_name", [
     "Sauce Labs Bolt T-Shirt"])
@pytest.mark.order(4)
@pytest.mark.dependency(depends=["login"])
def test_add_specific_product_to_cart(driver, product_name ):
    xpath = f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
    driver.find_element(By.XPATH, xpath).click()
    print(f"Added: {product_name}")
    time.sleep(2)

#Add_to_multiple_items
@pytest.mark.parametrize("product_ID", [
    "add-to-cart-sauce-labs-backpack",
    "add-to-cart-sauce-labs-bolt-t-shirt"
])
@pytest.mark.order(5)
@pytest.mark.dependency(depends=["login"])
def test_add_multiple_products(driver, product_ID):
    driver.find_element(By.ID, product_ID).click()
    print(f"Added: {product_ID}")
    time.sleep(1)

# Go to cart page
@pytest.mark.order(6)
@pytest.mark.dependency(depends=["login"])
def test_go_to_cart(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(2)

#Remove the one item
@pytest.mark.parametrize("remove_button_ID", [
    "remove-sauce-labs-bolt-t-shirt"
])
@pytest.mark.order(7)
@pytest.mark.dependency(depends=["login"])
def test_remove_items_from_cart(driver, remove_button_ID):
    driver.find_element(By.ID, remove_button_ID).click()
    print(f"Removed: {remove_button_ID}")
    time.sleep(2)

# Click checkout button
@pytest.mark.order(8)
@pytest.mark.dependency(depends=["login"])
def test_checkout(driver):
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Simi")
    driver.find_element(By.ID, "last-name").send_keys("Chakma")
    driver.find_element(By.ID, "postal-code").send_keys("124simichakma")
    driver.find_element(By.ID, "continue").click()
    assert "checkout-step-two" in driver.current_url

# Logout
@pytest.mark.order(9)
@pytest.mark.dependency(depends=["login"])
def test_logout(driver):
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    driver.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(1)
    assert "saucedemo" in driver.current_url
