def is_closed(file_):
    if file_.closed:
        print('Файл закрыт')
    else:
        print('Файл открыт')

cook_book = {}
with open('book.txt', 'r') as f:
    lines = f.readlines()
    line_count = 0

    while line_count < len(lines):
        dish_name = lines[line_count].strip()
        line_count += 1

        if not dish_name:
            continue

        ingredient_count = int(lines[line_count].strip())
        line_count += 1

        ingredient_list = []
        for i in range(ingredient_count):
            ingredient_info = lines[line_count + i].strip().split(' | ')
            ingredient_name = ingredient_info[0]
            ingredient_quantity = int(ingredient_info[1])
            ingredient_measure = ingredient_info[2]

            ingredient_list.append({
                'ingredient_name': ingredient_name,
                'quantity': ingredient_quantity,
                'measure': ingredient_measure
            })

        cook_book[dish_name] = ingredient_list
        line_count += ingredient_count

print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish not in cook_book:
            print('Ошибка: блюдо', dish, 'отсутствует в cook_book')
            continue
        for ingredient_info in cook_book[dish]:
                ingredient_name = ingredient_info['ingredient_name']
                ingredient_quantity = ingredient_info['quantity'] * person_count
                ingredient_measure = ingredient_info['measure']

                if ingredient_name not in shop_list:
                    shop_list[ingredient_name] = {
                        'measure': ingredient_measure,
                        'quantity': ingredient_quantity
                    }
                else:
                    shop_list[ingredient_name]['quantity'] += ingredient_quantity
    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

def sort_files(file1, file2, file3, output_file):
    file_info = [
        (count_lines(file1), file1),
        (count_lines(file2), file2),
        (count_lines(file3), file3)
    ]

    sorted_files = sorted(file_info, key=lambda x: x[0])

    with open(output_file, 'w') as output:
        for count, file in sorted_files:
            output.write(f"{file}\n"
                         f"{count}\n")
            with open(file, 'r') as f:
                output.write(f.read())
            output.write('\n')

def count_lines(file):
    with open(file, 'r') as f:
        return sum(1 for line in f)


file1 = '1.txt'
file2 = '2.txt'
file3 = '3.txt'
output_file = 'output.txt'
sort_files(file1, file2, file3, output_file)