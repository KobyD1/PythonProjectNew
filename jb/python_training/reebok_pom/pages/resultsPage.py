

class ResultsPage:

    def __init__(self,page):
        self.page = page

    def get_text_from_results(self):
        elements = self.page.query_selector_all("[class='product__grid__title gt-p']")
        elements_short= elements[0:5]
        for element in elements_short:
            text = element.inner_text()
            print (text)
            assert "Shoes" in text
        # print ("test end")
