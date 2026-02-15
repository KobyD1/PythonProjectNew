class vehicleParent():


    def price_calculator(self,price,tax,country_code="IL"):
        total_price = price * (100+tax)/100
        print (f"the total price is {total_price}")
        print (f"the country code  is {country_code}")

        return total_price