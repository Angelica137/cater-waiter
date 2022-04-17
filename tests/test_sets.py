from scripts.sets import *


def test_clean_ingredients():
    ingredients = ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro',
                   'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro']
    assert clean_ingredients('Punjabi-Style Chole', ingredients) == ('Punjabi-Style Chole', {'garam masala', 'bay leaves', 'ground turmeric', 'ginger', 'garlic paste', 'peppercorns',
                                                                                             'ginger paste', 'red chili powder', 'cardamom', 'chickpeas', 'cumin powder', 'vegetable oil', 'tomatoes', 'coriander powder', 'onions', 'cilantro', 'cloves'})


def test_check_drinks():
    ingredients = ['honeydew', 'coconut water', 'mint leaves',
                   'lime juice', 'salt', 'english cucumber']
    assert check_drinks(
        'Honeydew Cucumber', ingredients) == 'Honeydew Cucumber Mocktail'


def test_check_drink_alcohol():
    ingredients = ['cinnamon stick', 'scotch', 'whole cloves',
                   'ginger', 'pomegranate juice', 'sugar', 'club soda']
    assert check_drinks(
        'Shirley Tonic', ingredients) == 'Shirley Tonic Cocktail'


def test_categorise_dish_vegan():
    ingredients = ['tofu', 'soy sauce', 'salt', 'black pepper', 'cornstarch', 'vegetable oil',
                   'garlic', 'ginger', 'water', 'vegetable stock', 'lemon juice', 'lemon zest', 'sugar']
    assert categorise_dish("Sticky Lemon Tofu",
                           ingredients) == 'Sticky Lemon Tofu: VEGAN'


def test_categorise_dish_omnivore():
    ingredients = ['shrimp', 'bacon', 'avocado', 'chickpeas', 'fresh tortillas', 'sea salt',
                   'guajillo chile', 'slivered almonds', 'olive oil', 'butter', 'black pepper', 'garlic', 'onion']
    dish_name = 'Shrimp Bacon and Crispy Chickpea Tacos with Salsa de Guacamole'
    assert categorise_dish(
        dish_name, ingredients) == 'Shrimp Bacon and Crispy Chickpea Tacos with Salsa de Guacamole: OMNIVORE'


def test_tag_special_ingredients():
    name = 'Ginger Glazed Tofu Cutlets'
    ingredients = ['tofu', 'soy sauce', 'ginger', 'corn starch',
                   'garlic', 'brown sugar', 'sesame seeds', 'lemon juice']
    assert tag_special_ingredients((name, ingredients)) == (
        'Ginger Glazed Tofu Cutlets', {'garlic', 'soy sauce', 'tofu'})


def test_tag_special_ingredients_2():
    name = 'Arugula and Roasted Pork Salad'
    ingredients = ['pork tenderloin', 'arugula', 'pears', 'blue cheese',
                   'pine nuts', 'balsamic vinegar', 'onions', 'black pepper']
    assert tag_special_ingredients((name, ingredients)) == ('Arugula and Roasted Pork Salad', {
        'pork tenderloin', 'blue cheese', 'pine nuts', 'onions'})


def test_compile_ingredients():
    ingredients_list = [{'tofu', 'soy sauce', 'ginger', 'corn starch', 'garlic', 'brown sugar', 'sesame seeds', 'lemon juice'},
                        {'pork tenderloin', 'arugula', 'pears', 'blue cheese', 'pine nuts',
                         'balsamic vinegar', 'onions', 'black pepper'},
                        {'honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'}]
    assert compile_ingredients(ingredients_list) == {'arugula', 'brown sugar', 'honeydew', 'coconut water', 'english cucumber', 'balsamic vinegar', 'mint leaves', 'pears', 'pork tenderloin',
                                                     'ginger', 'blue cheese', 'soy sauce', 'sesame seeds', 'black pepper', 'garlic', 'lime juice', 'corn starch', 'pine nuts', 'lemon juice', 'onions', 'salt', 'tofu'}


def test_separate_appetisers():
    dishes = ['Avocado Deviled Eggs', 'Flank Steak with Chimichurri and Asparagus', 'Kingfish Lettuce Cups',
              'Grilled Flank Steak with Caesar Salad', 'Vegetarian Khoresh Bademjan', 'Avocado Deviled Eggs',
              'Barley Risotto', 'Kingfish Lettuce Cups']
    appetisers = ['Kingfish Lettuce Cups', 'Avocado Deviled Eggs', 'Satay Steak Skewers',
                  'Dahi Puri with Black Chickpeas', 'Avocado Deviled Eggs', 'Asparagus Puffs',
                  'Asparagus Puffs']

    assert set(separate_appetisers(dishes, appetisers)) == set(['Vegetarian Khoresh Bademjan', 'Barley Risotto', 'Flank Steak with Chimichurri and Asparagus',
                                                                'Grilled Flank Steak with Caesar Salad'])
