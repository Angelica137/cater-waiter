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
