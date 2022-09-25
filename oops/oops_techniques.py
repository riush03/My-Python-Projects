from Address import Adress

class Student:
    first_name:str
    last_name:str
    gender:str
    age:int
    adress:Adress

    adress = Adress()
    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self,s_first_name):
        self._first_name = s_first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, s_first_name):
        self._first_name = s_first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, s_first_name):
        self._first_name = s_first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, s_first_name):
        self._first_name = s_first_name