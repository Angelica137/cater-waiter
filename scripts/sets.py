def clean_ingredients(dish_name: str, dish_ingredients: list) -> tuple:
    """
    Dedupes the ingredients list and returns a tuple
    containing 2 elements, a string, the dishes name, and
    a set containing the deduped ingredients.
    """
    return (dish_name, set(dish_ingredients))
