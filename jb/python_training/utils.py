
class Utils_jb61:

    def age_calculator(self,age,ref_age=18):
        if age>ref_age:
            print(f"age is greater than {ref_age}")
            age_new =age+5
        else :
            print(f"age is less than {ref_age}")
            age_new =age-5

        return age_new

    def email_validator(self,email):
        print("trying to analyze if email is valid ")
        if "@" and "." in email:
            print ("email is valid")
            return True
        else:
            print ("email is not valid")
            return False

    def send_mails(self):
        print ("sending mails")

    def find_digits_summery(self,num):
        l=len(str(num))
        sum = 0
        if (l==3):
            for i in range (l):
                digit_as_str = str(num)[i]
                sum= sum+int(digit_as_str)
            print("3 digit number found")

            return sum




