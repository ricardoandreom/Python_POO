# overriding methods

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y
        print(self.x,self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return "Point(" + str(self.x) + ',' + str(self.y) + ")"

    def length(self):
        import math

        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __gt__(self, other):  # greater than
        return self.length() > other.length()

    def __ge__(self, other):  # greater than or equal to
        return self.length() >= other.length()

    def __lt__(self, other):  # less than
        return self.length() < other.length()

    def __le__(self, other):  # less than or equal to
        return self.length() <= other.length()

p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)

# Now we can compare points using ==

isSame = p1 == p2 # or isSame = p1.x == p2.x and p1.y == p2.y
print(isSame) # Prints False

p5 = p1 + p2
print(p5)
p6 = p4 - p1
print(p6)
p7 = p2*p3
print(p7)
print(p1)

isLess = p1 <= p2  # This is False
print(isLess)

print(Point(2,2).move(1,2))
