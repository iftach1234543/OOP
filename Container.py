import math
from Color import Color
from Square import Square
import random
from Rect import Rect
from circle import Circle


class Container:
    def __init__(self, shapes=None):
        """
        Initialize a Container object.

        :param shapes: List of shapes to initialize with (default is empty).
        """
        if shapes is None:
            shapes = []
        self.shapes = shapes

    def generate(self, num_shapes: int):
        """
        Generate random shapes and add them to the container.

        :param num_shapes: Number of shapes to generate.
        """
        colors = list(Color)
        for _ in range(num_shapes):
            shape_type = random.choice([Circle, Rect, Square])
            color = random.choice(colors)
            if shape_type == Circle:
                radius = random.uniform(1, 10)
                shape = Circle(color, radius)
            elif shape_type == Rect:
                length = random.uniform(1, 10)
                width = random.uniform(1, 10)
                shape = Rect(color, length, width)
            elif shape_type == Square:
                length = random.uniform(1, 10)
                shape = Square(color, length)
            self.shapes.append(shape)

    def sum_areas(self) -> float:
        """
        Calculate the sum of areas of all shapes in the container.

        :return: Total area of all shapes.
        """
        return sum(shape.get_area() for shape in self.shapes)

    def sum_perimeters(self) -> float:
        """
        Calculate the sum of perimeters of all shapes in the container.

        :return: Total perimeter of all shapes.
        """
        return sum(shape.get_per() for shape in self.shapes)

    def count_colors(self) -> dict:
        """
        Count the number of shapes for each color in the container.

        :return: Dictionary where keys are colors and values are counts.
        """
        color_count = {}
        for shape in self.shapes:
            color = shape.get_color()
            if color in color_count:
                color_count[color] += 1
            else:
                color_count[color] = 1
        return color_count


def test_container():
    """
    Test the Container class to ensure methods work as expected.
    """
    # Create a Container with no initial shapes
    container = Container()

    # Generate 10 random shapes
    container.generate(10)

    # Check if the number of shapes in the container matches the number generated
    assert len(container.shapes) == 10, f"Expected 10 shapes, but got {len(container.shapes)}"

    # Check if sum_areas returns the correct total area
    total_area = container.sum_areas()
    expected_area = sum(shape.get_area() for shape in container.shapes)
    assert math.isclose(total_area, expected_area), f"Expected total area {expected_area}, but got {total_area}"

    # Check if sum_perimeters returns the correct total perimeter
    total_perimeter = container.sum_perimeters()
    expected_perimeter = sum(shape.get_per() for shape in container.shapes)
    assert math.isclose(total_perimeter, expected_perimeter), f"Expected total perimeter {expected_perimeter}, but got {total_perimeter}"

    # Check if count_colors returns the correct color counts
    color_count = container.count_colors()
    expected_color_count = {}
    for shape in container.shapes:
        color = shape.get_color()
        if color in expected_color_count:
            expected_color_count[color] += 1
        else:
            expected_color_count[color] = 1
    assert color_count == expected_color_count, f"Expected color count {expected_color_count}, but got {color_count}"


if __name__ == '__main__':
    test_container()
    print("All Container tests passed!")
