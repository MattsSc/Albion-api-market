class ItemPriceEvaluated:
    def __init__(self, name = None):
        self.name = name
        self.caerleon = None
        self.city = None
        self.bestPrice = 0

    @property
    def name(self): 
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def caerleon(self):
        return self._caerleon

    @caerleon.setter
    def caerleon(self, caerleon):
        self._caerleon = caerleon

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        self._city = city

    @property
    def bestPrice(self):
        return self._bestPrice

    @bestPrice.setter
    def bestPrice(self, bestPrice):
        self._bestPrice = bestPrice


    def getProfit(self):
        return self._caerleon - (self._bestPrice * 1.04)



    def __str__(self):
        return f"ITEM: {self.name} , CAERLEON PRICE: {self.caerleon}, BEST CITY TO BUY {self.city} AT {self.bestPrice} .... AVG PROFIT: {self.getProfit()}"