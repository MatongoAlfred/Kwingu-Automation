import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import Tk, Text
from selenium.webdriver.chrome.service import Service

# set up the Chrome web-driver
service_object = Service('C:\\Users\\alfred.matongo_komaz\\PycharmProjects\\Kwingu_Automation\\Browsers\\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

# Maximize the browser window
driver.maximize_window()

# Create a Tkinter window
window = Tk()
window.title("Test Run Report")

# Create a Text widget to display the report
report_text = Text(window, height=10, width=50)
report_text.pack()

# Function to update the report
def update_report(message):
    report_text.insert("end", message + "\n")
    report_text.update()

try:
    # Navigate to Kwingu login page
    driver.get("https://uatkwingu.komaza.com/login")
    update_report("Navigated to Kwingu login page.")

    # Sleep for 3 seconds
    time.sleep(3)

    # Wait for the username and password fields to be visible
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Your username']"))
    )
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Your password']"))
    )

    # Enter the login credentials
    username_field.send_keys("32752214")
    password_field.send_keys("Alfredmat12#")
    update_report("Entered login credentials.")

    # Sleep for 3 seconds
    time.sleep(3)

    # Tab the Sign_In button
    submit_button = driver.find_element(By.CLASS_NAME, "login-button")
    submit_button.click()
    update_report("Clicked on Sign In button.")

    # Wait for the FOPs_dashboard to load
    dashboard_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='module-header']"))
    )

    # Check that we are on the dashboard page
    assert dashboard_header.is_displayed
    update_report("Logged in and reached the dashboard page.")

    # Sleep for 5 seconds
    time.sleep(5)

    # Ascertain that the test case was executed successfully
    update_report("Login testcase executed successfully.")

except Exception as e:
    update_report("Error: " + str(e))

finally:
    # Close the browser window
    driver.quit()
    update_report("Browser closed.")

# Start the Tkinter event loop
window.mainloop()