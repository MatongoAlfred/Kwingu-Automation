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

# Find and select 'Users' module from the main menu navigation
users_module_select = driver.find_element(By.XPATH,
                                          "//body/app-root/app-header/header/section/section/div/div/ul/li[4]/div/span/i")
users_module_select.click()

# Sleep for 5 secs
time.sleep(5)

# select user tree option
user_management = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-header/header/section/section/div/div/ul/li[4]/div[2]/li[2]/a")
    ))
user_management.click()

# sleep for 3 seconds
time.sleep(3)

# applying the filter by dept filter (Field Operations)
dept_filter = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-user-tree/div/div/kendo-combobox/span/kendo-searchbar/input"))
)
dept_filter.click()
dept_filter.send_keys("Field Operations")
dept_filter.send_keys(Keys.ENTER)

# sleep for 5 seconds
time.sleep(5)

# applying the 'Filter by Role' filter
role_filter = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-user-tree/div/div[2]/kendo-combobox/span/kendo-searchbar/input"))
)
role_filter.click()
role_filter.send_keys("Field Manager")
role_filter.send_keys(Keys.ENTER)

# checking if the 'Filter' button is working as expected
filter_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-user-tree/div/button"))
)
filter_button.click()

# sleep for 5 seconds
time.sleep(5)

# checking if the 'filter by person' filter is working as expected
person_filter = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-user-tree/div/kendo-grid/kendo-grid-toolbar/div/div[2]/kendo-combobox/span/kendo-searchbar/input"))
)
person_filter.click()
person_filter.send_keys("Test Kwale One")

# sleep for 10 seconds
time.sleep(10)
person_filter.send_keys(Keys.ENTER)

# checking if the filter button is working as expected
filter_table_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-user-tree/div/kendo-grid/kendo-grid-toolbar/div/div[2]/button[1]"))
)
filter_table_button.click()

# sleep for 5 secs
time.sleep(5)

# clearing the applied filters
clear_filters = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "clear-filters-button"))
)
clear_filters.click()

# sleep for 3 secs
time.sleep(3)

# checking if the related functionalities are working as expected
# checking if entered name does not exist in the database --- empty pop up is shown
person_filter.click()
person_filter.clear()
person_filter.send_keys("Not Available")

# ascertain that an empty pop up is displayed
empty_pop_up = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/kendo-popup[1]/div[1]/div[1]"))
)
assert empty_pop_up.is_displayed

# sleep for 3 seconds
time.sleep(3)

# checking if the down arrow is working as expected
down_arrow_filter = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-user-tree/div/kendo-grid/kendo-grid-toolbar/div/div[2]/kendo-combobox/span/span/span"))
)
down_arrow_filter.click()
assert empty_pop_up.is_displayed

# sleep for 3 secs
time.sleep(3)

# checking if the 'reset department' button is working as expected
reset_dept = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-user-tree/div/kendo-grid/kendo-grid-toolbar/button"))
)
reset_dept.click()

# sleep for 3 seconds
time.sleep(3)

# ascertain that the test case was executed successfully
print("Test Case Executed Successfully!!!!")