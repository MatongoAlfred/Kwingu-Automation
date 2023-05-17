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

# select user zone assignment option
user_management = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-header/header/section/section/div/div/ul/li[4]/div[2]/li[3]")
    ))
user_management.click()

# sleep for 3 seconds
time.sleep(3)

# checking if the header elements exist
filter_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "filter-class-icon"))
)

assert filter_icon.is_displayed()

# clicking on the filter icon
filter_icon.click()

# sleep for 3 secs
time.sleep(3)

# checking and clicking on the 'add filter' button
add_filter_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-zone-assignment/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[1]/div/div/div/div/div/button"))
)
add_filter_button.click()

# sleep for 3 seconds
time.sleep(3)

# Search for a column you want to filter
filter_column = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-zone-assignment/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[1]/input"))
)

filter_column.click()
filter_column.send_keys("Zone")

# wait for the list to be visible and select 'Zone' from the list options
zone_select = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-zone-assignment/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/ul/li[1]/label"))
)
zone_select.click()

# sleep for 5 seconds
time.sleep(5)

# checking if the zone filter box is visible
filter_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "filter-boxes"))
)
assert filter_box.is_displayed

# entering the zone you want to filter
zone_text = WebDriverWait(driver, 10).until(
   EC.presence_of_element_located((By.XPATH, "//body/app-root/app-zone-assignment/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/div/app-external-row-filter/div/input"))
)
zone_text.click()
zone_text.send_keys("kwale")

# sleep for 3 seconds
time.sleep(3)

# checking if the 'filter button' is working as expected
filter_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-zone-assignment/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/div/app-external-row-filter/div/div/button[2]"))
)
filter_button.click()

# sleep for 5 seconds
time.sleep(5)

# checking if you can remove the applied filter
remove_filter = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "close-button"))
)
remove_filter.click()

# sleep for 3 seconds
time.sleep(3)
