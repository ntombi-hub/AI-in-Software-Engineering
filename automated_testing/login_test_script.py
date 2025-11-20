# login_test_script.py
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com/login")

# Valid credentials
driver.find_element(By.ID, "username").send_keys("user1")
driver.find_element(By.ID, "password").send_keys("pass123")
driver.find_element(By.ID, "login").click()

# Capture result
success_message = driver.find_element(By.ID, "success").text
print("Login Result:", success_message)

driver.quit()
