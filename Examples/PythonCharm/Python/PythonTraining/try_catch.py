
try:
  print("try catch training")
  num1 = 10
  num2 = 0
  res = num1 /num2
# case of error
except ZeroDivisionError:
  print("Something went wrong")
  num2 = 1
  res = num1 / num2
# case of no error

# will be done anyway
finally:
  print("the value of rss is "+str(res))
#
# try:
#     elem = driver.find_element_by_xpath(".//*[@id='SORM_TB_ACTION0']")
#     elem.click()
# except NoSuchElementException:  #spelling error making this code not work as expected
#     pass




