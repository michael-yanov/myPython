def any_duplicates(square):
    lst = []
    for i in square:
        for j in i:
            lst.append(j)
    return len(lst) != len(set(lst))
    
print(any_duplicates([[1,2,3], [7,4,6], [5,8,9]]))


    