


class PlaywrightUtils:

    def is_button_clickable(self,element):
        try:
            element.click()
            return True


        except Exception as e:
            print(e)
            return False

    def is_button_exists(self,element):
        try:
            print ("try to click on element")
            element.click()
            return True
        except Exception as e:
            print(e)
            print ("element not found ")
            return False
