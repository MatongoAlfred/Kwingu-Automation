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

# Find and select 'Users' module from the main menu navigation
users_module_select = driver.find_element(By.XPATH,
                                          "//body/app-root/app-header/header/section/section/div/div/ul/li[4]/div/span/i")
users_module_select.click()

# Sleep for 5 secs
time.sleep(5)

# select user management option
user_management = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-header/header/section/section/div/div/ul/li[4]/div[2]/li[1]")
    ))
user_management.click()

# sleep for 3 seconds
time.sleep(3)

# clicking on the data export icon
data_export_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-entity-list/div/kendo-grid/kendo-grid-toolbar/div/button[2]"))
)
data_export_icon.click()

# sleep for 5 seconds
time.sleep(5)

# checking if the 'Cancel' button is working as expected
cancel_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-entity-list/div/app-export-grid/kendo-dialog/div[2]/kendo-dialog-actions/button[1]"))
)
cancel_button.click()

# sleep for 3 seconds
time.sleep(3)

# checking if the save button is working as expected
data_export_icon.click()
save_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-entity-list/div/app-export-grid/kendo-dialog/div[2]/kendo-dialog-actions/button[2]"))
)
save_button.click()

# sleep for 3 seconds
time.sleep(3)

# Assert that the test case is passed
print("Test Case Executed Successfully!!!")
