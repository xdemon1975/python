#!/usr/bin/python3

##strMyName = "xdemon"
##print(strMyName)
##
##nSecondNum = 20
##print(nSecondNum)
##
##print(12* 34)
##print(2**3)

##a = 20
##b = 20
##print(a > b)

##
##a = int(input("a="))
##b = int(input("b="))
##
##if a > b :
##    print("value=" + str(a))
##elif a < b :
##    print(b)
##else :
##    print("same value")
##
##while (a > 0) :
##    print(a, end = ' ')
##    a = a - 1

##for a in range(0, 12) :    
##    print(a, end = ' ')
##    
##print('')
##
##def add(a,b):
##    return a + b
##print(add(1,3))
##print(add("abc" , "def"))
##
##class C1:
##    a = 1
##
##print("c1 = ", C1.a)
##C1.b = 2
##
##x = C1()
##x.a=10
##print("c1 = ", x.a)


class SoJu:
    water = 0
    alchol = 0
    ingredient = 0
    volume = 0

td = SoJu()
td.water = 1
td.alchol = 99
td.ingredient = 1
td.volume = 3

tda = SoJu()
tda.water = 1
tda.alchol = 990
tda.ingredient = 1
tda.volume = 3

print(td.alchol)

print(tda.alchol)

print(hex(int('19',16)))


class Date :
    word = 'date : '

    def __init__(self, date):
        self.date = self.word + date
        
    @staticmethod    
    def now():
        return Date("today")

    @classmethod
    def now1(self1):
        return self1("today")

    def show(self):
        print (self.date)

class KoreanDate(Date):
    word = '날짜 : '


a = KoreanDate.now()
a.show()

b = KoreanDate.now1()
b.show()

print("aa" * 3)

l = ["a", "b", 4, 5]
print(l)

t = "a", "b", 4, 5
print(t)
print(t[1])











