# FIRST SOLUTION (NOT WORKING BY ONE)
# def find_start_of_packet(datastream):
#   # Initialize the buffer with the first four characters of the datastream.
#   buffer = datastream[:4]

#   # Iterate through the rest of the datastream.
#   for i in range(4, len(datastream)):
#     # Shift the buffer to the left by one character and add the next character
#     # from the datastream to the right.
#     buffer = buffer[1:] + datastream[i]

#     # Check if the four characters in the buffer are all different.
#     if len(set(buffer)) == 4:
#       # Return the number of characters that have been processed so far.
#       return i

# # Read the input from the file.
# with open("input.txt") as file:
#   datastream = file.read()

# # Find the start of the packet.
# result = find_start_of_packet(datastream)

# # Print the result.
# print(result)



# SECOND SOLUTION

# Read the input from the file.
with open("input.txt") as file:
  data = file.read()

# Initialize a buffer to store the last four characters
buffer = []

# Iterate through the datastream buffer
for i, c in enumerate(data):
  # Add the current character to the buffer
  buffer.append(c)
  
  # If the buffer has more than four characters, remove the oldest character
  if len(buffer) > 4:
    buffer.pop(0)
  
  # If the last four characters in the buffer are all different,
  # we have found the start-of-packet marker, so we return the number
  # of characters that have been processed so far
  if len(set(buffer)) == 4:
    print(i+1)
    break