matrix =      [[1, 2, 3],
               [4, 5, 9],
               [7, 10, 6]]
 
min_el, max_el = min(matrix[0]), max(matrix[0])
row_min, row_max = 0, 0
for _r, row in enumerate(matrix): #в змінну r записувались індекс елемента, а в column - значення
    if min(row) < min_el: #enumerate  - нумерує список і повертає номер та значення
        min_el = min(row)
        row_min = _r
    if max(row) > max_el:
        max_el = max(row)
        row_max = _r
 
matrix[row_min], matrix[row_max] = matrix[row_max], matrix[row_min]
 
for row in matrix:
    print(*row)
