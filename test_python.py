import math


# test filter, map, sorted
def test_filter():
    iterable = (1, 2, 3, 4, 5)
    assert tuple(filter(lambda x: x % 2 == 0, iterable)) == (2, 4)
    assert tuple(filter(lambda x: x % 2 == 1, iterable)) == (1, 3, 5)


def test_map():
    iterable = (1, 2, 3, 4, 5)
    assert tuple(map(lambda x: pow(x, 2), iterable)) == (1, 4, 9, 16, 25)


def test_sorted():
    iterable1 = (1, 2, 3, 4, 5)
    iterable2 = (5, 4, 3, 2, 1)
    iterable3 = ((2, 3), (1, 2))

    assert tuple(sorted(iterable1, reverse=False)) == iterable1
    assert tuple(sorted(iterable1, reverse=True)) == iterable2
    assert tuple(sorted(iterable3, key=lambda x: x[0])) == ((1, 2), (2, 3))


# test math pi, sqrt, pow, hypot
def test_pi():
    assert math.pi == 3.141592653589793


def test_sqrt():
    assert math.sqrt(16.0) == 4.0


def test_pow():
    assert math.pow(4.0, 2) == 16.0


def test_hypot():
    assert math.hypot(3.0, 4.0) == 5.0
    assert math.hypot(1.0, 3.0, 4.0, 5.0, 7.0) == 10.0
