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
service_object = Service(
    'C:\\Users\\alfred.matongo_komaz\\PycharmProjects\\Kwingu_Automation\\Browsers\\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

# Maximize the browser window
driver.maximize_window()

# Create a Tkinter window
window = Tk()
window.title("Automated Test : Data Export Check")
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
    update_report("User is able to see and click on the sign in button")

    # wait for the FOPs_dashboard to load
    dashboard_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='module-header']")))

    # sleep for 5 secs
    time.sleep(5)

    # check that we are on the dashboard page
    assert dashboard_header.is_displayed
    update_report("User is able to see that the FOPs dashboard has successfully loaded ")

    # check that the FOPs_dashboard page has the 'Hamburger Menu' icon
    hamburger_menu_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "menu-bar-close"))
    )

    # Clicking on the 'Hamburger Menu" icon
    hamburger_menu_icon.click()
    update_report("User is able to open the side navigation menu")

    # Sleep for 5 secs
    time.sleep(5)

    # Find and select 'activities' module from the main menu navigation
    zones_module_select = driver.find_element(By.XPATH,
                                              "//body/app-root/app-header/header/section/section/div/div/ul/li[8]")
    zones_module_select.click()
    update_report("User is able to select the zones module from the side navigation menu")

    # Sleep for 3 secs
    time.sleep(3)

    # close the sidebar navigation menu
    close_side_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "menu-bar-open"))
    )
    close_side_menu.click()
    update_report("User is able to close the side navigation menu")

    # sleep for 3 seconds
    time.sleep(3)

    # assert that were are on the zones table
    zones_page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "module-header"))
    )
    assert zones_page.is_displayed()
    update_report("User is able to see that the zones table has successfully loaded")

    # look for the filter button and click on it
    filter_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "filter-class-icon"))
    )
    filter_button.click()
    update_report("User is able to see and click on the filter button")

    # sleep for 3 seconds
    time.sleep(3)

    # Checking the 'internal filters'
    # clicking on the add filter button
    add_filter_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-zone-list/div[1]/kendo-grid/kendo-grid-toolbar/app-show-filter/div[1]/div/div/div/div/div/button"))
    )
    add_filter_button.click()
    update_report("User is able to see and click on the add filter button")

    # sleep for 3 seconds
    time.sleep(3)

    # search for the 'Zone Code' column on the popup window
    kcode_search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-column"))
    )
    kcode_search.click()
    kcode_search.send_keys("Zone Code")
    update_report("User is able to see and search for the zone column")

    # sleep for 3 seconds
    time.sleep(3)

    # select and clicking on the zone code option from the list
    wait = WebDriverWait(driver, 10)
    list_element = wait.until(EC.visibility_of_element_located((By.ID, "column-list")))
    item_xpath = "//body/app-root/app-zone-list/div[1]/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[1]/ul/li[2]/label"
    item_element = list_element.find_element(By.XPATH, item_xpath)
    item_element.click()
    update_report("User is able to select the zone column from the list ")

    # wait for 3 seconds
    time.sleep(3)

    # entering the zone code we want to filter
    filter_box_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-zone-list/div[1]/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/app-external-row-filter/div/input")
                                       ))
    filter_box_input.click()
    filter_box_input.send_keys("test")
    update_report("User is able to enter the zone to filter on the search box ")

    # sleep for 3 seconds
    time.sleep(3)

    # checking and clicking the 'filter' button
    filter_button_two = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-zone-list/div[1]/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/app-external-row-filter/div/div/button[2]"))
    )
    filter_button_two.click()
    update_report("User is able to see and click on the filter button")

    # sleep for 5 seconds
    time.sleep(5)

    # clicking on the export button
    export_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-zone-list/div[1]/kendo-grid/kendo-grid-toolbar/div/button[2]"))
    )
    export_button.click()
    update_report("User is able to see and click on the data export button")

    # sleep for 3 secs
    time.sleep(3)

    # checking if the export data pop up has been displayed
    pop_up_check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-zone-list/app-export-grid/kendo-dialog/div[2]/kendo-dialog-titlebar/div[1]"))
    )
    assert pop_up_check.is_displayed()
    update_report("User is able to see that the data export pop up is displayed ")

    # entering the name for the data we just downloaded
    edit_export = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-zone-list/app-export-grid/kendo-dialog/div[2]/div/p/span/input"))
    )
    edit_export.click()
    edit_export.send_keys("Zone Test Data")
    update_report("User is able to name the csv file of the data to export ")

    # sleep for 3 secs
    time.sleep(3)

    # clicking on the 'Save' button
    save_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-zone-list/app-export-grid/kendo-dialog/div[2]/kendo-dialog-actions/button[2]"))
    )
    save_button.click()
    update_report("User is able to see and click on the save button")

    # sleep for 3 secs
    time.sleep(3)

    # Test report
    print("Test executed successfully!!!")

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
