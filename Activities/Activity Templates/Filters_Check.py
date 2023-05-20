import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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

# Find and select 'activities' module from the main menu navigation
activities_module_select = driver.find_element(By.XPATH,
                                               "//body/app-root/app-header/header/section/section/div/div/ul/li[5]/div/span")
activities_module_select.click()

# Sleep for 3 secs
time.sleep(3)

# select activity templates option
activity_template = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-header/header/section/section/div/div/ul/li[5]/div[2]/li[5]")
    ))
activity_template.click()

# sleep for 5 seconds
time.sleep(5)

# checking and clicking on the filters button
filter_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/div/button/button"))
)
filter_button.click()

# sleep for 3 secs
time.sleep(3)

# checking and clicking on the 'add filter' button
add_filter = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[1]/div/div/div/div/div/button"))
)
add_filter.click()

# sleep for 3 secs
time.sleep(3)

# search for the 'Process name' column on the popup window
process_search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "input-column"))
)
process_search.click()
process_search.send_keys("Process")

# sleep for 3 seconds
time.sleep(3)

# select  the process options from the list
wait = WebDriverWait(driver, 10)
list_element = wait.until(EC.visibility_of_element_located((By.ID, "column-list")))
item_xpath = "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[1]/ul/li[1]/label"
item_element = list_element.find_element(By.XPATH, item_xpath)
item_element.click()

# wait for 3 seconds
time.sleep(3)

# entering the process we want to filter
filter_box_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/app-external-multicheck-filter/div/ul/li[1]/input")
                                   ))
filter_box_input.click()
filter_box_input.send_keys("Land Preparation")

# sleep for 3 seconds
time.sleep(3)

# checking the process we need
check_process = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/app-external-multicheck-filter/div/ul/li[2]/input"))
)
check_process.click()

# sleep for 3 secs
time.sleep(3)

# checking and clicking the 'filter' button
filter_button_two = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/app-external-multicheck-filter/div/div/button[2]"))
)
filter_button_two.click()

# sleep for 5 seconds
time.sleep(5)

# Test Summary
print("Test case executed successfully!!!")