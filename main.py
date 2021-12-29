def get_recipes(recipes_file='list.txt'):
    cook_book = {}
    with open(recipes_file, encoding='utf-8') as receipt_file:
        while True:
            dish = receipt_file.readline().rstrip('\n').lower()
            if not dish:
                break
            cook_book[dish] = []
            i = int(receipt_file.readline().rstrip('\n'))
            items = [receipt_file.readline().rstrip('\n').rsplit('|') for _ in range(i)]
            for item in items:
                cook_book[dish].append({'ingridient_name': item[0].rstrip(), 'quantity': int(item[1].replace(' ', '')),
                'measure': item[2].replace(' ', '')})
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list(cook_book):
    person_count = int(input('Количество человек: '))
    dishes = input('Введите блюда через запятую с маленькой буквы: ').split(', ')
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
    print_shop_list(shop_list)


cook_book = get_recipes()
create_shop_list(cook_book)
