from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




driver = webdriver.Chrome(executable_path="../driver/chromedriver100.exe")
#driver.implicitly_wait(30)
driver.maximize_window()

driver.get("http://automationpractice.com/index.php")

text = driver.find_element_by_css_selector("files[class='search_query form-control ac_input']")
text.click()
text.send_keys("hat")

search = driver.find_element_by_css_selector("button[class='btn btn-default button-search']")
search.click()

results = driver.find_element_by_css_selector("span[class='lighter']")
results.text
driver.quit()