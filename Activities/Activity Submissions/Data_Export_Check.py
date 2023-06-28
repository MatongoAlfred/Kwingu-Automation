import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# set up the Chrome web-driver
service_object = Service('C:\\Users\\alfred.matongo_komaz\\PycharmProjects\\Kwingu_Automation\\Browsers\\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

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

# Find and select 'activities' module from the main menu navigation
activities_module_select = driver.find_element(By.XPATH,
                                               "//body/app-root/app-header/header/section/section/div/div/ul/li[5]/div/span")
activities_module_select.click()

# Sleep for 3 secs
time.sleep(3)

# select activities submission option
activities_submission = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-header/header/section/section/div/div/ul/li[5]/div[2]/li[2]/a")
    ))
activities_submission.click()

# waiting for the activities submission table to load
time.sleep(5)

# Checking if the data export icon exists
data_export = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/div/button[3]/img"))
)
data_export.click()

# sleep for 3 secs
time.sleep(3)

# Checking the export data confirmation pop up is displayed
export_pop_up = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-activity-list/app-export-grid/kendo-dialog/div[2]/kendo-dialog-titlebar/div[1]"))
)
assert export_pop_up.is_displayed()

# checking if the 'Cancel' button is working as expected
cancel_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-activity-list/app-export-grid/kendo-dialog/div[2]/kendo-dialog-actions/button[1]"))
)
cancel_button.click()

# sleep for 3 secs
time.sleep(3)

# checking if the 'Save' button is available and working as expected
data_export.click()

# sleep for 3 seconds
time.sleep(3)

# Clicking the save button
save_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-activity-list/app-export-grid/kendo-dialog/div[2]/kendo-dialog-actions/button[2]"))
)
save_button.click()

# sleep for 3 secs
time.sleep(3)

# checking that the data export has begun
export_begun = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, "//body/app-root/app-activity-list/app-export-grid/kendo-dialog/div[2]/div/p"), "Preparing the CSV file for download...")
)
# Check if the element has the expected text
if export_begun:
    print("Test Case passed successfully")
else:
    print("Test case working as expected but the text is not available")
