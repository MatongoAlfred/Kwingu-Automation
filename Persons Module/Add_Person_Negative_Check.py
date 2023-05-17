import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# set up the Chrome webdriver
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

# clicking on the 'Hamburger Menu" icon
hamburger_menu_icon.click()

# Sleep for 3 secs
time.sleep(3)

# find and select 'Persons' module from the main menu navigation
shamba_module_select = driver.find_element(By.XPATH, '//*[@id="menu-navigation"]/ul/li[3]')
shamba_module_select.click()

# sleep for 3 secs
time.sleep(3)

# wait for the 'Persons Table' to load
persons_header = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "module-header")))

# Check that we are on the 'Persons Table' page
assert persons_header.is_displayed

# closing the sidebar main navigation menu
hamburger_menu_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "menu-bar-open"))
)
hamburger_menu_icon.click()

# sleep for 3 secs
time.sleep(3)

# Checking and clicking on the 'Add Entity' button
export_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-entity-list/div/kendo-grid/kendo-grid-toolbar/div/button[3]"))
)
export_button.click()

# sleep for 3 seconds
time.sleep(3)

# adding person's first name details
first_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[1]/div/input"))
)
first_name.click()

# first name text box is empty
first_name_error_two = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[1]/div/div"))
)
assert first_name_error_two.is_displayed()

# sleep for 3 seconds
time.sleep(3)

# entering invalid values in the first name text field
first_name.send_keys("6536(#90+++")

# first name text box has invalid values entered
first_name_error_one = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[1]/div/div[2]"))
)
assert first_name_error_one.is_displayed()

# sleep for 5 secs
time.sleep(5)

# entering the valid first name
first_name.clear()
first_name.send_keys("Sam")

# sleep for 5 seconds
time.sleep(5)

# adding the middle name --- first name negative test case applies
middle_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[2]/div/input"))
)
middle_name.click()
middle_name.send_keys("Automation")

# adding the last name --- first name negative test case applies
last_name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "/html/body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[3]/div/input"))
)
last_name.click()
last_name.send_keys("Test")

# adding the Employee ID ---- does not need validation
employee_ID = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[5]/div/input"))
)
employee_ID.click()
employee_ID.send_keys("4433221122")

# sleep for 5 seconds
time.sleep(5)

# add the Employee National ID
national_ID = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[6]/div/input"))
)
national_ID.click()

# Employee national ID text field is empty
national_ID_error_one = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[6]/div/div"))
)
assert national_ID_error_one.is_displayed()

# Entering only a space in the national ID text field
national_ID.send_keys(" ")
national_ID_error_two = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[6]/div/div"))
)
# sleep for 5 seconds
time.sleep(5)

# Entering a valid ID number in the national ID text field
national_ID.clear()
national_ID.send_keys("32752233")

# Sleep for 5 seconds
time.sleep(5)

# selecting the FA Role
role_select = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[7]/span/kendo-combobox/span/kendo-searchbar/input"))
)
role_select.click()
role_select.send_keys("Field Facilitator")
role_select.send_keys(Keys.ENTER)

# sleep for 5 seconds
time.sleep(5)

# entering an invalid role
role_select.clear()
role_select.send_keys("56789@1")

# checking if the correct error is being displayed
role_select_error = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "k-nodata"))
)
assert role_select_error.is_displayed()

# sleep for 5 seconds
time.sleep(5)

# selecting a valid role
role_select.clear()
role_select.send_keys("Field Facilitator")
role_select.send_keys(Keys.ENTER)

# sleep for 5 seconds
time.sleep(5)

# adding FA Phone number
fa_number = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[9]/div/input"))
)
fa_number.click()

# phone number text field is empty
fa_number_empty_error = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[9]/div/div"))
)
assert fa_number_empty_error.is_displayed()

# keying in an invalid phone number
fa_number.send_keys("23")
fa_number_empty_error_one = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[9]/div/div[2]"))
)
assert fa_number_empty_error_one.is_displayed()

# sleep for 5 secs
time.sleep(5)

# entering a valid phone number
fa_number.clear()
fa_number.send_keys("0711223344")

# sleep for 5 seconds
time.sleep(5)

# selecting the Country Code
code_select = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[10]/div/span/kendo-combobox/span/kendo-searchbar/input"))
)
code_select.click()

# country code text field is empty
code_select_error = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[10]/div/div"))
)
assert code_select_error.is_displayed()

# entering an invalid country code
code_select.send_keys("25423")
code_select_error_one = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "k-nodata"))
)
assert code_select_error_one.is_displayed()

# sleep for 5 secs
time.sleep(5)

# entering a valid country code
code_select.clear()
code_select.send_keys("254")
code_select.send_keys(Keys.ENTER)

# sleep for 5 seconds
time.sleep(5)

# selecting the active status
status_check = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[15]/span[2]/div[1]/label"))
)
status_check.click()

# sleep for 5 seconds
time.sleep(5)

# selecting the active status as NO
status_check = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[15]/span[2]/div[2]/label"))
)
status_check.click()

# checking if the 'Inactivity reason is displayed
inactivity_reason = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[16]/span/kendo-combobox/span/kendo-searchbar"))
)
assert inactivity_reason.is_displayed

# sleep for 5 seconds
time.sleep(5)

# checking if the inactivity field has the required options
inactivity_reason.click()

# sleep for 5 seconds
time.sleep(5)

# selecting the represents organisation check box
rep_check = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[14]/span[2]/div[1]/label"))
)
rep_check.click()

# sleep for 5 seconds
time.sleep(5)

# represents active  status selection
rep_status_check = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[16]/span/kendo-combobox/span/kendo-searchbar/input"))
)
rep_status_check.click()
rep_status_check.send_keys("Active")
rep_status_check.send_keys(Keys.ENTER)

# sleep for 5 seconds
time.sleep(5)

# tapping the save button
save_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[1]/div[3]/button[2]"))
)
save_button.click()

# sleep for 5 seconds
time.sleep(5)

# selecting 'YES' on the confirmation pop up
pop_up_yes = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-person-add-edit/kendo-dialog/div[2]/kendo-dialog-actions/button[2]"))
)
pop_up_yes.click()

# sleep for 5 seconds
time.sleep(5)

# Ascertain that the test case passed
print("Test Case Executed successfully")
