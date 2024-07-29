```python
"""
*References:
http://en.wikibooks.org/wiki/Computer_Science_Design_Patterns/Bridge_Pattern#Python

*TL;DR
Decouples an abstraction from its implementation.
"""

# ConcreteImplementor 1/2
class DrawingAPI1:
    def draw_circle(self, x, y, radius):
        print(f"API1.circle at {x}:{y} radius {radius}")

    def __repr__(self):
        return f"{self.__class__.__name__}()"


# ConcreteImplementor 2/2
class DrawingAPI2:
    def draw_circle(self, x, y, radius):
        print(f"API2.circle at {x}:{y} radius {radius}")

    def __repr__(self):
        return f"{self.__class__.__name__}()"


# Refined Abstraction
class CircleShape:
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, pct):
        self._radius *= pct

    def another_public_method(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}()"


class Dog:
    def bark(self):
        """Make the dog bark."""

    def speak(self) -> str:
        """Returns a string representing the speaking sound."""


class Cat:
    """Class representing a cat."""
    
    def meow(self):
        """Produces a meowing sound."""

    def speak(self) -> str:
        """Returns a string representing the speaking sound."""


class Human:
    """A class representing a human."""

    def speak(self) -> str:
        """Returns a string representing the speaking sound."""

    def another_public_method(self):
        pass

class Car:
    """A class representing a car."""

    def make_noise(self, octane_level: int) -> str:
        """Generate noise based on the octane level."""

    def drive(self):
        pass


def main():
    """
    >>> shapes = (CircleShape(1, 2, 3, DrawingAPI1()), CircleShape(5, 7, 11, DrawingAPI2()))

    >>> for shape in shapes:
    ...    shape.scale(2.5)
    ...    shape.draw()
    API1.circle at 1:2 radius 7.5
    API2.circle at 5:7 radius 27.5
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
```