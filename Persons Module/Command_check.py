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

# Find and select 'Persons' module from the main menu navigation
shamba_module_select = driver.find_element(By.XPATH, '//*[@id="menu-navigation"]/ul/li[3]')
shamba_module_select.click()

# Sleep for 5 secs
time.sleep(20)

# Wait for the 'Persons Table' to load
persons_header = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "module-header")))

# Check that we are on the 'Persons Table' page
assert persons_header.is_displayed

# Checking for the 'Persons Table' header elements
filters_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "filters-button"))
)
filters_button.click()

# sleep for 3 seconds
time.sleep(3)

# checking and clicking on the 'add filter' button
add_filter = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[@id='filter-box-data']/div[1]/div[1]/div[1]/div[1]/button[1]"))
)
add_filter.click()

# Sleep for 3 seconds
time.sleep(3)

# Search for a column you want to filter
filter_column = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search a column']"))
)

filter_column.click()
filter_column.send_keys("Full Name")

# wait for the list to be visible and select full name from the list options
wait = WebDriverWait(driver, 10)
list_element = wait.until(EC.visibility_of_element_located((By.ID, "column-list")))
item_xpath = "//*[@id='column-list']/li[9]/label"
item_element = list_element.find_element(By.XPATH, item_xpath)
item_element.click()

# sleep for 3 seconds
time.sleep(3)

# clicking on the filter box text field and typing in the 'KCode' we wish to filter
enter_full_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "k-textbox"))
)
enter_full_name.click()
enter_full_name.send_keys("Alfred Automation Test")

# sleep for 5 seconds
time.sleep(5)

# searching and clicking on the 'Filter' button
filter_button_click = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "k-primary")))

filter_button_click.click()

# sleep for 5 seconds
time.sleep(5)

# checking and clicking on the command icon
command_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "checkmark"))
)
command_icon.click()

# sleep for 3 seconds
time.sleep(3)

# checking and clicking on the batch edit icon on the page header
batch_edit_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-entity-list/div/kendo-grid/kendo-grid-toolbar/div/kendo-menu/ul/li/span"))
)
batch_edit_button.click()

# sleep for 3 seconds
time.sleep(3)

# checking if the batch edit pop up has been displayed
batch_edit_dialog = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-entity-list/div/app-batch-edit/kendo-dialog/div[2]/kendo-dialog-titlebar"))
)
assert batch_edit_dialog.is_displayed

# checking if the cancel icon on the pop-up is working
cancel_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-entity-list/div/app-batch-edit/kendo-dialog/div[2]/kendo-dialog-titlebar/div[2]/a"))
)
cancel_icon.click()

# sleep for 3 seconds
time.sleep(3)

# selecting the field to edit
batch_edit_button.click()
select_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-entity-list/div/app-batch-edit/kendo-dialog/div[2]/div/div/span/kendo-combobox/span/kendo-searchbar/input"))
)
select_field.click()
select_field.send_keys("official_type_id")
select_field.send_keys(Keys.ENTER)

# sleep for 3 seconds
time.sleep(3)

# selecting the corresponding value
value_edit = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-entity-list/div/app-batch-edit/kendo-dialog/div[2]/div/div[2]/span/kendo-combobox/span/kendo-searchbar/input"))
)
value_edit.click()
value_edit.send_keys("National ID")
value_edit.send_keys(Keys.ENTER)

# sleep f0r 3 seconds
time.sleep(3)

# clicking on the cancel button
cancel_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-entity-list/div/app-batch-edit/kendo-dialog/div[2]/kendo-dialog-actions/button[1]"))
)
cancel_button.click()

# sleep for 5 seconds
time.sleep(5)