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

# select activities submission option
activities_submission = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-header/header/section/section/div/div/ul/li[5]/div[2]/li[2]/a")
    ))
activities_submission.click()

# sleep for 5 seconds
time.sleep(5)

# checking and clicking on the filters button
filter_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/div/button[2]"))
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
item_xpath = "//*[@id='column-list']/li[2]/label"
item_element = list_element.find_element(By.XPATH, item_xpath)
item_element.click()

# wait for 3 seconds
time.sleep(3)

# entering the kcode we want to filter
filter_box_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/app-external-row-filter/div/input")
                                   ))
filter_box_input.click()
filter_box_input.send_keys("kwl-2023-0212")

# sleep for 3 seconds
time.sleep(3)

# checking and clicking the 'filter' button
filter_button_two = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/app-external-row-filter/div/div/button[2]"))
)
filter_button_two.click()

# sleep for 5 seconds
time.sleep(5)

# using internal filters to filter by status
status_filter = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[1]/div/div/div/div[2]/div/button"))
)
status_filter.click()

# sleep for 3 seconds
time.sleep(3)

# typing in the column we need : status column
select_status = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[1]/div/input"))
)
select_status.click()
select_status.send_keys("Status")

# sleep for 3 secs
time.sleep(3)

# select and clicking on the status option from the list
wait = WebDriverWait(driver, 10)
list_element = wait.until(EC.visibility_of_element_located((By.ID, "column-list")))
item_xpath = "//*[@id='column-list']/li[6]/label[1]"
item_element = list_element.find_element(By.XPATH, item_xpath)
item_element.click()

# sleep for 3 secs
time.sleep(3)

# searching the status we want to filter
text_status = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/app-external-multicheck-filter/div/ul/li[1]/input"))
)
text_status.click()
text_status.send_keys("Submitted")

# sleep for 3 secs
time.sleep(3)

# clicking on the 'submitted'status
submitted_status = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/app-external-multicheck-filter/div/ul/li[2]/input"))
)
submitted_status.click()

# sleep for 3 secs
time.sleep(3)

# clicking on the 'Filter' button
filter_click = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/app-external-multicheck-filter/div/div/button[2]"))
)
filter_click.click()

# sleep for 3 secs
time.sleep(3)

# checking if the 'View Activity' icon is available and clickable
view_activity_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-activity-list/div/kendo-grid/div/kendo-grid-list/div[1]/div[1]/table/tbody/tr/td/span/button"))
)
view_activity_icon.click()

# sleep for 3 secs
time.sleep(3)

# ascertain that were are in the activity full view
activity_full_view = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.XPATH, "//body/app-root/app-activity-review/div/div/div[2]/div[2]/fieldset/form/div[1]/h3"))
)
assert activity_full_view.is_displayed()

# checking if the contract photo is available in the activity form answers
contract_image_check = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-activity-review/div/div/div[2]/div[2]/fieldset/form/div[2]/div/div[1]/div[29]/div/span/div[2]/button[1]"))
)
contract_image_check.click()

# sleep for 3 seconds
time.sleep(3)

# closing the contract image
close_image = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-activity-review/kendo-dialog/div[2]/div/span/i"))
)
close_image.click()

# sleep for 3 seconds
time.sleep(3)

# test summary
print("Test case executed successfully")
