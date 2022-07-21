from src.Circle import Circle
import pytest


#   Площадь
@pytest.mark.parametrize("input_side, exp", [
    (4, 48),
    (7, 147),
    (0, "raise ValueError"),
    (-1, "raise ValueError")
])
def test_area(input_side, exp):
    circle = Circle(input_side)
    assert circle.area == exp


#   Периметр
@pytest.mark.parametrize("input_side, exp", [
    (5, 30),
    (3, 18),
    (0, "raise ValueError"),
    (-1, "raise ValueError")
])
def test_perimeter(input_side, exp):
    circle = Circle(input_side)
    assert circle.perimeter == exp
