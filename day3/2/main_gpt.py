# Open the input file
with open('input.txt', 'r') as file:
  # Read the lines from the file and store them in a list
  rucksacks = file.read().strip().split('\n')

def find_common_item_type(rucksack1, rucksack2, rucksack3):
  # Convert the rucksacks to sets
  set1 = set(rucksack1)
  set2 = set(rucksack2)
  set3 = set(rucksack3)

  # Find the common item type by taking the intersection of the three sets
  common_item_types = set1.intersection(set2, set3)

  # Return the first common item type (there should only be one)
  return list(common_item_types)[0]
# Initialize the sum of priorities to 0
sum_of_priorities = 0

# Go through each group of three rucksacks
for i in range(0, len(rucksacks), 3):
  # Find the item type that appears in all three rucksacks
  common_item_type = find_common_item_type(rucksacks[i], rucksacks[i+1], rucksacks[i+2])

  # Find the ASCII value of the item type
  ascii_value = ord(common_item_type)

  # Calculate the priority of the item type
  if common_item_type.islower():
    priority = ascii_value - 96
  else:
    priority = ascii_value - 38

  # Add the priority to the sum of all priorities
  sum_of_priorities += priority

# Print the sum of all priorities
print(sum_of_priorities)
