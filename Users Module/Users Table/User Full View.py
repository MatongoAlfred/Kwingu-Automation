import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from tkinter import Tk, Text

# set up the Chrome web-driver
service_object = Service('C:\\Users\\alfred.matongo_komaz\\PycharmProjects\\Kwingu_Automation\\Browsers\\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

# Maximize the browser window
driver.maximize_window()

# Create a Tkinter window
window = Tk()
window.title("Automated Test : Password Reset")
window.configure(bg="Dark Green")

# Create a Text widget to display the report
report_text = Text(window, height=25, width=100, font=("IBM Plex Sans", 12))
report_text.pack()

# Counter for bullet points
bullet_count = 0

# Flag to track if Test Summary header has been displayed
is_test_summary_displayed = False

# Flag to track if the test encountered an error
has_error = False


# Function to update the report
def update_report(message, is_header=False, is_footer=False, is_bold=False):
    global is_test_summary_displayed, bullet_count, has_error
    if is_header:
        if is_test_summary_displayed:
            return
        report_text.insert("end", message + "\n")
        report_text.tag_config("bold", font=("IBM Plex Sans", 12, "bold"))
        report_text.insert("end", "\n", "bold")
        is_test_summary_displayed = True
    else:
        if is_footer:
            report_text.insert("end", message + "\n")
            if is_bold:
                report_text.tag_config("bold", font=("IBM Plex Sans", 12, "bold"))
                report_text.insert("end", "\n", "bold")
        else:
            bullet_count += 1
            report_text.insert("end", "• " + message + "\n")
            if has_error:
                report_text.tag_config("error", font=("IBM Plex Sans", 12, "bold"), foreground="red")
                report_text.insert("end", "Test failed, we encountered an error as seen above\n", "error")
    report_text.update()


try:
    # navigate to the Kwingu login page
    driver.get("https://uatkwingu.komaza.com/login")
    update_report("Here are the test results: ", is_header=True)
    update_report("User is able to navigate to Kwingu login page")

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
    update_report("User is able to enter the username")
    update_report("User is able to enter the password")

    # tab the Sign_In button
    submit_button = driver.find_element(By.XPATH, "//button[@class='login-button']")
    submit_button.click()
    update_report("User is able to see and click on the sign in button ")

    # wait for the FOPs_dashboard to load
    dashboard_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='module-header']"))
    )

    # sleep for 5 secs
    time.sleep(5)

    # check that we are on the dashboard page
    assert dashboard_header.is_displayed
    update_report("User is able to see that the FOPs dashboard has successfully loaded ")

    # check that the FOPs_dashboard page has the 'Hamburger Menu' icon
    hamburger_menu_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "menu-bar-close"))
    )

    # Clicking on the 'Hamburger Menu' icon
    hamburger_menu_icon.click()
    update_report("User is able to open the side navigation menu")

    # Sleep for 5 secs
    time.sleep(5)

    # Find and select 'Users' module from the main menu navigation
    users_module_select = driver.find_element(
        By.XPATH, "//body/app-root/app-header/header/section/section/div/div/ul/li[4]/div/span/i"
    )
    users_module_select.click()
    update_report("User is able to select the users module from the side navigation menu ")

    # Sleep for 5 secs
    time.sleep(5)

    # select user management option
    user_management = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root/app-header/header/section/section/div/div/ul/li[4]/div[2]/li[1]"))
    )
    user_management.click()
    update_report("User is able to select the user management sub module ")

    # sleep for 3 seconds
    time.sleep(3)

    # checking and clicking on the filter icon
    filter_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root/app-entity-list/div/kendo-grid/kendo-grid-toolbar/div/button[1]"))
    )

    assert filter_icon.is_displayed
    filter_icon.click()
    update_report("User is able to see and click the main filter icon on the page header")

    # sleep for 3 seconds
    time.sleep(3)

    # checking and clicking on the 'add filter' button
    add_filter_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root/app-entity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[1]/div/div/div/div/div/button"))
    )
    add_filter_button.click()
    update_report("User is able to see and click on the add filter button on the expanded filter view ")

    # sleep for 3 seconds
    time.sleep(3)

    # Search for a column you want to filter
    filter_column = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search a column']"))
    )

    filter_column.click()
    filter_column.send_keys("Username")
    update_report("User is able to click on the search a filter input box ")
    update_report("User is able to to enter in the column they wish to filter on the search box")

    # wait for the list to be visible and select 'Role(Kwingu)' from the list options
    wait = WebDriverWait(driver, 10)
    list_element = wait.until(EC.visibility_of_element_located((By.ID, "column-list")))
    item_xpath = "//*[@id='column-list']/li[1]/label"
    item_element = list_element.find_element(By.XPATH, item_xpath)
    item_element.click()
    update_report("User is able to select the username column from the list")

    # sleep for 5 seconds
    time.sleep(5)

    # checking if the username filter box is visible
    filter_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root/app-entity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/app-external-row-filter/div/input"))
    )
    assert filter_box.is_displayed
    update_report("User is able to see the filter pop up window is displayed for internal filters")

    # sleep for 5 secs
    time.sleep(5)

    # entering the username you want to filter
    username_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root/app-entity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/app-external-row-filter/div/input"))
    )
    username_text.click()
    username_text.send_keys("32782214")
    update_report("User is able to enter the username ")

    # sleep for 3 seconds
    time.sleep(3)

    # checking if the 'filter button' is working as expected
    filter_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root/app-entity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/app-external-row-filter/div/div/button[2]"))
    )
    filter_button.click()
    update_report("User is able to see and click on the filter button on the filter box")

    # sleep for 3 seconds
    time.sleep(3)

    # checking and clicking on the user full view icon
    user_full_view = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-entity-list/div/kendo-grid/div/kendo-grid-list/div[1]/div[1]/table/tbody/tr[1]/td/span[2]/button"))
    )
    user_full_view.click()
    update_report("User is able to see and click on user full view icon")

    # sleep for 3 seconds
    time.sleep(3)

    # checking that we are on the user full view page
    full_view_check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "full-view-title-bar"))
    )
    assert full_view_check.is_displayed
    update_report("User is able to see they have been navigated to the user full view")

    # checking if the edit icon is working as expected
    edit_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-entity-add-edit/div/div/div[2]/div[1]/div[2]/img[1]"))
    )
    edit_icon.click()
    update_report("User is able to see that the edit icon is working as expected")

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
    update_report("User is able to see and clear the name")
    update_report("User is able to see and enter in a new name for the user")

    # sleep for 5 seconds
    time.sleep(5)

    # checking if the 'Save' button is working as expected
    save_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "save-button"))
    )
    save_button.click()
    update_report("User is able to see and click on the filter button and see that is working as expected")

    # sleep for 3 seconds
    time.sleep(3)

except Exception as e:
    has_error = True
    update_report("Error: " + str(e))

finally:

    # Close the browser window
    driver.quit()

update_report("Test Execution Completed", is_footer=True, is_bold=True)
update_report("Further Analysis : ", is_footer=True, is_bold=True)

# Display the total bullet count
update_report(f"Total test cases executed: {bullet_count}", is_footer=True, is_bold=True)

# Publish the final test result
if has_error:
    update_report("Test failed, we encountered an error as seen above")
else:
    update_report("The test was a success, all test cases passed")

# Start the Tkinter event loop
window.mainloop()
