# Open the input file
with open('input.txt', 'r') as file:
  # Read the lines from the file and store them in a list
  rucksacks = file.read().strip().split('\n')

def find_common_item_type(rucksack):
  # Split the rucksack into its two compartments
  comp1, comp2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]

  # Find the common item type by going through each character in the first compartment
  # and checking if it appears in the second compartment
  for c in comp1:
    if c in comp2:
      return c
# Initialize the sum of priorities to 0
sum_of_priorities = 0

# Go through each rucksack
for rucksack in rucksacks:
  # Find the item type that appears in both compartments
  common_item_type = find_common_item_type(rucksack)

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
