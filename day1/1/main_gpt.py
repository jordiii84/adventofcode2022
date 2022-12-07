f = open("input_test.txt", "r")
food_items = f.read().splitlines()

current_elf = 1

elf_calories = {i: 0 for i in range(1, len(food_items) + 1)}

for item in food_items:
    if item == '':
        current_elf += 1
    else:
        elf_calories[current_elf] += int(item)

max_calories = max(elf_calories.values())

print(max_calories)

