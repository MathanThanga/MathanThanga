# update_naukri_profile.py
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Load credentials and new name from environment variables
USERNAME = os.getenv("NAUKRI_USERNAME")
PASSWORD = os.getenv("NAUKRI_PASSWORD")
NEW_NAME = os.getenv("Thangamailraj")

if not USERNAME or not PASSWORD or not NEW_NAME:
    print("Missing required environment variables: NAUKRI_USERNAME, NAUKRI_PASSWORD, NEW_DISPLAY_NAME", file=sys.stderr)
    sys.exit(1)

# Setup Chrome options for headless mode
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920,1080")

# Start driver
driver = webdriver.Chrome(options=options)

try:
    # Step 1: Go to login page
    driver.get("https://www.naukri.com/nlogin/login")
    time.sleep(3)  # Wait for page to load

    # Step 2: Enter username
    username_input = driver.find_element(By.ID, "usernameField")
    username_input.clear()
    username_input.send_keys(USERNAME)

    # Step 3: Enter password
    password_input = driver.find_element(By.ID, "passwordField")
    password_input.clear()
    password_input.send_keys(PASSWORD)

    # Step 4: Click login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    time.sleep(5)  # Wait for login and redirect

    # Step 5: Navigate to profile edit page
    driver.get("https://www.naukri.com/mnjuser/profile")  # Adjust if needed
    time.sleep(5)

    # Step 6: Find the name input field and update it
    # Inspect and replace selector if needed
    name_field = driver.find_element(By.ID, "name")  # Update selector if different
    name_field.clear()
    name_field.send_keys(NEW_NAME)

    # Step 7: Save changes
    save_button = driver.find_element(By.XPATH, "//button[contains(text(),'Save')]")
    save_button.click()

    time.sleep(5)  # Wait for save to complete

    print("Profile updated successfully.")

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(2)

finally:
    driver.quit()
