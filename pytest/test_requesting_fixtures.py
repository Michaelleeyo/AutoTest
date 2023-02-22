import pytest


class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True


class FruitSalad:
    def __init__(self, *fruit_bow1):
        self.fruit = fruit_bow1
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()

# Arrange


@pytest.fixture
def fruit_bow1():
    return [Fruit("apple"), Fruit("banana")]


def test_fruit_salad(fruit_bow1):
    fruit_salad = FruitSalad(*fruit_bow1)
    assert all(fruit.cubed for fruit in fruit_salad.fruit)
