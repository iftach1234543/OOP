import math
from shape import Shape
from Color import Color


class Circle(Shape):
    def __init__(self, color: Color, radius: float):
        """
        Initialize a Circle object.

        param color: Color of the circle.
        param radius: Radius of the circle.
        """
        self.color = color
        self.radius = radius
        self.area, self.perimeter = circle_properties(radius)

    def set_color(self, color: Color):
        """
        Set the color of the circle.

        :param color: Color to set.
        """
        self.color = color

    def get_color(self) -> Color:
        """
        Get the color of the circle.

        :return: Color of the circle.
        """
        return self.color

    def get_area(self) -> float:
        """
        Get the area of the circle.

        :return: Area of the circle.
        """
        return self.area

    def get_per(self) -> float:
        """
        Get the perimeter of the circle.

        :return: Perimeter of the circle.
        """
        return self.perimeter


def circle_properties(radius):
    """
        Calculate the area and perimeter of a circle.

        param radius: Radius of the circle.
        :return: Tuple containing area and perimeter of the circle.
        raises ValueError: If the radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")

    area = math.pi * (radius ** 2)
    perimeter = 2 * math.pi * radius

    return area, perimeter


def test_circle_properties():
    """
    Test the circle_properties function to ensure it calculates
    area and perimeter correctly.
    """
    # Test with a positive radius
    radius = 5
    expected_area = math.pi * (radius ** 2)
    expected_perimeter = 2 * math.pi * radius
    area, perimeter = circle_properties(radius)

    assert math.isclose(area, expected_area), f"Expected area {expected_area}, but got {area}"
    assert math.isclose(perimeter, expected_perimeter), f"Expected perimeter {expected_perimeter}, but got {perimeter}"

    # Test with radius of 0
    radius = 0
    expected_area = math.pi * (radius ** 2)
    expected_perimeter = 2 * math.pi * radius
    area, perimeter = circle_properties(radius)

    assert math.isclose(area, expected_area), f"Expected area {expected_area}, but got {area}"
    assert math.isclose(perimeter, expected_perimeter), f"Expected perimeter {expected_perimeter}, but got {perimeter}"

    # Test with another positive radius
    radius = 2.5
    expected_area = math.pi * (radius ** 2)
    expected_perimeter = 2 * math.pi * radius
    area, perimeter = circle_properties(radius)

    assert math.isclose(area, expected_area), f"Expected area {expected_area}, but got {area}"
    assert math.isclose(perimeter, expected_perimeter), f"Expected perimeter {expected_perimeter}, but got {perimeter}"

    # Test with a negative radius (should raise ValueError)
    try:
        circle_properties(-1)
        assert False, "Expected ValueError for negative radius, but no exception was raised."
    except ValueError:
        pass


if __name__ == '__main__':
    # Run the test for circle_properties
    test_circle_properties()
    print("All tests passed!")
