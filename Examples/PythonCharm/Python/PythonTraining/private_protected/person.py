class person():
    def __init__(self,first_name,last_name,age):
        self.f_name = first_name
        self.__l_name = last_name    #private
        self._age = age              #protected

