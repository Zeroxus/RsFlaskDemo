import numpy as np
import pandas as pd
from pandas import Series,DataFrame

class ISBN:
    def __init__(self):
        pass
        # pass

    def getISBN(self,booklist):
        with open('../Analyse/NUMBERS.txt', 'a+', encoding='UTF-8') as f:
            for book in booklist:
                print(book[1])
                f.write(book[1]+',\n')



    def getRates(self):
        pass

    def getCategory(self):
        pass