from Square import Square
from Rect import Rect
from circle import Circle
import math
from Color import Color
from Container import Container


def find_rectangle_dimensions(shape_a, shape_b):
    """
    Find dimensions of a rectangle based on the combined area and perimeter of two shapes.

    param shape_a: First shape (Circle or Rect).
    :param shape_a:
    :param shape_b: Second shape (Circle or Rect).
    :return: Rect or Square with calculated dimensions.
    :raises ValueError: If the calculated area or perimeter is invalid.
    """
    area = float(shape_a.get_area()) + float(shape_b.get_area())
    perimeter = float(shape_a.get_per()) + float(shape_b.get_per())

    if perimeter <= 0 or area <= 0:
        raise ValueError("Perimeter and area must be positive values.")

    semi_perimeter = perimeter / 2

    a = 1
    b = -semi_perimeter
    c = area

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        raise ValueError("No real solutions for the given area and perimeter.")

    width1 = (-b + math.sqrt(discriminant)) / (2 * a)
    length1 = semi_perimeter - width1

    if width1 == length1:
        new_shape = Square(Color.BLACK, length1)
    else:
        new_shape = Rect(Color.BLACK, width1, length1)

    return new_shape


def main():
    """
    Main function to create a container, generate shapes, and print statistics.
    """
    my_container = Container()
    my_container.generate(100)
    print("Total area:", my_container.sum_areas())
    print("Total perimeter:", my_container.sum_perimeters())
    print("Colors:", my_container.count_colors())


def test_find_rectangle_dimensions():
    """
    Test the find_rectangle_dimensions function with known shapes.
    """
    # Create known shapes
    circle1 = Circle(Color.RED, 5)
    rect1 = Rect(Color.GREEN, 4, 6)

    # Calculate expected results
    area = circle1.get_area() + rect1.get_area()
    perimeter = circle1.get_per() + rect1.get_per()

    semi_perimeter = perimeter / 2
    a = 1
    b = -semi_perimeter
    c = area

    discriminant = b ** 2 - 4 * a * c
    width1 = (-b + math.sqrt(discriminant)) / (2 * a)
    length1 = semi_perimeter - width1

    if width1 == length1:
        expected_shape = Square(Color.BLACK, length1)
    else:
        expected_shape = Rect(Color.BLACK, width1, length1)

    # Call function to test
    new_shape = find_rectangle_dimensions(circle1, rect1)

    # Check if the new shape matches the expected shape
    assert isinstance(new_shape, (Rect, Square)), "The new shape should be a Rect or Square."
    assert new_shape.get_area() == area, f"Expected area: {area}, but got: {new_shape.get_area()}"
    assert new_shape.get_per() == perimeter, f"Expected perimeter: {perimeter}, but got: {new_shape.get_per()}"


if __name__ == '__main__':
    test_find_rectangle_dimensions()
    print("All tests passed!")
    main()
