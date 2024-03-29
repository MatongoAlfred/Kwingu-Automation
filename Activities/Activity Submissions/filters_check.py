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
    update_report("User is able to see and click on the sign in button ")

    # wait for the FOPs_dashboard to load
    dashboard_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='module-header']")))

    # sleep for 5 secs
    time.sleep(5)

    # check that we are on the dashboard page
    assert dashboard_header.is_displayed
    update_report("User is able to see that the FOPs dashboard has successfully loadec ")

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
    activities_module_select = driver.find_element(By.XPATH,
                                                   "//body/app-root/app-header/header/section/section/div/div/ul/li[5]/div/span")
    activities_module_select.click()
    update_report("User is able to select the activities module from the side navigation menu")

    # Sleep for 3 secs
    time.sleep(3)

    # select activities submission option
    activities_submission = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-header/header/section/section/div/div/ul/li[5]/div[2]/li[2]/a")
        ))
    activities_submission.click()
    update_report("User is able to see and select the activities submissions sub module from the menu ")

    # sleep for 5 seconds
    time.sleep(5)

    # checking and clicking on the filters button
    filter_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/div/button[2]"))
    )
    filter_button.click()
    update_report("User is able to see and click on the main filter button on the header")

    # sleep for 3 secs
    time.sleep(3)

    # checking and clicking on the 'add filter' button
    add_filter = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[1]/div/div/div/div/div/button"))
    )
    add_filter.click()
    update_report("User is able to see and select the add filter button on the internal filters")

    # sleep for 3 secs
    time.sleep(3)

    # search for the 'shamba kcode' column on the popup window
    kcode_search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "input-column"))
    )
    kcode_search.click()
    kcode_search.send_keys("shamba kcode")
    update_report("User is able to click and search the shamba kcode column on the search box ")

    # sleep for 3 seconds
    time.sleep(3)

    # select and clicking on the shamba kcode option from the list
    wait = WebDriverWait(driver, 10)
    list_element = wait.until(EC.visibility_of_element_located((By.ID, "column-list")))
    item_xpath = "//*[@id='column-list']/li[2]/label"
    item_element = list_element.find_element(By.XPATH, item_xpath)
    item_element.click()
    update_report("User is able to select the shamba kcode column from the list of columns")

    # wait for 3 seconds
    time.sleep(3)

    # entering the kcode we want to filter
    filter_box_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/app-external-row-filter/div/input")
                                       ))
    filter_box_input.click()
    filter_box_input.send_keys("kwl-2023-0159")
    update_report("User is able to enter the kcode in the search box ")

    # sleep for 3 seconds
    time.sleep(3)

    # checking and clicking the 'filter' button
    filter_button_two = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-activity-list/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[2]/app-external-row-filter/div/div/button[2]"))
    )
    filter_button_two.click()
    update_report("User is able to see and click on the filter button on the internal filters pop up window ")

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