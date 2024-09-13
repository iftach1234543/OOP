from Rect import Rect
from Color import Color


class Square(Rect):
    def __init__(self, color: Color, length: float):
        """
        Initialize a Square object.

        :param color: Color of the square.
        :param length: Length of the square (same as width).
        """
        super().__init__(color, length, length)

    def set_color(self, color: Color):
        """
        Set the color of the square.

        :param color: Color to set.
        """
        self.color = color

    def get_color(self) -> Color:
        """
        Get the color of the square.

        :return: Color of the square.
        """
        return self.color

    def get_area(self) -> float:
        """
        Get the area of the square.

        :return: Area of the square.
        """
        return self.area

    def get_per(self) -> float:
        """
        Get the perimeter of the square.

        :return: Perimeter of the square.
        """
        return self.perimeter
