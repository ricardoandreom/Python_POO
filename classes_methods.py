# creating classes

# creating a new class of DOG
# lets add some methods
###################################################

class Dog0():
    def __init__(self): # constructor  # don't forget the self keyword
        print("Created a dog")

    def speak(self):
        pass

tim0 = Dog0()  # This will print "Created a dog" because __init__ will automatically be called

############################################################################################


class Dog1():
    def __init__(self, name,age): # add the argument name and age
        self.name = name  # self.name is now an attribute of the Dog class and has a specific value for each instance
        self.age = age
        self.li = [1,2,3]
    def speak(self):
        print('Hi,I am',self.name,"and I'm",self.age)

    def change_age(self,age): # the arguments after the atributes have to be on arguments class unless if it has to bem some fixe variable
        self.age = age


# creating instances of the class Dog1

tim1 = Dog1("Tim",55) # we are saying that tim1.name = "Tim" and tim1.age = 55
dog2 = Dog1("Fred",56)

tim1.speak()  # Prints "Tim"
dog2.speak() # Prints "Fred"

print(tim1.age) # returns us the age of tim as well
print(tim1.li)

#######################################################

class Dog3():
    def __init__(self, name,age): # add the argument name and age
        self.name = name  # self.name is now an attribute of the Dog class and has a specific value for each instance
        self.age = age
        self.li = [1,2,3]
    def speak(self):
        print('Hi,I am',self.name,"and I'm",self.age)

    def change_age(self,age): # the arguments after the atributes have to be on arguments class unless if it has to bem some fixe variable
        self.age = age

    # creating a new instance attribute to this Dog class
    def add_weight(self, weight):
        self.weight = weight

tim2 = Dog3("Tim",44)
tim2.add_weight(60)
print(tim2.weight)
tim2.change_age(23)
tim2.speak()

##################################################################

# final class Dog

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("I am", self.name, "and I am", self.age, "years old")

    def change_age(self, age):
        self.age = age  # This changes the age attribute

tim = Dog("Tim", 5)
tim.change_age(7)
tim.speak() # This will print "I am Tim and I am 7 years old"