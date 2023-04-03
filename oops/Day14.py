
'''
class varibale
'''

class Car:
    num_wheel = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model


car1 = Car("Toypta", "camrcy")
car2 = Car("honda", "civic")


print(car1.num_wheel)
print(car2.num_wheel)