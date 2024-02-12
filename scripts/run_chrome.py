from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_driver = webdriver.Chrome(options=chrome_options)
chrome_driver.get("http://localhost:8080/chrome")
print("Chrome Browser Title:", chrome_driver.title)
chrome_driver.quit()

