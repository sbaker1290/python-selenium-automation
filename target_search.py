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

driver.find_element(By.ID, 'search').send_keys('tea')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(5)

actual_search_text = driver.find_element(By.XPATH,"//div[@data-test='lp-resultsCount']").text
expected_search_text = 'tea'
assert expected_search_text in actual_search_text, f'Error, Expected text{expected_search_text}'
print('Test case passed')