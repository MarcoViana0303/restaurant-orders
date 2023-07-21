from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # Test instantiation
    ingredient = Ingredient("queijo mussarela")
    assert isinstance(ingredient, Ingredient)

    # Test restrictions
    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert ingredient.restrictions == expected_restrictions

    # Test __repr__
    expected_repr = "Ingredient('queijo mussarela')"
    assert repr(ingredient) == expected_repr

    # Test __eq__
    ingredient2 = Ingredient("queijo mussarela")
    assert ingredient == ingredient2

    # Test __hash__ for different ingredients
    ingredient3 = Ingredient("bacon")
    assert hash(ingredient) != hash(ingredient3)

    # Test __hash__ for equal ingredients
    ingredient4 = Ingredient("queijo mussarela")
    assert hash(ingredient) == hash(ingredient4)

    # Test name correctness
    assert ingredient.name == "queijo mussarela"
