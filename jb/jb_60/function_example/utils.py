class utils:


    def getting_vat(self,price):
        print (f"Getting VAT for {price}")
        new_price = price.replace("$","")
        new_price_as_int = int(new_price)
        new_price_final = new_price_as_int * 1.18
        print(f"The final price is {new_price_final}")
        return new_price_final

    def add_suffix(self, price,rate):
        price = price*rate
        price_as_str= str(price)
        new_price = price_as_str+"ILS"
        print (f"the price is {new_price}")

    def avg_calc(self,nums):
        print ("calculate Avg. of numbers")
        sum =0
        for num in nums:
            print (num)
            sum = sum + num

        size = len(nums)
        avg = sum/size
        print (f"the avg value is {avg}")
        return avg , size



    def print_between_numbers(self,num1, num2):
        if (num1>num2):
            low = num2
            high= num1
        else:
            low = num1
            high = num2


        for num in range (low, high):
            print (num)


