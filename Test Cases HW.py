from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


# Test Case

# open the url
driver.get('https://www.target.com/')

# click on Account
driver.find_element(By.ID, 'account-sign-in').click()
sleep(5)

# click on sign in button
driver.find_element(By.XPATH, "//button[text()='Sign in or create account']").click()
sleep(5)

# verify "Sign in or create account" text is shown
actual_text = driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text
expected_text = 'Sign in or create account'
assert expected_text in actual_text
print('Test Case Pass')

# verify SignIn button id shown
driver.find_element(By.XPATH, "//button[text()='Sign in with passkey']")

driver.quit()