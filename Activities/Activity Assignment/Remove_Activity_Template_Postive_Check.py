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

# select activities assignment option
activities_assignment = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-header/header/section/section/div/div/ul/li[5]/div[2]/li[1]/a")
    ))
activities_assignment.click()

# sleep for 5 seconds
time.sleep(5)

# close the sidebar navigation menu
close_side_menu = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "menu-bar-open"))
)
close_side_menu.click()

# sleep for 3 seconds
time.sleep(3)

# assert that were are on the activities assignment page
activity_assignmemt_page = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "activity-ass-header"))
)
assert activity_assignmemt_page.is_displayed()

# wait for the records to load for 10 seconds
time.sleep(10)

# checking the external filter if it works
external_filter_tap = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "th#k-grid0-r0c2 > kendo-grid-filter-menu > a"))
)
external_filter_tap.click()

# sleep for 3 seconds
time.sleep(3)

# entering the kcode
text_input_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root[1]/kendo-popup[1]/div[1]/kendo-grid-filter-menu-container[1]/form[1]/div[1]/app-custom-row-filter[1]/div[1]/input[1]"))
)
text_input_box.click()
text_input_box.send_keys("klf-2023-0037")

# sleep for 3 seconds
time.sleep(3)

# clicking on the filter button
external_filter_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/kendo-popup/div/kendo-grid-filter-menu-container/form/div/app-custom-row-filter/div/div/button[2]"))
)
external_filter_button.click()

# sleep for 5 seconds
time.sleep(5)

# clicking on the command icon
command_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-activity-list/div/kendo-grid/div/kendo-grid-list/div[1]/div[1]/table/tbody/tr/td/label/span"))
)
command_icon.click()

# checking if the actions icon becomes active
actions_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "profile-image")
                                   ))
actions_button.click()

# sleep for 3 seconds
time.sleep(3)

# selecting the remove template option from the list
remove_template = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "remove-template"))
)
remove_template.click()

# sleep for 3 seconds
time.sleep(3)
