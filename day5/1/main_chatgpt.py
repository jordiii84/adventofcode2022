# Open the file in read mode
with open("input.txt", "r") as file:
    # Read the contents of the file
    ranges_string = file.read()
    
# Split the input string into individual ranges
ranges = ranges_string.strip("\n").split(",")

num_fully_contained_pairs = 0

for range1 in ranges:
    # Split the range into the starting and ending numbers
    start1, end1 = map(int, range1.split("-"))
    
    for range2 in ranges:
        # Split the range into the starting and ending numbers
        start2, end2 = map(int, range2.split("-"))
        
        # If the start and end of range1 are both greater than or equal to the start and end of range2, respectively,
        # then range1 fully contains range2
        if start1 >= start2 and end1 <= end2:
            num_fully_contained_pairs += 1

# Divide by two because each pair is counted twice (once for each range in the pair)
print(num_fully_contained_pairs // 2)