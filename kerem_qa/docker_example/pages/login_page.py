from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class loginPage():


    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)


    def click_on_login_button(self):
        print ("click_on_login_button")
        sale_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "SALE")))

        self.driver.find_element(By.ID,"login-button").click()



    def set_user_and_password(self,user_text, password_text):
        user = self.driver.find_element(By.ID,"user-name")
        user.clear()
        user.send_keys(user_text)
        password = self.driver.find_element(By.ID,"password")
        password.clear()
        password.send_keys(password_text)

