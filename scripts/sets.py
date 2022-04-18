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
    categories = [VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE]
    for category in categories:  # O(n)
        if set(dish_ingredients).issubset(category):
            category_name = [name for name in globals() if globals()[
                name] is category]
            return dish_name + ': ' + str(category_name[0])


def tag_special_ingredients(dish: tuple) -> tuple:
    """
    Returns the dish's name plus its ingredients requiring
    a special note.
    """
    return (dish[0], set(dish[1]) & SPECIAL_INGREDIENTS)


def compile_ingredients(dishes: list) -> set:
    """
    Returns a set containing the deduped ingredients in dishes
    """
    shopping_list = set()
    for dish in dishes:  # O(n)
        shopping_list.update(dish)
    return shopping_list


def separate_appetisers(dishes: list, appetizers: list) -> list:
    """
    Removes the list of appetisers from the list of dishes to
    return a list containing only dishes not uses as appetesiers
    """
    return list(set(dishes) - set(appetizers))  # O(n)


def singleton_ingredients(dishes: list, INTERSECTIONS: set) -> set:
    """
    Returns a set contianing the ingredients that are unique for
    particular dishes
    """
    return compile_ingredients(dishes) - INTERSECTIONS  # O(n)
