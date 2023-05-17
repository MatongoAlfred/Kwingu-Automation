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

# filtering the user whose details we want to view
# checking and clicking on the filter icon
filter_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-entity-list/div/kendo-grid/kendo-grid-toolbar/div/button[1]"))
)

assert filter_icon.is_displayed
filter_icon.click()

# sleep for 3 seconds
time.sleep(3)

# checking and clicking on the 'add filter' button
add_filter_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-entity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[1]/div/div/div/div/div/button"))
)
add_filter_button.click()

# sleep for 3 seconds
time.sleep(3)

# Search for a column you want to filter
filter_column = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search a column']"))
)

filter_column.click()
filter_column.send_keys("Username")

# wait for the list to be visible and select 'Role(Kwingu)' from the list options
wait = WebDriverWait(driver, 10)
list_element = wait.until(EC.visibility_of_element_located((By.ID, "column-list")))
item_xpath = "//*[@id='column-list']/li[1]/label"
item_element = list_element.find_element(By.XPATH, item_xpath)
item_element.click()

# sleep for 5 seconds
time.sleep(5)

# checking if the username filter box is visible
filter_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "filter-boxes"))
)
assert filter_box.is_displayed

# entering the username you want to filter
username_text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-entity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/div/app-custom-row-filter/div/input"))
)
username_text.click()
username_text.send_keys("32782214")

# sleep for 3 seconds
time.sleep(3)

# checking if the 'filter button' is working as expected
filter_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-entity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/div/app-custom-row-filter/div/div[2]/button[2]"))
)
filter_button.click()

# sleep for 5 seconds
time.sleep(5)

# checking and clicking on the user full view icon
user_full_view = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-entity-list/div/kendo-grid/div/kendo-grid-list/div[1]/div[1]/table/tbody/tr[1]/td/span[2]/button"))
)
user_full_view.click()

# sleep for 3 seconds
time.sleep(3)

# checking that we are on the user full view page
full_view_check = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "full-view-title-bar"))
)
assert full_view_check.is_displayed

# checking if the edit icon is working as expected
edit_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-entity-add-edit/div/div/div[2]/div[1]/div[2]/img[1]"))
)
edit_icon.click()

# sleep for 3 seconds
time.sleep(3)

# editing the user full view
# editing the person's name
person_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-entity-add-edit/div/div/div[2]/div[2]/fieldset/form/div/div[1]/input"))
)
person_name.click()
person_name.clear()
person_name.send_keys("32782214")

# sleep for 5 seconds
time.sleep(5)

# checking if the 'Save' button is working as expected
save_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "save-button"))
)
save_button.click()

# sleep for 3 seconds
time.sleep(3)
