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




#2.SauceDemo Automation with PyTest + Selenium
This repository contains an automated test suite using Selenium WebDriver and PyTest to test the SauceDemo e-commerce demo site.

The script uses @pytest.fixture for setup/teardown and @pytest.mark.dependency to manage execution flow.

📌 Features
✅ Login to SauceDemo

✅ Sort products (commented in current version)

✅ Add specific or multiple items to the cart

✅ Navigate and remove items from the cart

✅ Complete checkout with customer info

✅ Validate payment summary page

✅ Logout functionality

✅ Structured with pytest and selenium

🛠️ Tech Stack
1.Python 3.x
2.Selenium WebDriver
3.ChromeDriver
4.PyTest

📦 Setup Instructions
✅ 1. Install Python dependencies
pip install selenium pytest pytest-dependency
✅ 2. Install ChromeDriver
Download the ChromeDriver version matching your browser and add it to your PATH.

🚀 How to Run
pytest test_saucedemo.py

🔄 Test Flow (via @pytest.mark.dependency):
1. Open browser (incognito via @pytest.fixture)
2. Login
3. Add product to cart
4. Go to cart
5. Checkout
6. Fill customer info
7. Confirm payment summary
8. (Logout - optional)
Commented-out functions (sort_products, add_specific_product_to_cart, etc.) can be uncommented for extended flows.

🧪 Sample Credentials:
Username: standard_user
Password: secret_sauce
These are publicly available test credentials from SauceDemo.
