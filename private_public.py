# Private and Public

# To declare something as private we use one underscore before the name.
class _Private:
    def __init__(self, name):
        self.name = name


class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)  # Even though we decalre something private we can still call and us it

    def _display(self):  # Private
        print("Hello")

    def display(self):  # Public
        print("Hi")