import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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
    update_report("Here are the test results : ", is_header=True)
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
    update_report("User is able to see and click on the Login button")

    # wait for the FOPs_dashboard to load
    dashboard_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='module-header']")))

    # sleep for 5 secs
    time.sleep(5)

    # check that we are on the dashboard page
    assert dashboard_header.is_displayed
    update_report("User is able to see that the FOPs Dashboard has successfully load")

    # check that the FOPs_dashboard page has the 'Hamburger Menu' icon
    hamburger_menu_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "menu-bar-close"))
    )

    # Clicking on the 'Hamburger Menu' icon
    hamburger_menu_icon.click()
    update_report("User is able to open the side navigation menu")

    # Sleep for 5 secs
    time.sleep(5)

    # Find and select 'Persons' module from the main menu navigation
    shamba_module_select = driver.find_element(By.XPATH, '//*[@id="menu-navigation"]/ul/li[3]')
    shamba_module_select.click()
    update_report("User is able to select the persons module on option from the side navigation menu")

    # Sleep for 5 secs
    time.sleep(20)

    # Wait for the 'Persons Table' to load
    persons_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "module-header")))

    # Check that we are on the 'Persons Table' page
    assert persons_header.is_displayed
    update_report("User is able to the persons table successfully load")

    # Checking for the 'Persons Table' header elements
    filters_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "filters-button"))
    )
    filters_button.click()
    update_report("User is able to see and click on the filters button")

    # sleep for 3 seconds
    time.sleep(3)

    # checking and clicking on the 'add filter' button
    add_filter = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='filter-box-data']/div[1]/div[1]/div[1]/div[1]/button[1]"))
    )
    add_filter.click()
    update_report("User is able to see and click on the 'Add filter' button")

    # Sleep for 3 seconds
    time.sleep(3)

    # Search for a column you want to filter
    filter_column = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search a column']"))
    )

    filter_column.click()
    filter_column.send_keys("Full Name")
    update_report("User is able to search for the 'Full name' column on the internal filters search box")

    # wait for the list to be visible and select full name from the list options
    wait = WebDriverWait(driver, 10)
    list_element = wait.until(EC.visibility_of_element_located((By.ID, "column-list")))
    item_xpath = "//*[@id='column-list']/li[9]/label"
    item_element = list_element.find_element(By.XPATH, item_xpath)
    item_element.click()
    update_report("User is able to navigate to Kwingu login page")

    # sleep for 3 seconds
    time.sleep(3)

    # clicking on the filter box text field and typing in the 'KCode' we wish to filter
    enter_full_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "k-textbox"))
    )
    enter_full_name.click()
    enter_full_name.send_keys("Alfred Automation Test")
    update_report("User is able to enter the Persons full name they wish to filter")

    # sleep for 5 seconds
    time.sleep(5)

    # searching and clicking on the 'Filter' button
    filter_button_click = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "k-primary")))

    filter_button_click.click()
    update_report("User is able to see and click on the Filter button")

    # sleep for 5 seconds
    time.sleep(5)

    # checking and clicking on the command icon
    command_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "checkmark"))
    )
    command_icon.click()
    update_report("User is able to see and click on the command icon")

    # sleep for 3 seconds
    time.sleep(3)

    # checking and clicking on the batch edit icon on the page header
    batch_edit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-entity-list/div/kendo-grid/kendo-grid-toolbar/div/kendo-menu/ul/li/span"))
    )
    batch_edit_button.click()
    update_report("User is able to see and click on the batch edit icon")

    # sleep for 3 seconds
    time.sleep(3)

    # checking if the batch edit pop up has been displayed
    batch_edit_dialog = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-entity-list/div/app-batch-edit/kendo-dialog/div[2]/kendo-dialog-titlebar"))
    )
    assert batch_edit_dialog.is_displayed
    update_report("User is able to see that the batch edit pop up has been displayed")

    # checking if the cancel icon on the pop-up is working
    cancel_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-entity-list/div/app-batch-edit/kendo-dialog/div[2]/kendo-dialog-titlebar/div[2]/a"))
    )
    cancel_icon.click()
    update_report("User is able to see and click on the cancel icon")

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
    update_report("User is able to select 'official id type' as the field to edit")

    # sleep for 3 seconds
    time.sleep(3)

    # selecting the corresponding value
    value_edit = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root/app-entity-list/div/app-batch-edit/kendo-dialog/div[2]/div/div[2]/span/kendo-combobox/span/kendo-searchbar/input"))
    )
    value_edit.click()
    value_edit.send_keys("National ID")
    value_edit.send_keys(Keys.ENTER)
    update_report("User is able to select 'National ID' as the 'official ID type' to edit")

    # sleep f0r 3 seconds
    time.sleep(3)

    # clicking on the cancel button
    cancel_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root/app-entity-list/div/app-batch-edit/kendo-dialog/div[2]/kendo-dialog-actions/button[1]"))
    )
    cancel_button.click()
    update_report("User is able to see and click on the 'cancel' button")

    # sleep for 5 seconds
    time.sleep(5)

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