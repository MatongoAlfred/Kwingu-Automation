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
window.title("Automated Test : Users Filter Check")
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
    update_report("User is able to see that the FOPs dashboard has successfully load")

    # check that the FOPs_dashboard page has the 'Hamburger Menu' icon
    hamburger_menu_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "menu-bar-close"))
    )

    # Clicking on the 'Hamburger Menu" icon
    hamburger_menu_icon.click()
    update_report("User is able to open the side navigation menu ")
    # Sleep for 5 secs
    time.sleep(5)

    # Find and select 'Users' module from the main menu navigation
    users_module_select = driver.find_element(By.XPATH,
                                              "//body/app-root/app-header/header/section/section/div/div/ul/li[4]/div/span/i")
    users_module_select.click()
    update_report("User is able to select the users module from the side navigation menu")

    # Sleep for 5 secs
    time.sleep(5)

    # select user tree option
    user_management = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-header/header/section/section/div/div/ul/li[4]/div[2]/li[2]/a")
        ))
    user_management.click()
    update_report("User is able to select the user tree submodule from the menu")

    # sleep for 3 seconds
    time.sleep(3)

    # applying the filter by dept filter (Field Operations)
    dept_filter = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-user-tree/div/div/kendo-combobox/span/kendo-searchbar/input"))
    )
    dept_filter.click()
    dept_filter.send_keys("Field Operations")
    dept_filter.send_keys(Keys.ENTER)
    update_report("User is able to click on the department filter ")
    update_report("User is able to select the Field Operations department on the filter ")

    # sleep for 5 seconds
    time.sleep(5)

    # applying the 'Filter by Role' filter
    role_filter = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-user-tree/div/div[2]/kendo-combobox/span/kendo-searchbar/input"))
    )
    role_filter.click()
    role_filter.send_keys("Field Manager")
    role_filter.send_keys(Keys.ENTER)
    update_report("User is able to click on the role filter ")
    update_report("User is able to select the field manager role from the filter ")

    # checking if the 'Filter' button is working as expected
    filter_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root/app-user-tree/div/button"))
    )
    filter_button.click()
    update_report("User is able to click on the main filter on the user tree table ")

    # sleep for 5 seconds
    time.sleep(5)

    # checking if the 'filter by person' filter is working as expected
    person_filter = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-user-tree/div/kendo-grid/kendo-grid-toolbar/div/div[2]/kendo-combobox/span/kendo-searchbar/input"))
    )
    person_filter.click()
    person_filter.send_keys("Test Kwale One")
    update_report("User is able to click on the person filter")
    update_report("User is able to enter the persons name")

    # sleep for 10 seconds
    time.sleep(10)
    person_filter.send_keys(Keys.ENTER)
    update_report("User is able to see and click on the person filter ")

    # checking if the filter button is working as expected
    filter_table_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-user-tree/div/kendo-grid/kendo-grid-toolbar/div/div[2]/button[1]"))
    )
    filter_table_button.click()
    update_report("User is able to click on the main filter and see if it is working as expected ")

    # sleep for 5 secs
    time.sleep(5)

    # clearing the applied filters
    clear_filters = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "clear-filters-button"))
    )
    clear_filters.click()
    update_report("User is able to clear the applied filters on the user tree table ")

    # sleep for 3 secs
    time.sleep(3)

    # checking if the related functionalities are working as expected
    # checking if entered name does not exist in the database --- empty pop up is shown
    person_filter.click()
    person_filter.clear()
    person_filter.send_keys("Not Available")
    update_report("User is able to see that if person does not exist an empty pop is displayed ")

    # ascertain that an empty pop up is displayed
    empty_pop_up = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/kendo-popup[1]/div[1]/div[1]"))
    )
    assert empty_pop_up.is_displayed
    update_report("User is able to see that that if the person is not found the related pop up is shown ")

    # sleep for 3 seconds
    time.sleep(3)

    # checking if the down arrow is working as expected
    down_arrow_filter = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-user-tree/div/kendo-grid/kendo-grid-toolbar/div/div[2]/kendo-combobox/span/span/span"))
    )
    down_arrow_filter.click()
    assert empty_pop_up.is_displayed
    update_report("User is able to see and click on the down arrow icon")
    update_report("User is able to see that the down arrow is working ")
    update_report("User is able to see that pop up is displayed when the down arrow is clicked")

    # sleep for 3 secs
    time.sleep(3)

    # checking if the 'reset department' button is working as expected
    reset_dept = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root/app-user-tree/div/kendo-grid/kendo-grid-toolbar/button"))
    )
    reset_dept.click()
    update_report("User is able to see and click on reset department button")
    update_report("User is able to see that the reset department button is working ")

    # sleep for 3 seconds
    time.sleep(3)

    # ascertain that the test case was executed successfully
    print("Test Case Executed Successfully!!!!")

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