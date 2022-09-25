class Adress:
    streets:str
    city:str
    state:str
    zip_code:int

    @property
    def streets(self):
        return self._streets
    @streets.setter
    def streets(self,s_street):
        self._streets = str(s_street)
    @property
    def city(self):
        return self._city
    @city.setter
    def city(self,s_city):
        self._city = str(s_city)
    @property
    def state(self):
        return self._state
    @state.setter
    def state(self,s_state):
        self._state = s_state
    @property
    def zip_code(self):
        return self._zip_code
    @zip_code.setter
    def zip_code(self,s_zip_code):
        self._zip_code = s_zip_code