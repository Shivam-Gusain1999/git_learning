class complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def shownumber(self):
     print(self.real,"i +", self.img,"j")

    def __add__(obj1, obj2):
        newreal = obj1.real + obj2.real
        newimg = obj1.img + obj2.img
        return complex(newreal, newimg)

num1 = complex(4, 7)    
num1.shownumber()

num2 = complex(8, 9)    
num2.shownumber()

num3 = num1 + num2
num3.shownumber()