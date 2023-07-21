import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from tkinter import Tk, Text

# Set up the Chrome web driver
service_object = Service(
    'C:\\Users\\alfred.matongo_komaz\\PycharmProjects\\Kwingu_Automation\\Browsers\\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

# maximize the browser window
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

    # sleep for 2 seconds
    time.sleep(2)

    # locate 'Request a new password' text link
    request_password_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "request-password-link"))
    )

    # tapping on the 'Request a new password' text link
    request_password_text.click()
    update_report("User is able to see and click on the 'request a new password' link")

    # sleep for 2 seconds
    time.sleep(2)

    # wait for the 'Password Request' page to load
    request_password_header_text = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "request-password-header-text"))
    )

    # check that we are on the 'Password Request' page
    assert request_password_header_text.is_displayed
    update_report("User is able to navigate to 'Password request' page")

    # wait for the 'Employee ID' and 'Official ID Number' fields to load
    employee_id_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Your Employee ID']"))
    )
    official_id_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Your Official ID Number']"))
    )

    # sleep for 3 seconds
    time.sleep(3)

    # enter the required information to request a new password
    employee_id_field.send_keys("32752214")
    update_report("User is able to enter the Employee ID")

    # sleep for 2 seconds
    time.sleep(2)
    official_id_field.send_keys("32752214")
    update_report("User is able to Official ID number")

    # sleep for 3 seconds
    time.sleep(3)

    # tap the 'Request a new password' button
    request_new_password_button = driver.find_element(By.XPATH, "//button[@class='reset-password-button']")
    request_new_password_button.click()
    update_report("User is able to see and click on the 'Request a new password' button")

    # sleep for 3 seconds
    time.sleep(3)

    # wait for the 'Success' page to load
    success_header_text = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "success-msg-header"))
    )

    # check that we are on the 'Password Request' page
    assert success_header_text.is_displayed
    update_report("User is able to see that they have successfully reset their Kwingu password")

    # sleep for 3 seconds
    time.sleep(3)

    # ascertain that the 'Password Reset' testcase was successfully executed
    print("Password Reset Testcase Passed Successfully")

    # close the browser window
    driver.quit()

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
