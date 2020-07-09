with open('all_numbers.txt', "w") as all_numbers:
    all_numbers.write(input('Введіть числа через кому: '))
with open('all_numbers.txt') as all_numbers:
    all_numbers = all_numbers.read()
print(all_numbers)
all_numbers = all_numbers.split(',')
list_= []
for i in all_numbers:
    if int(i)%2 == 0:
        list_.append(i)
print(list_)
with open('sort_numbers.txt', "w") as sort_numbers:
    for i in list_:
        sort_numbers.write(str(i)+' ')
with open('sort_numbers.txt') as sort_numbers:
    print('Sorted numbers are: ',sort_numbers.read())
