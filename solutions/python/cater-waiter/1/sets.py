"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    dish_set=set(dish_ingredients)
    final_tuple=[dish_name,dish_set]
    return tuple(final_tuple)
    """Remove duplicates from `dish_ingredients`.

    Parameters:
        dish_name (str): The name of the dish.
        dish_ingredients (list): The ingredients for the dish.

    Returns:
        tuple: Containing (dish name, ingredient set).

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.

    """

    pass


def check_drinks(drink_name, drink_ingredients):
    
    if set(drink_ingredients).isdisjoint(ALCOHOLS)==False:
        return f'{drink_name} Cocktail'
    else :
        return f'{drink_name} Mocktail'
    """Append "Cocktail" (alcohol)  or "Mocktail" (no alcohol) to `drink_name`, based on `drink_ingredients`.

    Parameters:
        drink_name (str): Name of the drink.
        drink_ingredients (list): Ingredients in the drink.

    Returns:
        str: `drink_name` appended with "Mocktail" or "Cocktail".

    The function should return the name of the drink followed by "Mocktail" (non-alcoholic) and drink
    name followed by "Cocktail" (includes alcohol).

    """

    pass


def categorize_dish(dish_name, dish_ingredients):
    if dish_ingredients<=VEGAN:
        return f'{dish_name}: VEGAN'
    if dish_ingredients<=VEGETARIAN:
        return f'{dish_name}: VEGETARIAN'
    if dish_ingredients<=PALEO:
        return f'{dish_name}: PALEO'
    if dish_ingredients<=KETO:
        return f'{dish_name}: KETO'
    if dish_ingredients<=OMNIVORE:
        return f'{dish_name}: OMNIVORE'
    
    """Categorize `dish_name` based on `dish_ingredients`.

    Parameters:
        dish_name (str): The dish to be categorized.
        dish_ingredients (set): The ingredients for the dish.

    Returns:
        str: The dish name appended with ": <CATEGORY>".

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    `<CATEGORY>` can be any one of  (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`
    """

    pass


def tag_special_ingredients(dish):
    SPECIAL_INGREDIENTS_set=set(dish[1])&SPECIAL_INGREDIENTS
    return (dish[0], SPECIAL_INGREDIENTS_set)
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`.

    Parameters:
        dish (tuple): (dish name, list of dish ingredients).

    Returns:
        tuple: Containing (dish name, dish special ingredients).

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """

    pass


def compile_ingredients(dishes):
    all_ingredients=set()
    for i in dishes:
        all_ingredients.update(i)
    return all_ingredients
 
    """Create a master list of ingredients.

    Parameters:
        dishes (list): Dish ingredient sets.

    Returns:
        set: Ingredients compiled from `dishes`.

    This function should return a `set` of all ingredients from all listed dishes.
    """

    pass


def separate_appetizers(dishes, appetizers):
    set1=set(dishes)
    set2=set(appetizers)
    set3=list(set1 - set2)
    return set3
    
    """Determine which `dishes` are designated `appetizers` and remove them.

    Parameters:
        dishes (list): Group of dish names.
        appetizers (list): Group of appetizer names.

    Returns:
        list: Group of dish names that do not appear on appetizer list.

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """

    pass


def singleton_ingredients(dishes, intersection):
    set1=set()
    for dish in dishes:
        set2=set(dish-intersection)
        set1.update(set2)
    return set1

    """Find singleton ingredients within the group of dishes (ingredients that only appear once across dishes).

    Parameters:
        dishes (list): Group of ingredient sets.
        intersection (set): Can be one of `<CATEGORY>_INTERSECTIONS` constants imported from `sets_categories_data.py`.

    Returns:
        set: Containing singleton ingredients.

    Each dish is represented by a `set` of its ingredients.

    Each `<CATEGORY>_INTERSECTIONS` is an `intersection` of all dishes in the category. `<CATEGORY>` can be any one of:
        (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).

    The function should return a `set` of ingredients that only appear in a single dish.
    """

    pass
