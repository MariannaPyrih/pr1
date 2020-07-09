class Goods():
    def __init__(self, model, price, year):
        self.model = model
        self.price = price
        self.year = year

    def print(self):
        print(self.__class__.__name__)
        print('Model: ', self.model)
        print('Price: ', self.price)
        print('Year: ', self.year)

class TV(Goods):
    def __init__(self, model, price, year, dia, matrix):
        Goods.__init__(self, model, price, year)
        self.model = model
        self.price = price
        self.year = year
        self.dia = dia
        self.matrix = matrix
    def print(self):
        super().print()
        print('Dia ecran: ', self.dia)
        print('Matrix tv: ', self.matrix)
        print('__________________')
        
class Phone(Goods):
    def __init__(self, os, count_camera, model, price, year):
        Goods.__init__(self, model, price, year)
        self.os = os
        self.count_camera = count_camera
    def print(self):
        super().print()
        print('Os: ', self.os)
        print('Count_camera: ', self.count_camera)
        print('_________________')

class LapTope(Goods):
    def __init__(self, dia, processor, model, price, year):
        Goods.__init__(self, model, price, year)
        self.dia = dia
        self.processor = processor
    def print(self):
        super().print()
        print('Diagonal ecran is: ', self.dia)
        print('Type of processor is: ', self.processor)
        print('_________________')

 

tv = TV ('a123', 12000, 2016, 34, 'b123')
ph = Phone ('android', 2, 'zte blade', 6000, 2017)
lp = LapTope(15, 14000, 'Asus', 'Intel', 2018)
tv.print()
ph.print()
lp.print()
