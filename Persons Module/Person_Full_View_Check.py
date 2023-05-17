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

# Find and select 'Persons' module from the main menu navigation
shamba_module_select = driver.find_element(By.XPATH, '//*[@id="menu-navigation"]/ul/li[3]')
shamba_module_select.click()

# Sleep for 5 secs
time.sleep(5)

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

# clicking on the person full view
person_full_view = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-entity-list/div/kendo-grid/div/kendo-grid-list/div[1]/div[1]/table/tbody/tr[1]/td/span[2]/button"))
)
person_full_view.click()

# sleep for 5 seconds
time.sleep(5)

# clicking on the edit icon
edit_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[1]/div[2]/img[1]"))
)
edit_icon.click()

# sleep for 3 seconds
time.sleep(3)

# checking if the cancel button is working as expected
cancel_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "cancel-button"))
)
cancel_button.click()

# sleep for 3 seconds
time.sleep(3)

# clicking on the edit icon
edit_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[1]/div[2]/img[1]"))
)
edit_icon.click()

# sleep for 3 seconds
time.sleep(3)

# editing person's full name
first_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[1]/div/input"))
)
first_name.clear()

# sleep for 3 seconds
time.sleep(3)

# entering the new name
first_name.send_keys("Alfred")

# changing the role to the FM
role_select = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[7]/span/kendo-combobox/span/kendo-searchbar/input"))
)
role_select.clear()

# sleep for 3 seconds
time.sleep(3)

# selecting the new role i.e. FM
role_select.send_keys("Field Manager")
role_select.send_keys(Keys.ENTER)

# saving the person's details
save_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "save-button"))
)
save_button.click()

# sleep for 5 seconds
time.sleep(5)

# checking if the role change pop-up is getting displayed
role_pop_up = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-person-add-edit/kendo-dialog/div[2]/kendo-dialog-titlebar"))
)
assert role_pop_up.is_displayed

# clicking 'Yes' on the pop-up
yes_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-person-add-edit/kendo-dialog/div[2]/kendo-dialog-actions/button[2]"))
)
yes_button.click()

# sleep for 3 seconds
time.sleep(3)

# ascertain the test case was executed successfully
print("Test case executed successfully!!!")
