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

# Find and select 'inventory' module from the main menu navigation
inventory_module_select = driver.find_element(By.XPATH,
                                              "//body/app-root/app-header/header/section/section/div/div/ul/li[6]/div/span")
inventory_module_select.click()

# Sleep for 3 secs
time.sleep(3)

# select inventory activity option
inventory_activity = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-header/header/section/section/div/div/ul/li[6]/div[2]/li[1]/a")
    ))
inventory_activity.click()

# sleep for 5 seconds
time.sleep(5)

# close the sidebar navigation menu
close_side_menu = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "menu-bar-open"))
)
close_side_menu.click()

# sleep for 3 seconds
time.sleep(3)

# assert that were are on the inventory activity page
inventory_activity_page = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-inventory-activities/div/kendo-grid/kendo-grid-toolbar/span"))
)
assert inventory_activity_page.is_displayed()

# sleep for 3 secs
time.sleep(3)

# look for the filter button and click on it
filter_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "filter-class-icon"))
)
filter_button.click()

# sleep for 3 seconds
time.sleep(3)

# Checking the 'internal filters'
# clicking on the add filter button
add_filter_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-inventory-activities/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[1]/div/div/div/div/div/button"))
)
add_filter_button.click()

# sleep for 3 seconds
time.sleep(3)

# search for the 'shamba kcode' column on the popup window
kcode_search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "input-column"))
)
kcode_search.click()
kcode_search.send_keys("shamba kcode")

# sleep for 3 seconds
time.sleep(3)

# select and clicking on the shamba kcode option from the list
wait = WebDriverWait(driver, 10)
list_element = wait.until(EC.visibility_of_element_located((By.ID, "column-list")))
item_xpath = "//*[@id='column-list']/li[5]/label"
item_element = list_element.find_element(By.XPATH, item_xpath)
item_element.click()

# wait for 3 seconds
time.sleep(3)

# entering the kcode we want to filter
filter_box_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-inventory-activities/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/app-external-row-filter/div/input")
                                   ))
filter_box_input.click()
filter_box_input.send_keys("kwl-2023-0159")

# sleep for 3 seconds
time.sleep(3)

# checking and clicking the 'filter' button
filter_button_two = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-inventory-activities/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/app-external-row-filter/div/div[2]/button[2]"))
)
filter_button_two.click()

# sleep for 5 seconds
time.sleep(5)

# Checking the 'external filters'
external_filter = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-inventory-activities/div/kendo-grid/div/div/div[2]/table/thead/tr/th[5]/kendo-grid-filter-menu/a"))
)
external_filter.click()

# sleep for 3 seconds
time.sleep(3)

# clearing the applied internal filter
clear_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/kendo-popup/div/kendo-grid-filter-menu-container/form/div/app-custom-row-filter/div/div/button[1]"))
)
clear_button.click()

# sleep for 3 secs
time.sleep(3)

# checking the external filter if it works
external_filter1 = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-inventory-activities/div/kendo-grid/div/div/div[2]/table/thead/tr/th[5]/kendo-grid-filter-menu/a"))
)
external_filter1.click()

# sleep for 3 secs
time.sleep(3)

# launch pop up here
external_filter_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/kendo-popup/div/kendo-grid-filter-menu-container/form/div/app-custom-row-filter/div/input"))
)
external_filter_input.click()
external_filter_input.clear()
external_filter_input.send_keys("kwl-2023-0159")

# clicking on the filter button
external_filter_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/kendo-popup/div/kendo-grid-filter-menu-container/form/div/app-custom-row-filter/div/div/button[2]"))
)
external_filter_button.click()

# sleep for 5 seconds
time.sleep(5)

# Test summary report
print("Test case successfully executed!!!")
