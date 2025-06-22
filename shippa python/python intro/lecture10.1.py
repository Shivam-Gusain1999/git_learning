class cirlce:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
        
c2 = cirlce(21)
print(c2.area())
print(c2.perimeter())