import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from tkinter import Tk, Text

# set up the Chrome web-driver
service_object = Service(
    'C:\\Users\\alfred.matongo_komaz\\PycharmProjects\\Kwingu_Automation\\Browsers\\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

# Maximize the browser window
driver.maximize_window()

# Create a Tkinter window
window = Tk()
window.title("Automated Test : Delete Person")
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
    update_report("User is able to enter username")
    update_report("User is able to enter the password")

    # tab the Sign_In button
    submit_button = driver.find_element(By.XPATH, "//button[@class='login-button']")
    submit_button.click()
    update_report("User is able to see and click the sign in button ")

    # wait for the FOPs_dashboard to load
    dashboard_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='module-header']")))

    # sleep for 2 secs
    time.sleep(2)

    # check that we are on the dashboard page
    assert dashboard_header.is_displayed
    update_report("User is able to see that the FOPs dashboard has successfully load")

    # check that the FOPs_dashboard page has the 'Hamburger Menu' icon
    hamburger_menu_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "menu-bar-close"))
    )

    # Clicking on the 'Hamburger Menu' icon
    hamburger_menu_icon.click()
    update_report("User is able to open the side navigation menu")

    # Sleep for 3 secs
    time.sleep(3)

    # Find and select 'Persons' module from the main menu navigation
    shamba_module_select = driver.find_element(By.XPATH, '//*[@id="menu-navigation"]/ul/li[3]')
    shamba_module_select.click()
    update_report("User is able to select persons module the side navigation menu")

    # Sleep for 2 secs
    time.sleep(2)

    # Wait for the 'Persons Table' to load
    persons_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "module-header")))

    # Check that we are on the 'Persons Table' page
    assert persons_header.is_displayed
    update_report("User is able to see that the persons table has successfully load")

    # closing the sidebar menu navigation
    hamburger_menu_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "menu-bar-open"))
    )
    hamburger_menu_icon.click()
    update_report("User is able to close the side navigation menu")

    # sleep for 3 seconds
    time.sleep(3)

    # Checking and clicking on the main filter button
    filters_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "filters-button"))
    )
    filters_button.click()
    update_report("User is able to click on the main filter button")

    # sleep for 2 seconds
    time.sleep(2)

    # checking and clicking on the 'add filter' button
    add_filter = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='filter-box-data']/div[1]/div[1]/div[1]/div[1]/button[1]"))
    )
    add_filter.click()
    update_report("User is able to click on the add filter button")

    # Sleep for 2 seconds
    time.sleep(2)

    # Search for a column you want to filter
    filter_column = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search a column']"))
    )

    filter_column.click()
    filter_column.send_keys("Full Name")
    update_report("User is able to search for the full name column in the internal filters")

    # wait for the list to be visible and select full name from the list options
    wait = WebDriverWait(driver, 10)
    list_element = wait.until(EC.visibility_of_element_located((By.ID, "column-list")))
    item_xpath = "//*[@id='column-list']/li[9]/label"
    item_element = list_element.find_element(By.XPATH, item_xpath)
    item_element.click()
    update_report("User is able to see and click on the full name column")

    # sleep for 2 seconds
    time.sleep(2)

    # clicking on the filter box text field and typing in the 'KCode' we wish to filter
    enter_full_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "k-textbox"))
    )
    enter_full_name.click()
    enter_full_name.send_keys("Eric Automation Test")
    update_report("User is able to enter persons full name")

    # sleep for 2 seconds
    time.sleep(2)

    # searching and clicking on the 'Filter' button
    filter_button_click = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "k-primary")))

    filter_button_click.click()
    update_report("User is able to see and click on the persons filter button")

    # sleep for 5 seconds
    time.sleep(5)

    # checking and tapping on the 'Delete' icon
    delete_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-entity-list/div/kendo-grid/div/kendo-grid-list/div[1]/div[1]/table/tbody/tr/td/span[1]/button"))
    )
    delete_button.click()
    update_report("User is able to see and click on the delete person button")

    # sleep for 2 seconds
    time.sleep(2)

    # checking if the cancel button is working
    cancel_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-entity-list/div/app-delete-entity/kendo-dialog/div[2]/kendo-dialog-actions/button[1]"))
    )
    cancel_button.click()
    update_report("User is able to click on the Cancel button")

    # sleep for 2 seconds
    time.sleep(2)

    # checking if the 'Yes' button is working well
    delete_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-entity-list/div/kendo-grid/div/kendo-grid-list/div[1]/div[1]/table/tbody/tr/td/span[1]/button"))
    )
    delete_button.click()
    update_report("User is able to see and click on the delete button")

    yes_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-entity-list/div/app-delete-entity/kendo-dialog/div[2]/kendo-dialog-actions/button[2]"))
    )
    yes_button.click()
    update_report("User is able to see and click on the 'Yes' button")

    # sleep for 2 seconds
    time.sleep(2)

    # ascertain that the test case passed
    print("Test case executed successfully")
    print("User not deleted due to dependency on Users table")
    print("Delete user from Users Table first : Run // Delete User // script")
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
