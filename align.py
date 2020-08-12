def print_picnic(items_dict, left_width, right_width):
    print('PICNIC ITEMS'.center(left_width + right_width, '-'))
    for k, v in items_dict.items():
        print(k.ljust(left_width, '.') + str(v).rjust(right_width))


picnic_items = {
    'sandwiches': 4,
    'apples': 12,
    'cups': 4,
    'cookies': 12
}

left_width = int(input('Enter left align: '))
right_width = int(input('Enter right align: '))
print_picnic(picnic_items, left_width, right_width)