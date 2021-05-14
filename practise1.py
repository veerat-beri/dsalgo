

def get_dish(current_ingredients: set, fat_ingredients, carb_ingredients, fiber_ingredients, can_cook_x: bool, can_cook_y: bool, total_ingredients_required=4):
    if len(current_ingredients) < total_ingredients_required:
        return "-", can_cook_x, can_cook_y

    if (not can_cook_x) and (not can_cook_y):
        return "-", can_cook_x, can_cook_y

    # Make X
    if can_cook_x:
        total_fat_ingredients = len(fat_ingredients)
        total_fibre_ingredients = len(fat_ingredients)

        if total_fat_ingredients + total_fibre_ingredients >= 4:
            if total_fat_ingredients >= 2:
                fib_fat_diff = total_fibre_ingredients - (total_fat_ingredients - 2)
                if fib_fat_diff > 0:
                    if fib_fat_diff >= 2:
                        fiber_ingredients = fiber_ingredients[2:]
                        fat_ingredients = fat_ingredients[2:]
                    else:
                        fiber_ingredients = fiber_ingredients[1:]
                        fat_ingredients = fat_ingredients[3:]

                elif fib_fat_diff < 0:
                    fat_fib_diff = abs(fib_fat_diff)
                    if fat_fib_diff >= 2:
                        fat_ingredients = fat_ingredients[4:]






            return "X", False, True
        return "-", can_cook_x, can_cook_y

    # Make Y
    total_carb_ingredients = len(carb_ingredients)
    return "Y", True, False

