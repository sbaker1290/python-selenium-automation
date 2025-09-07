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


driver.get('https://stackoverflow.com/users/signup')

# Find Create your account text
driver.find_element(By.CSS_SELECTOR,'.flex--item.fs-headline1' )

# find text under create your account
driver.find_element(By.CSS_SELECTOR,'.flex--item.js-terms')

# Email input field
driver.find_element(By.ID, 'email')

# Password input field
driver.find_element(By.ID, 'password')

# Find the eye
driver.find_element(By.CSS_SELECTOR,'.ps-absolute.iconEyeOffSm')

# Sign up button
driver.find_element(By.ID, 'submit-button')

# Sign up with Google button
driver.find_element(By.CSS_SELECTOR,'.flex--item.s-btn__google')

# Sign up with GitHub button
driver.find_element(By.CSS_SELECTOR,'.flex--item.s-btn__github')

# Get stack overflow terms
driver.find_element(By.XPATH, "//a[contains(@href,'stackoverflow.com/teams?')]")
