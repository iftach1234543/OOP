from shape import Shape
from Color import Color


class Rect(Shape):
    def __init__(self, color: Color, length: float, width: float):
        """
        Initialize a Rect object.

        :param color: Color of the rectangle.
        :param length: Length of the rectangle.
        :param width: Width of the rectangle.
        """
        self.color = color
        self.length = length
        self.width = width
        self.area = length * width
        self.perimeter = 2 * (length + width)

    def set_color(self, color: Color):
        """
        Set the color of the rectangle.

        :param color: Color to set.
        """
        self.color = color

    def get_color(self) -> Color:
        """
        Get the color of the rectangle.

        :return: Color of the rectangle.
        """
        return self.color

    def get_area(self) -> float:
        """
        Get the area of the rectangle.

        :return: Area of the rectangle.
        """
        return self.area

    def get_per(self) -> float:
        """
        Get the perimeter of the rectangle.

        :return: Perimeter of the rectangle.
        """
        return self.perimeter
