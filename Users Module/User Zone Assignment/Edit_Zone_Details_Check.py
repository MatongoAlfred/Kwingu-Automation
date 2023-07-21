import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from tkinter import Tk, Text
from selenium.webdriver.common.keys import Keys

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
    update_report("User is able to the password")

    # tab the Sign_In button
    submit_button = driver.find_element(By.XPATH, "//button[@class='login-button']")
    submit_button.click()
    update_report("User is able to see and click on the sign in button")

    # wait for the FOPs_dashboard to load
    dashboard_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='module-header']"))
    )

    # sleep for 5 secs
    time.sleep(5)

    # check that we are on the dashboard page
    assert dashboard_header.is_displayed
    update_report("User is able to see that the FOPs dashboard has loaded successfully ")

    # check that the FOPs_dashboard page has the 'Hamburger Menu' icon
    hamburger_menu_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "menu-bar-close"))
    )

    # Clicking on the 'Hamburger Menu' icon
    hamburger_menu_icon.click()
    update_report("User is able to open the side navigation ")

    # Sleep for 5 secs
    time.sleep(5)

    # Find and select 'Users' module from the main menu navigation
    users_module_select = driver.find_element(By.XPATH,
                                              "//body/app-root/app-header/header/section/section/div/div/ul/li[4]/div/span/i")
    users_module_select.click()
    update_report("User is able to select the users module from the side navigation menu ")

    # Sleep for 5 secs
    time.sleep(5)

    # select user zone assignment option
    user_management = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-header/header/section/section/div/div/ul/li[4]/div[2]/li[3]")
        ))
    user_management.click()
    update_report("User is able to select the user zone assignment option ")

    # sleep for 3 seconds
    time.sleep(3)

    # clicking on the filter icon
    filter_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//body/app-root/app-zone-assignment/div/kendo-grid/kendo-grid-toolbar/div/div/button"))
    )
    filter_icon.click()
    update_report("User is able to click on the main filter icon ")

    # sleep for 5 seconds
    time.sleep(5)

    # clicking on the add filter button
    add_filter_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//body/app-root/app-zone-assignment/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[1]/div/div/div/div/div/button"))
    )
    add_filter_button.click()
    update_report("User is able to see and click on add filter button ")

    # sleep for 3 seconds
    time.sleep(3)

    # entering the 'zone' column name on the search bar
    edit_column = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root/app-zone-assignment/div/kendo-grid/kendo-grid-toolbar/app-show-filter/div[2]/app-showfilters/div/kendo-popup/div/div/div[1]/div/input"))
    )
    edit_column.click()
    edit_column.send_keys("Zone")
    update_report("User is able to see the search box and be able to type in the column they want")

    # wait for the list to be visible and select zone from the list options
    wait = WebDriverWait(driver, 10)
    list_element = wait.until(EC.visibility_of_element_located((By.ID, "column-list")))
    item_xpath = "//*[@id='column-list']/li[2]/label[1]"
    item_element = list_element.find_element(By.XPATH, item_xpath)
    item_element.click()
    update_report("User is able to select the zone column from the internal filters pop up window ")

    # sleep for 3 seconds
    time.sleep(3)

    # clicking on the filter box text field and typing in the 'zone' we wish to filter
    enter_zone_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "k-textbox"))
    )
    enter_zone_name.click()
    enter_zone_name.send_keys("kwale county")
    update_report("User is able to enter the zone name in the zone filter ")

    # sleep for 5 seconds
    time.sleep(5)

    # searching and clicking on the 'Filter' button
    filter_button_click = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "k-primary")))

    filter_button_click.click()
    update_report("User is able to see and click the filter button on the filter pop up window")

    # sleep for 5 seconds
    time.sleep(5)

    # clicking on the zone edit icon
    edit_zone = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root/app-zone-assignment/div/kendo-grid/div/kendo-grid-list/div[1]/div[1]/table/tbody/tr[1]/td/span[1]/button"))
    )
    edit_zone.click()
    update_report("User is able to see and click the edit zone icon")

    # sleep for 3 secs
    time.sleep(5)

    # checking if the zone edit pop up is displayed
    zone_pop_up = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root/app-zone-assignment/kendo-dialog/div[2]/kendo-dialog-titlebar/div[1]"))
    )
    zone_pop_up.click()
    update_report("User is able to see that the zone edit pop up has been displayed")

    # sleep for 5 secs
    time.sleep(5)

    # editing the zone details
    re_assign_FA = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root/app-zone-assignment/kendo-dialog/div[2]/div/div/div/div[1]/span/kendo-combobox/span/kendo-searchbar/input"))
    )
    re_assign_FA.clear()
    re_assign_FA.send_keys("Test FA Agwata")
    re_assign_FA.send_keys(Keys.ENTER)
    update_report("User is able to successfully assign FA to a zone")

    # sleep for 3 secs
    time.sleep(3)

    # clicking the 'Assign button'
    assign_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//body/app-root[1]/app-zone-assignment[1]/kendo-dialog[1]/div[2]/kendo-dialog-actions[1]/button[1]"))
    )
    assign_button.click()
    update_report("User is able to see and click on the 'Assign Person' button")

    # sleep for 3 secs
    time.sleep(3)

    # Assert that the test case is passed
    print("Test Case Executed Successfully!!!")

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
