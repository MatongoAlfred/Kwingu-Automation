import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# checking and tapping on the 'Person History' icon
history_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,
                                    "//body/app-root/app-entity-list/div/kendo-grid/div/kendo-grid-list/div[1]/div[1]/table/tbody/tr/td/span[3]/button"))
)
history_button.click()

# sleep for 3 seconds
time.sleep(3)

# checking if the history pop up is visible
history_pop_up = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-entity-list/div/app-list-view/kendo-dialog/div[2]/kendo-dialog-titlebar/div[1]"))
)
assert history_pop_up.is_displayed

# sleep for 3 secs
time.sleep(3)

# checking if the cancel icon is working
cancel_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-entity-list/div/app-list-view/kendo-dialog/div[2]/kendo-dialog-titlebar/div[2]/a"))
)
cancel_icon.click()
# checking if the pop-up navigation are working well
# checking if 'go to next page' button is working
history_button.click()
next_page_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-entity-list/div/app-list-view/kendo-dialog/div[2]/div/kendo-listview/kendo-datapager/kendo-datapager-next-buttons/button[1]"))
)
next_page_icon.click()

# checking if the 'go to previous page' button is working
previous_page_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-entity-list/div/app-list-view/kendo-dialog/div[2]/div/kendo-listview/kendo-datapager/kendo-datapager-prev-buttons/button[2]"))
)
previous_page_icon.click()

# checking if the 'go to last page' button is working
last_page_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-entity-list/div/app-list-view/kendo-dialog/div[2]/div/kendo-listview/kendo-datapager/kendo-datapager-next-buttons/button[2]"))
)
last_page_icon.click()

# checking if the 'go to first page' button is working
first_page_icon = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root/app-entity-list/div/app-list-view/kendo-dialog/div[2]/div/kendo-listview/kendo-datapager/kendo-datapager-prev-buttons/button[1]"))
)
first_page_icon.click()

# checking if the page counter works and is visible
counter_check = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-entity-list[1]/div[1]/app-list-view[1]/kendo-dialog[1]/div[2]/div[1]/kendo-listview[1]/kendo-datapager[1]/kendo-datapager-info[1]"))
)
assert counter_check.is_displayed

# sleep for 4 secs
time.sleep(4)
