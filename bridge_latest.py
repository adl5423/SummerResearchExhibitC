```python
import doctest

class DrawingAPI1:
    def draw_circle(self, x, y, radius):
        """Draws a circle with the given parameters."""
        print(f'API1.circle at {x}:{y} radius {radius}')

    def another_method(self):
        pass


class DrawingAPI2:
    """Class representing the second drawing API."""
    def draw_circle(self, x, y, radius):
        """Draws a circle with the given parameters."""
        print(f'API2.circle at {x}:{y} radius {radius}')

    def additional_method(self):
        pass


class CircleShape:
    """Represents a circle shape."""
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        """Draws the bridge."""
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, pct):
        """Scale the object by the given percentage."""
        self._radius *= pct


def main():
    shapes = (CircleShape(1, 2, 3, DrawingAPI1()), CircleShape(5, 7, 11, DrawingAPI2()))

    for shape in shapes:
        shape.scale(2.5)
        shape.draw()


if __name__ == "__main__":
    main()
    doctest.testmod()
```