#1.SauceDemo Selenium Login Test!
Python using "Selenium" to automate the login process on SauceDemo. It uses "attribute selectors (ID)" and "XPath" to interact with the webpage.

Requirements:
Python 3.7+
Google Chrome browser

ChromeDriver (compatible with your Chrome version)
Install Dependencies:
pip install selenium
pip install webdriver-manager

🔍 What the Script Does Opens https://www.saucedemo.com/ Logs in with: Username: problem_user Password: secret_sauce Checks if login was successful using attribute & XPath both Prints result in terminal Closes browser after 3 seconds




## 2.  SauceDemo Automation with Pytest & Selenium

This project automates a full shopping flow on [SauceDemo](https://www.saucedemo.com/) using Python, Selenium WebDriver, and Pytest. It includes login, product sorting, cart operations, checkout, and logout — all organized with reusable Pytest features like fixtures, parametrize, and test dependencies.


## 🚀 Technologies Used

- Python 3.8+
- Selenium WebDriver
- Pytest
- ChromeDriver
- Pytest plugins: `pytest-order`, `pytest-dependency`


## 📦 Installation

1. **Clone the repo**  
   git clone https://github.com/your-username/saucedemo-pytest-automation.git
   cd saucedemo-pytest-automation
   
Create virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

| Order | Test Name                           | Description                                        |
| ----- | ----------------------------------- | -------------------------------------------------- |
| 1     | `test_login`                        | Logs into SauceDemo using standard credentials     |
| 2     | `test_sort_products`                | Sorts products by name and price                   |
| 3     | `test_add_to_cart`                  | Adds Sauce Labs Backpack to cart                   |
| 4     | `test_add_specific_product_to_cart` | Adds Sauce Labs Bolt T-Shirt via product name      |
| 5     | `test_add_multiple_products`        | Adds multiple products using parametrize           |
| 6     | `test_go_to_cart`                   | Navigates to the cart page                         |
| 7     | `test_remove_items_from_cart`       | Removes one product from cart                      |
| 8     | `test_checkout`                     | Proceeds with checkout and enters customer details |
| 9     | `test_logout`                       | Logs the user out                                  |
