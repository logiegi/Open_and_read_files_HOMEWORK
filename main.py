from pprint import pprint

with open('files', 'rt', encoding="utf-8") as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ingredients_count = int(file.readline().strip())
        ingredients = []
        for _ in range(ingredients_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        file.readline()
        cook_book[dish] = ingredients
    print('cook_book =')
    pprint(cook_book, sort_dicts=False)
print()
print()


# 2.txt

def get_shop_list_by_dishes(dishes, person_count):
    order = {}
    for dish in dishes:
        for k, v in cook_book.items():
            if dish in k:
                get_order(v, order, person_count)
    pprint(order)


def get_order(v, order, person_count):
    for dish_ingredients in v:
        if dish_ingredients['ingredient_name'] not in order:
            order[list(dish_ingredients.values())[0]] = {'measure': dish_ingredients['measure'],
                                                         'quantity': dish_ingredients['quantity'] * person_count}
        else:
            order[list(dish_ingredients.values())[0]]['quantity'] += dish_ingredients['quantity'] * person_count


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

# 3.txt


with open('4.txt', 'x', encoding='utf-8') as file_4:
    result = {}
    file_1 = open('1.txt', 'rt', encoding="utf-8")
    file_2 = open('2.txt', 'rt', encoding="utf-8")
    file_3 = open('3.txt', 'rt', encoding="utf-8")
    a, b, c = file_1.readlines(), file_2.readlines(), file_3.readlines()
    result[file_1.name] = a, len(a)
    result[file_2.name] = b, len(b)
    result[file_3.name] = c, len(c)
    sort_result = {k: v for k, v in sorted(result.items(), key=lambda item: len(item[1][0]))}
    for k, v in sort_result.items():
        file_4.write(k)
        file_4.write('\n')
        file_4.write(str(v[1]))
        file_4.write('\n')
        file_4.writelines(v[0])
        file_4.write('\n')
    file_1.close()
    file_2.close()
    file_3.close()
