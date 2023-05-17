import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# set up the Chrome webdriver
driver = webdriver.Chrome()

# maximize the browser window
driver.maximize_window()

# navigate to the Kwingu login page
driver.get("https://uatkwingu.komaza.com/login")

# sleep for 2 seconds
time.sleep(2)

# locate 'Request a new password' text link
request_password_text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "request-password-link"))
)

# tapping on the 'Request a new password' text link
request_password_text.click()

# sleep for 2 seconds
time.sleep(2)

# wait for the 'Password Request' page to load
request_password_header_text = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "request-password-header-text")))

# check that we are on the 'Password Request' page
assert request_password_header_text.is_displayed

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

# sleep for 2 seconds
# enter the required information to request a new password
time.sleep(2)
official_id_field.send_keys("32752214")

# sleep for 3 secs
time.sleep(3)

# tab the 'Request a new password' button
request_new_password_button = driver.find_element(By.XPATH, "//button[@class='reset-password-button']")
request_new_password_button.click()

# sleep for 3 secs
time.sleep(3)

# wait for the 'Success' page to load
success_header_text = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, "success-msg-header")))

# check that we are on the 'Password Request' page
assert success_header_text.is_displayed

# sleep for 3 secs
time.sleep(3)

# ascertain that the 'Password Reset' testcase was successfully executed
print("Password Reset Testcase Passed Successfully")

# close the browser window
driver.quit()
