class Test_Guru99():

    def test_set_flight(self,setup_playwright):
        page = setup_playwright
        page.goto("https://demo.guru99.com/test/newtours/reservation.php")
        page.locator("[value='oneway']").click()
        passengers= page.locator("[name='passCount']")
        passengers.select_option(index=2)
        airline= page.locator("[name='airline']")
        airline.select_option(index=1)
        print ("test end")




