x = set("i love python")
vowels = 0
constants = 0
new = set()
for i in x:
    letter = i.lower()
    if letter == "a" or letter == "e" or\
       letter == "i" or letter == "o" or\
       letter == "u" or letter == "y":
        vowels += 1
        new.add(letter)
    else:
        constants += 1
new1=list(new)
new1.sort()

print("Голосні: %s\n Приголосні: %s" % (vowels, constants))
print(new1)
