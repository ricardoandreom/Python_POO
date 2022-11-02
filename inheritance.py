# Inheritance

# Example 1
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I am", self.name, "and I am", self.age, "years old")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)  # This will call the Animal classes constructor method
    '''self.name = name
        self.age = age
        self.type = "dog"''' # or we can use the previous 3 lines instead of the 1st two ones

tim = Dog("Tim", 5)
tim.speak() # This will print "I am Tim and I am 5 years old"

### Example 2
# realistic example of inheritance and where you may use it.
class Vehicle:
    def __init__(self, price, color):
        self.color = color
        self.price = price
        self.gas = 0

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas


class Truck(Vehicle):
    def __init__(self, price, color, tires):
        super().__init__(price, color)
        self.tires = tires

    def beep(self):
        print("Honk honk")


class Car(Vehicle):
    def __init__(self, price, color, speed):
        super().__init__(price, color)
        self.speed = speed

    def beep(self):
        print("Beep Beep")