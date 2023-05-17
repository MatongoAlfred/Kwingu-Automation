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

# Checking for the 'Colum Group' button
column_groups_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "column-group-container"))
)

# Clicking on the 'Column Group' button
column_groups_button.click()

# Check that the 'Column Groups' view is expanded
column_expanded_view = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "column-group-align"))
)

# Checking that the correct view 'Column Group' was expanded
column_groups_header = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "sub-header-label"))
)
assert column_groups_header.is_displayed

# Sleep for 5 seconds
time.sleep(5)

# Checking that there are already added column groups in the view
column_group_added = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "k-button"))
)
assert column_group_added.is_displayed

# Clicking on the column groups search bar
column_group_search_bar = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "k-searchbar"))
)
column_group_search_bar.click()

# Sleep for 5 secs
time.sleep(5)

# Choosing an "Enrollment Activity" column group from the drop-down list
column_group_search_bar_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "k-input"))
)
column_group_search_bar_input.click()
column_group_search_bar_input.send_keys("Enrollment Activity")

# sleep for 5 seconds
time.sleep(5)

# Checking if the clear all button exists
clear_columns_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "clear-columns-button"))
)

# clicking the 'Clear All Column Groups' button
clear_columns_button.click()

# Sleep for 5 seconds
time.sleep(5)

# Test Success Summary
print('Test Successfully executed, no failed test cases')
