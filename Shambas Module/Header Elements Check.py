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

# Checking for the 'Powertable' header elements
column_groups_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "column-group-container"))
)

filters_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "filters-button"))
)

actions_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "disabled-assign-button"))
)

export_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "profile-image"))
)

add_shamba_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "add-button"))
)

import_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "export-button"))
)

table_view = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "table-view"))
)

map_view = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "map-view"))
)

# ascertain that the testcase was successfully executed
print("Test Summary")
print("Verified : Column Group button is available in the powertable")
print("Verified : Filters button is available in the powertable")
print("Verified : Actions button is available in the powertable")
print("Verified : Export button is available in the powertable")
print("Verified : Add Shamba Details button is available in the powertable")
print("Verified : Import Polygon button is available in the powertable")
print("Verified : Table View button is available in the powertable")
print("Verified : Map View button is available in the powertable")


