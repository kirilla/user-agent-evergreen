from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Edge
edge_options = webdriver.EdgeOptions()
edge_options.add_argument("--headless")
edge_options.use_chromium = True
edge_options.add_argument("--disable-blink-features=AutomationControlled")
edge_driver = webdriver.Edge(options=edge_options)
edge_driver.get("http://localhost:8080/edge")
print("Edge Browser Title:", edge_driver.title)
edge_driver.quit()
