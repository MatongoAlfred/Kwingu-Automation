import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# set up the Chrome web-driver
service_object = Service('C:\\Users\\alfred.matongo_komaz\\PycharmProjects\\Kwingu_Automation\\Browsers\\chromedriver.exe')
driver = webdriver.Chrome(service=service_object)

# maximize the browser window
driver.maximize_window()

# navigate to Kwingu login page
driver.get("https://uatkwingu.komaza.com/login")

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

# sleep for 3 seconds
time.sleep(3)

# tap the Sign_In button
submit_button = driver.find_element(By.CLASS_NAME, "login-button")
submit_button.click()

# wait for the FOPs_dashboard to load
dashboard_header = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[@class='module-header']")))

# check that we are on the dashboard page
assert dashboard_header.is_displayed

# sleep for 5 seconds
time.sleep(5)

# ascertain that the testcase was successfully executed
print("Login testcase executed successfully")

# close the browser window
driver.quit()