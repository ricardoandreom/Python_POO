# static methods e class methods
class myClass:
    count=0
    def __init__(self,x):
        self.x = x

    # Notice staticMethod does not require the self parameter
    @staticmethod
    def staticMethod():
        return "i am a static method"

    @classmethod
    def classMethod(cls):
        cls.count += 1
        return cls.count+3
    # The classMethod can access and modify class variables. It takes the class name as a required parameter

print(myClass.staticMethod())
print(myClass.classMethod())