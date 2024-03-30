class Circle:
    def __init__(self, radius):
        self._radius = radius

    # @property
    def get_radius(self):
        return self._radius

    # @radius.setter
    def set_radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value


circle = Circle(5)


print("Initial radius:", circle.get_radius())


try:
    circle.set_radius(-2)
except ValueError as e:
    print("Error:", e)


circle.radius = 10
print("Updated radius:", circle.get_radius())
