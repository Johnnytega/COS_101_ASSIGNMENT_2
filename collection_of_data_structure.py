okpa_list = ['bambara nut', 'maggie', 'pepper', 'palm oil']
print(okpa_list)
okpa_list.append('fish')
print(okpa_list)

ingredient = input("Enter an ingredient: ")
for item in okpa_list:
    if item == ingredient:
        print(item, "is in the list")


numbers = list(range(1, 11))
total = sum(numbers)
print("numbers:", numbers)
print("sum of numbers:", total)

for number in range(10,0,-1):
    print(number)