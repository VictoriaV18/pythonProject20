class Dessert:
    def __init__(self, name = '', calories=0):
        self._name = name
        self._calories = calories
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value,str):
            raise ValueError
        self._name = value

    @property
    def calories(self):
        return self._calories

    @calories.setter
    def calories(self, value):
        if not isinstance(value,(int, float)) or value < 0:
            raise ValueError
        self._calories = value

    def is_healthy(self):
        return self.calories < 200


    def is_delicious(self):
        return True


class JellyBean(Dessert):
    def __init__(self, name='', calories=0, flavor=''):
        super().__init__(name, calories)
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    def is_delicious(self):
        return self._flavor.lower() != 'black licorice'

jelly_bean1 = JellyBean('Jelly Bean', 160, 'black licorice')
print(jelly_bean1.is_delicious())