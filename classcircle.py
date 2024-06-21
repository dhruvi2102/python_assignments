pi=3.14
class Circle:
    def area(self):
        r=float(input("Enter radius: "))
        area=pi*r*r
        print(area)

    def perimeter(self):
        r=float(input("Enter radius: "))  
        perimeter=2*pi*r
        print(perimeter)

obj=Circle()
obj.area()
obj.perimeter()        