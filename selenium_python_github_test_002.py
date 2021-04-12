from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

###Test with wrong password given. "Incorrect username or password." is displayed over Signing in element of page.###
###time is used for  better visibility of actions###
###Used my own e-mail address###
driver = webdriver.Chrome("C:\chromedriver.exe")
driver.get("https://github.com/login")
###grab on username field and fill with e-mail address###
username_field = driver.find_element_by_id("login_field")
username_field.send_keys("Marc391@op.pl")
time.sleep(2)
###grab on password field and fill with password###
password_field = driver.find_element_by_id("password")
password_field.send_keys("wrongPassword")
time.sleep(2)
###grab on sign in button field and click on it###
sign_in_button = driver.find_element_by_name("commit")
sign_in_button.click()
time.sleep(2)
###Try to find element with "flash-error" class if there is no
# such element then log "FAIL" and if there is then log "PASS"###
try:
    driver.find_element_by_class_name("flash-error")
    print("PASS")
except:
    print("FAIL")
driver.close()