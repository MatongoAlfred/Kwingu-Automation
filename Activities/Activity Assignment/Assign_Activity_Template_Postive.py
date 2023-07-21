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
window.title("Automated Test : Assign Activity Template")
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
    update_report("User is able to enter the username ")
    update_report("User is able to enter the password")

    # tab the Sign_In button
    submit_button = driver.find_element(By.XPATH, "//button[@class='login-button']")
    submit_button.click()
    update_report("User is able to see and click on the submit button ")

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
    update_report("User is able to open the side navigation menu ")

    # Sleep for 5 secs
    time.sleep(5)

    # Find and select 'activities' module from the main menu navigation
    activities_module_select = driver.find_element(By.XPATH,
                                                   "//body/app-root/app-header/header/section/section/div/div/ul/li[5]/div/span")
    activities_module_select.click()
    update_report("User is able to see and select the activities module from the side navigation menu")

    # Sleep for 3 secs
    time.sleep(3)

    # select activities assignment option
    activities_assignment = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-header/header/section/section/div/div/ul/li[5]/div[2]/li[1]/a")
        ))
    activities_assignment.click()
    update_report("User is able to select the activities assignment sub module from the menu")

    # sleep for 5 seconds
    time.sleep(5)

    # close the sidebar navigation menu
    close_side_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "menu-bar-open"))
    )
    close_side_menu.click()
    update_report("User is able to close the side navigation menu ")

    # sleep for 3 seconds
    time.sleep(3)

    # assert that were are on the activities assignment page
    activity_assignmemt_page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "activity-ass-header"))
    )
    assert activity_assignmemt_page.is_displayed()
    update_report("User is able to see that the activity assignment table has successfully loaded ")

    # wait for the records to load for 10 seconds
    time.sleep(10)

    # checking the external filter if it works
    external_filter_tap = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "th#k-grid0-r0c2 > kendo-grid-filter-menu > a"))
    )
    external_filter_tap.click()
    update_report("User is able to click on the external filter button")

    # sleep for 3 seconds
    time.sleep(3)

    # entering the kcode
    text_input_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root[1]/kendo-popup[1]/div[1]/kendo-grid-filter-menu-container[1]/form[1]/div[1]/app-custom-row-filter[1]/div[1]/input[1]"))
    )
    text_input_box.click()
    text_input_box.send_keys("klf-2023-0037")
    update_report("User is able to enter the kcode into the search box of the external filter pop up window ")

    # sleep for 3 seconds
    time.sleep(3)

    # clicking on the filter button
    external_filter_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/kendo-popup/div/kendo-grid-filter-menu-container/form/div/app-custom-row-filter/div/div/button[2]"))
    )
    external_filter_button.click()
    update_report("User is able to see and click the filter button on the external filter  ")

    # sleep for 5 seconds
    time.sleep(5)

    # clicking on the command icon
    command_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root/app-activity-list/div/kendo-grid/div/kendo-grid-list/div[1]/div[1]/table/tbody/tr/td/label/span"))
    )
    command_icon.click()
    update_report("User is able to see and click on the command icon")

    # checking if the actions icon becomes active
    actions_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "profile-image")
                                       ))
    actions_button.click()
    update_report("User is able to see and click on the actions button on the header")

    # sleep for 3 seconds
    time.sleep(3)

    # selecting the assign activity template option from the list
    assign_activity_template = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='k-menu0-child0']/li[1]/span[1]/div[1]/span[1]"))
    )
    assign_activity_template.click()
    update_report("User is able to see and select the assign activity template option ")

    # sleep for 3 seconds
    time.sleep(3)

    # selecting the activity template
    select_template = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root/app-activity-list/kendo-dialog/div[2]/div/div/kendo-combobox/span/kendo-searchbar/input"))
    )
    select_template.click()
    select_template.send_keys("Planting")
    select_template.send_keys(Keys.ENTER)
    update_report("User is able to see and select the required template to assign ")
    update_report("User is able to successfully assign an activity template")

    # select the desired date from the calendar
    #desired_date = '20' # set the desired date as a string
    #day_locator = (By.XPATH, f'//div[@class="day" and text()="{desired_date}"]')
    #wait = WebDriverWait(driver, 10) # set maximum wait time for the element to appear
    #day_element = wait.until(EC.element_to_be_clickable(day_locator))
    #day_element.click()

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
