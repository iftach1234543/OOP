from enum import Enum


class Color(Enum):
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"
    YELLOW = "Yellow"
    CYAN = "Cyan"
    MAGENTA = "Magenta"
    BLACK = "Black"


def test_color_enum():
    """
    Test the Color enum to ensure it has the correct members and values.
    """
    # Test the names and values of the Color enum
    assert Color.RED.name == "RED", f"Expected 'RED', but got {Color.RED.name}"
    assert Color.RED.value == "Red", f"Expected 'Red', but got {Color.RED.value}"

    assert Color.GREEN.name == "GREEN", f"Expected 'GREEN', but got {Color.GREEN.name}"
    assert Color.GREEN.value == "Green", f"Expected 'Green', but got {Color.GREEN.value}"

    assert Color.BLUE.name == "BLUE", f"Expected 'BLUE', but got {Color.BLUE.name}"
    assert Color.BLUE.value == "Blue", f"Expected 'Blue', but got {Color.BLUE.value}"

    assert Color.YELLOW.name == "YELLOW", f"Expected 'YELLOW', but got {Color.YELLOW.name}"
    assert Color.YELLOW.value == "Yellow", f"Expected 'Yellow', but got {Color.YELLOW.value}"

    assert Color.CYAN.name == "CYAN", f"Expected 'CYAN', but got {Color.CYAN.name}"
    assert Color.CYAN.value == "Cyan", f"Expected 'Cyan', but got {Color.CYAN.value}"

    assert Color.MAGENTA.name == "MAGENTA", f"Expected 'MAGENTA', but got {Color.MAGENTA.name}"
    assert Color.MAGENTA.value == "Magenta", f"Expected 'Magenta', but got {Color.MAGENTA.value}"

    assert Color.BLACK.name == "BLACK", f"Expected 'BLACK', but got {Color.BLACK.name}"
    assert Color.BLACK.value == "Black", f"Expected 'Black', but got {Color.BLACK.value}"

    # Test that all colors are included in the Color enum
    expected_colors = {"RED", "GREEN", "BLUE", "YELLOW", "CYAN", "MAGENTA", "BLACK"}
    actual_colors = set(color.name for color in Color)
    assert expected_colors == actual_colors, f"Expected colors: {expected_colors}, but got: {actual_colors}"


if __name__ == '__main__':
    # Run tests for Color enum
    test_color_enum()
    print("All Color enum tests passed!")
