def get_cook_book():
    cook_book = {}
    with open("recipe.txt") as data:
        for items in data:
            name = items.strip()
            number = int(data.readline())
            list_ingr = []
            for pars_ingredients in range(number):
                all_ingr = data.readline().strip().split('|')
                pattern = {'ingredient_name': all_ingr[0], 'quantity': all_ingr[1], 'measure': all_ingr[2]}
                list_ingr.append(pattern)
                cook_book[name] = list_ingr
            data.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish_name, recipe in get_cook_book().items():
        for order in dishes:
            if order == dish_name:
                for ingred in recipe:
                    if ingred['ingredient_name'] not in shop_list.keys():
                        pattern = {'measure': ingred['measure'], 'quantity': person_count * int(ingred['quantity'])}
                        shop_list[ingred['ingredient_name']] = pattern
                    else:
                        shop_list[ingred['ingredient_name']]['quantity'] += person_count * int(ingred['quantity'])
    return shop_list


# print(get_cook_book())
# print(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Запеченный картофель', 'Запеченный картофель'], 1))
