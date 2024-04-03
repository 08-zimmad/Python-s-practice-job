class Circle:
    def __init__(self, radius):
        self._radius = radius


    # for setter without decorator
    #replace radius with get_radius and remove property
    @property
    def radius(self):
        return self._radius


    # for setter without decorator
    #replace radius with set_radius and remove @radius.setter
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value


circle = Circle(5)


print("Initial radius:", circle.radius)


try:
    circle.set_radius=-2  # without decoratted getter/setter use instead: circle.set_radius(-2) 
except ValueError as e:
    print("Error:", e)


circle.radius = 10
print("Updated radius:", circle.radius) # without decoratted getter/setter use instead: circle.get_radius()
