from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    # Test instantiation
    dish = Dish("Lasanha", 35.0)
    assert isinstance(dish, Dish)

    # Test name and price attributes
    assert dish.name == "Lasanha"
    assert dish.price == 35.0

    # Test __repr__
    expected_repr = "Dish('Lasanha', R$35.00)"
    assert repr(dish) == expected_repr

    # Test __eq__
    dish2 = Dish("Lasanha", 35.0)
    assert dish == dish2

    # Test __hash__
    assert hash(dish) == hash(dish2)

    # Test add_ingredient_dependency
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("molho de tomate")
    dish.add_ingredient_dependency(ingredient1, 200)
    dish.add_ingredient_dependency(ingredient2, 500)
    assert dish.recipe == {ingredient1: 200, ingredient2: 500}

    # Test get_restrictions
    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert dish.get_restrictions() == expected_restrictions

    # Test get_ingredients
    expected_ingredients = {ingredient1, ingredient2}
    assert dish.get_ingredients() == expected_ingredients

    # Test invalid price type
    with pytest.raises(TypeError):
        Dish("Lasanha", "35.0")

    # Test price <= 0
    with pytest.raises(ValueError):
        Dish("Lasanha", -35.0)

    # Test __hash__ for different dish
    dish3 = Dish("Purê de batata", 35.0)
    assert hash(dish) != hash(dish3)
