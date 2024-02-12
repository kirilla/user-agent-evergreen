from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Firefox
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")
firefox_options.add_argument("--marionette")
firefox_options.add_argument("--disable-blink-features=AutomationControlled")
firefox_driver = webdriver.Firefox(options=firefox_options)
firefox_driver.get("http://localhost:8080/firefox")
print("Firefox Browser Title:", firefox_driver.title)
firefox_driver.quit()
