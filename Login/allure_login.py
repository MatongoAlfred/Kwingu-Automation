import subprocess

# Install required libraries
subprocess.run(["pip", "install", "allure-pytest", "selenium"])

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome web driver
service_object = webdriver.chrome.service.Service(
    'C:\\Users\\alfred.matongo_komaz\\PycharmProjects\\Kwingu_Automation\\Browsers\\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

# Maximize the browser window
driver.maximize_window()

# Function to update the report using Allure annotations
def update_report(message):
    allure.attach(message, name="Test Step")

try:
    # navigate to Kwingu login page
    driver.get("https://uatkwingu.komaza.com/login")
    update_report("Test Results: User is able to navigate to Kwingu login page")

    # sleep for 3 seconds
    time.sleep(3)

    # wait for the username and password fields to be visible
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

    # sleep for 3 seconds
    time.sleep(3)

    # tap the Sign_In button
    submit_button = driver.find_element(By.CLASS_NAME, "login-button")
    submit_button.click()
    update_report("User is able to see and click the 'Login' button")

    # wait for the FOPs_dashboard to load
    dashboard_header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='module-header']")))

    # check that we are on the dashboard page
    assert dashboard_header.is_displayed
    update_report("User is able to see the FOPs Dashboard load successfully")

    # sleep for 5 seconds
    time.sleep(5)

    # ascertain that the testcase was successfully executed
    print("Login testcase executed successfully")

except Exception as e:
    update_report("Error: " + str(e))
    raise e

finally:
    # Close the browser window
    driver.quit()

# Function to generate Allure report
def generate_allure_report():
    allure_cmd = 'allure generate ./allure-results -o ./allure-report'
    subprocess.run(allure_cmd, shell=True)

# Run tests using Pytest and generate Allure report
if __name__ == "__main__":
    pytest.main(['-s', '-v', '--alluredir', 'allure-results'])
    generate_allure_report()
