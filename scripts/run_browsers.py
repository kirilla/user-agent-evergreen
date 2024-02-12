from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_driver = webdriver.Chrome(options=chrome_options)
chrome_driver.get("http://localhost:8080/chrome")
print("Chrome Browser Title:", chrome_driver.title)
chrome_driver.quit()

# Edge
edge_options = webdriver.EdgeOptions()
edge_options.add_argument("--headless")
edge_driver = webdriver.Edge(options=edge_options)
edge_driver.get("http://localhost:8080/edge")
print("Edge Browser Title:", edge_driver.title)
edge_driver.quit()

# Firefox
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--headless")
firefox_driver = webdriver.Firefox(options=firefox_options)
firefox_driver.get("http://localhost:8080/firefox")
print("Firefox Browser Title:", firefox_driver.title)
firefox_driver.quit()

