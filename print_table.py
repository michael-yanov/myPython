def print_table(data):
    print('TABLE'.center(30, '-'))
    len_lst = []
    for j in range(4): #cols
        for i in range(3): #rows
            len_lst.append(len(data[i][j]))
            max_len = max(len_lst)
    for j in range(4): #cols
        for i in range(3): #rows
            print((data[i][j]).rjust(max_len), end=' ')
        print()

table_data = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']
]

print_table(table_data)
