import math
import pytest
from main import Area
def test_circle_area(capsys):
    s = Area(3)
    s.get_area()
    captured = capsys.readouterr()
    assert f"площадь круга = {round(math.pi * 9, 2)}" in captured.out

def test_rectangle_area(capsys):
    s = Area(3, 4)
    s.get_area()
    captured = capsys.readouterr()
    assert "площадь прямоугольника = 12" in captured.out

def test_triangle_area_right(capsys):
    s = Area(3, 4, 5)
    s.get_area()
    captured = capsys.readouterr()
    assert "Площадь прямоугольного треугольника = 6.0" in captured.out

def test_invalid_triangle(capsys):
    s = Area(1, 5, 9)
    s.get_area()
    captured = capsys.readouterr()
    assert "не существует" in captured.out

def test_invalid_args():
    with pytest.raises(ValueError):
        Area(1, "a", 3)
