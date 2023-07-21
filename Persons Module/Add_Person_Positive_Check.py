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
window.title("Automated Test : Add Person Positive Check")
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
    update_report("User is able to enter a password")

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

    # clicking on the 'Hamburger Menu' icon
    hamburger_menu_icon.click()
    update_report("User is able to open the side navigation menu")

    # Sleep for 2 secs
    time.sleep(2)

    # find and select 'Persons' module from the main menu navigation
    shamba_module_select = driver.find_element(By.XPATH, '//*[@id="menu-navigation"]/ul/li[3]')
    shamba_module_select.click()
    update_report("User is able to select the 'Persons' module from the side navigation menu")

    # sleep for 2 secs
    time.sleep(2)

    # wait for the 'Persons Table' to load
    persons_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "module-header")))

    # Check that we are on the 'Persons Table' page
    assert persons_header.is_displayed
    update_report("User is able to see that the 'Persons table' has fully load")

    # closing the sidebar main navigation menu
    hamburger_menu_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "menu-bar-open"))
    )
    hamburger_menu_icon.click()

    # sleep for 3 secs
    time.sleep(3)

    # Checking and clicking on the 'Add Entity' button
    export_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-entity-list/div/kendo-grid/kendo-grid-toolbar/div/button[3]"))
    )
    export_button.click()
    update_report("User is able to see and click on the 'Add Entity' button")

    # sleep for 2 seconds
    time.sleep(2)

    # adding person's first name details
    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[1]/div/input"))
    )
    first_name.click()
    first_name.send_keys("Alfred")
    update_report("User is able to 'persons' first name")

    # adding the middle name
    middle_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[2]/div/input"))
    )
    middle_name.click()
    middle_name.send_keys("Automation")
    update_report("User is able to add 'persons' middle name")

    # adding the last name
    last_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[3]/div/input"))
    )
    last_name.click()
    last_name.send_keys("Test")
    update_report("User is able to add 'persons' last name")

    # adding the Employee ID
    employee_ID = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[5]/div/input"))
    )
    employee_ID.click()
    employee_ID.send_keys("444422222233")
    update_report("User is able to add Employee ID")

    # sleep for 2 seconds
    time.sleep(2)

    # add the Employee National ID
    national_ID = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[6]/div/input"))
    )
    national_ID.click()
    national_ID.send_keys("444422222233")
    update_report("User is able to add National ID")

    # sleep for 2 seconds
    time.sleep(2)

    # selecting the FA Role
    role_select = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[7]/span/kendo-combobox/span/kendo-searchbar/input"))
    )
    role_select.click()
    role_select.send_keys("Field Facilitator")
    role_select.send_keys(Keys.ENTER)
    update_report("User is able to select FEN role as Field Facilitator")

    # sleep for 2 seconds
    time.sleep(2)

    # adding FA Phone number
    fa_number = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[9]/div/input"))
    )
    fa_number.click()
    fa_number.send_keys("0711223344")
    update_report("User is able to add FEN's phone number")

    # sleep for 2 seconds
    time.sleep(2)

    # selecting the Country Code
    code_select = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[10]/div/span/kendo-combobox/span/kendo-searchbar/input"))
    )
    code_select.click()
    code_select.send_keys("254")
    code_select.send_keys(Keys.ENTER)
    update_report("User is able to select FEN's country code")

    # sleep for 2 seconds
    time.sleep(2)

    # selecting the active status
    status_check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[15]/span[2]/div[1]/label"))
    )
    status_check.click()
    update_report("User is able to change FEN active status to 'Yes'")

    # sleep for 2 seconds
    time.sleep(2)

    # selecting the represents organisation check box
    rep_check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[14]/span[2]/div[1]/label"))
    )
    rep_check.click()
    update_report("User is able to update that the FA represents the organisation")

    # sleep for 2 seconds
    time.sleep(2)

    # represents active  status selection
    rep_status_check = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-person-add-edit/div/div/div[2]/div[2]/fieldset/div/form/div[16]/span/kendo-combobox/span/kendo-searchbar/input"))
    )
    rep_status_check.click()
    rep_status_check.send_keys("Active")
    rep_status_check.send_keys(Keys.ENTER)
    update_report("User is able to update the FA's status to 'Active'")

    # sleep for 3 seconds
    time.sleep(3)

    # tapping the save button
    save_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-person-add-edit/div/div/div[2]/div[1]/div[3]/button[2]"))
    )
    save_button.click()
    update_report("User is able to see and click on the 'Save' button")

    # sleep for 3 seconds
    time.sleep(3)

    # selecting 'YES' on the confirmation pop up
    pop_up_yes = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-person-add-edit/kendo-dialog/div[2]/kendo-dialog-actions/button[2]"))
    )
    pop_up_yes.click()
    update_report("User is able to see and click on the 'YES' button on the confirmation pop up")

    # sleep for 3 seconds
    time.sleep(3)

    # Ascertain that the test case passed
    print("Test Case Executed successfully")

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
