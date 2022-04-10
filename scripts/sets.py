from data.sets_categories_data import *


def clean_ingredients(dish_name: str, dish_ingredients: list) -> tuple:
    """
    Dedupes the ingredients list and returns a tuple
    containing 2 elements, a string, the dishes name, and
    a set containing the deduped ingredients.
    """
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name: str, drink_ingredients: list) -> str:
    """
    Checks the list of ingredients for the given drink to see if
    if it is a mocktail or a cocktail.
    Returns a string with the drinks name and its category (mocktail or cocktail)
    """
    if set(drink_ingredients).isdisjoint(ALCOHOLS):
        return drink_name + ' Mocktail'
    return drink_name + ' Cocktail'


def categorise_dish(dish_name: str, dish_ingredients: set) -> str:
    """
    Checks the dish's ingredients against the categories sets and
    returns the dish's name and its category.
    """
    if set(dish_ingredients).union(VEGAN):
        return dish_name + ': VEGAN'
