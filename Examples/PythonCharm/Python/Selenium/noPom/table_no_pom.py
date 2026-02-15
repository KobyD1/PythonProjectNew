from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# create a new Firefox session
driver = webdriver.Chrome(executable_path="../driver/chromedriver100.exe")
#driver.implicitly_wait(30)
driver.maximize_window()

# Navigate to the application home page
driver.get("https://testpages.herokuapp.com/styled/tag/table.html")

# get the search textbox
table = driver.find_element_by_id("mytable")
rows = table.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
for row in rows:
    # Get the columns (all the column 2)
    cols = row.find_elements(By.TAG_NAME, "td")
    for col in cols:
      pattern = col.text
      print ("pattern found ",pattern)

driver.quit()