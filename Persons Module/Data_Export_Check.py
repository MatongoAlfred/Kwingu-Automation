import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# sleep for 2 secs
time.sleep(2)

# check that we are on the dashboard page
assert dashboard_header.is_displayed()

# check that the FOPs_dashboard page has the 'Hamburger Menu' icon
hamburger_menu_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "menu-bar-close"))
)

# Clicking on the 'Hamburger Menu" icon
hamburger_menu_icon.click()

# Sleep for 2 secs
time.sleep(2)

# Find and select 'Persons' module from the main menu navigation
shamba_module_select = driver.find_element(By.XPATH, '//*[@id="menu-navigation"]/ul/li[3]')
shamba_module_select.click()

# Sleep for 2 secs
time.sleep(2)

# Wait for the 'Persons Table' to load
persons_header = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "module-header")))

# Check that we are on the 'Persons Table' page
assert persons_header.is_displayed()

# sleep for 2 seconds
time.sleep(2)

# closing the sidebar main navigation menu
hamburger_menu_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "menu-bar-open"))
)
hamburger_menu_icon.click()

# sleep for 5 secs
time.sleep(5)

# Checking and clicking on the 'Export Icon'
export_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "profile-image"))
)
export_button.click()

# sleep for 5 seconds
time.sleep(5)

# Checking if export pop up has been displayed
export_pop_up = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-entity-list/div/app-export-grid/kendo-dialog/div[2]/kendo-dialog-titlebar/div[1]"))
)
assert export_pop_up.is_displayed()

# sleep for 2 seconds
time.sleep(2)

# checking if the cancel icon is visible and working
cancel_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-entity-list/div/app-export-grid/kendo-dialog/div[2]/kendo-dialog-titlebar/div[2]/a")
                                   ))
cancel_icon.click()

# sleep for 5 seconds
time.sleep(5)

# invoking the export pop_up
export_button.click()

# sleep for 3 seconds
time.sleep(3)

# checking if the cancel button is visible and working as expected
cancel_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-entity-list/div/app-export-grid/kendo-dialog/div[2]/kendo-dialog-actions/button[1]")
                                   ))
cancel_button.click()

# sleep for 5 seconds
time.sleep(5)

# invoking the export pop_up
export_button.click()

# sleep for 3 secs
time.sleep(3)

# checking if the export pop up is working as expected
save_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-entity-list/div/app-export-grid/kendo-dialog/div[2]/kendo-dialog-actions/button[2]")
                                   ))
save_button.click()

# sleep for 10 seconds
time.sleep(10)

# Checking the data export has successfully started
export_start = driver.find_element(By.XPATH,
                                   "//body/app-root/app-entity-list/div/app-export-grid/kendo-dialog/div[2]/div/p")
assert export_start.is_displayed()

print("Test Case executed successfully!!!")
