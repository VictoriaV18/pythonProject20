class Dessert:
    def __init__(self, name = '', calories=0):
        self._name = name
        self._calories = calories
    @property
    def name(self):
        return self._name
    @name.setter

    def name(self, value):
        self._name = value

    @property
    def calories(self):
        return self._calories
    @calories.setter
    def calories(self, value):
        self._calories = value
    def is_healthy(self):
        return self.calories < 200


    def is_delicious(self):
        return True

dessert1 =Dessert('apple pie', 250)
print(dessert1.is_healthy())
print(dessert1.is_delicious())
dessert2 = Dessert('mango dessert', 120)
print(dessert2.is_healthy())
print(dessert2.is_delicious())