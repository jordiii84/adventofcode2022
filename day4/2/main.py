# This code seems to be reading in lines from a file called "input.txt". 
# Each line in the file represents a pair of ranges, separated by a comma. 
# For example, "1-10,20-30" would be one line in the file.
f = open("input.txt", "r")
lines = f.readlines()

# The code defines two functions, `get_limits` and `get_sections`, which are used to parse the range pairs from each line. 
# The `get_limits` function returns the start and end of the range as a tuple, while the `get_sections` function returns a list of all the numbers in the range.
def get_limits(pair):
    digits=pair.split("-")
    return(int(digits[0]),int(digits[1]))

def get_sections(pair):
    digits=pair.split("-")
    return [i for i in range(int(digits[0]),int(digits[1])+1)]

# The code then iterates over the lines in the input file, and for each line, it uses the `get_sections` function to create two lists of numbers representing the two ranges from the line. 
# Then, it checks if any of the numbers from the first range are also in the second range. If so, it increments a variable called `overlap` by 1 and breaks out of the inner loop.
overlap=0
for line in lines:
    assigned = line.strip("\n").split(",")
    print(assigned)
    elv1=get_sections(assigned[0])
    elv2=get_sections(assigned[1])
    for section in elv1:
        if section in elv2:
            print(f"{assigned} Si"  )
            overlap+=1
            break

# At the end, the code prints the value of `overlap`, which is the total number of range pairs that had at least one number in common.
print(overlap)
