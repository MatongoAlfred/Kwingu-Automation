import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome webdriver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# navigate to the Kwingu login page
driver.get("https://uatkwingu.komaza.com/login")

# wait for the username and password fields to load
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Your username']"))
)
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Your password']"))
)

# enter the login credentials
username_field.send_keys("32752214")
password_field.send_keys("Alfredmat12#")

# tab the Sign_In button
submit_button = driver.find_element(By.XPATH, "//button[@class='login-button']")
submit_button.click()

# wait for the FOPs_dashboard to load
dashboard_header = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[@class='module-header']")))

# sleep for 5 secs
time.sleep(5)

# check that we are on the dashboard page
assert dashboard_header.is_displayed

# check that the FOPs_dashboard page has the 'Hamburger Menu' icon
hamburger_menu_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "menu-bar-close"))
)

# Clicking on the 'Hamburger Menu" icon
hamburger_menu_icon.click()

# Sleep for 5 secs
time.sleep(5)

# Find and select 'Shambas' module from the main menu navigation
shamba_module_select = driver.find_element(By.XPATH, '//*[@id="menu-navigation"]/ul[1]/li[2]')
shamba_module_select.click()

# Sleep for 5 secs
time.sleep(20)

# Wait for the 'Shamba Powertable' to load
powertable_header = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "module-header")))

# Check that we are on the 'Shamba Powertable' page
assert powertable_header.is_displayed

# Checking for the 'Filters' button
filters_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "filters-button"))
)

# Clicking on the 'Filters' button
filters_button.click()

# Sleep for 5 secs
time.sleep(5)

# Check that the 'Filters' view is expanded
filters_expanded_view = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "filter-box"))
)

# Checking that the correct view 'Filter Box' was expanded
filter_header = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "sub-header-label"))
)
assert filter_header.is_displayed

# Sleep for 5 seconds
time.sleep(5)

# Checking and clicking on the 'Add Filter' button
add_filter_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "k-button-icontext"))
)
add_filter_button.click()

# Sleep for 5 seconds
time.sleep(5)

# Search for a column you want to filter
filter_column = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search a column']"))
)

filter_column.click()
filter_column.send_keys("Shamba KCode")

# Sleep for 3 seconds
time.sleep(3)

# wait for the list to be visible and select shamba KCode from the list options
wait = WebDriverWait(driver, 10)
list_element = wait.until(EC.visibility_of_element_located((By.ID, "column-list")))
item_xpath = "//*[@id='column-list']/li[1]/label[1]"
item_element = list_element.find_element(By.XPATH, item_xpath)
item_element.click()

# sleep for 5 seconds
time.sleep(5)

# clicking on the filter box text field and typing in the 'KCode' we wish to filter
enter_kcode = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "k-textbox"))
)
enter_kcode.click()
enter_kcode.send_keys("kwl-2023-0120")

# sleep for 5 seconds
time.sleep(5)

# searching and clicking on the 'Filter' button
filter_button_click = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "k-primary")))

filter_button_click.click()

# sleep for 5 seconds
time.sleep(5)

# searching and clicking on the 'Clear All Filters' button
# Checking if the 'Clear All' button exists
clear_filters_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "clear-filters-button"))
)

# clicking the 'Clear All Filters' button
clear_filters_button.click()

# Sleep for 5 seconds
time.sleep(5)

# Test Success Summary
print('Test Successfully executed, no failed test cases')

# sleep for 5 seconds
time.sleep(10)
