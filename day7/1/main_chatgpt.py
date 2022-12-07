f = open("input_test.txt", "r")
lines = f.read().splitlines()
# Parse the input and build the filesystem tree
#!/usr/bin/env python3

# Create a dictionary to store the sizes of directories
dir_sizes = {}

# Keep track of the current directory
current_dir = "/"

# Read the input and process each line
for line in lines:
    # Split the line into words
    words = line.split()
    
    # If the line begins with "cd", change the current directory
    if words[0] == "cd":
        if words[1] == "..":
            # Move to the parent directory
            current_dir = current_dir[:current_dir.rindex("/")]
        elif words[1] == "/":
            # Move to the root directory
            current_dir = "/"
        else:
            # Move to the specified directory
            current_dir += "/" + words[1]
    
    # If the line begins with "ls", process the files and directories in the current directory
    elif words[0] == "ls":
        # Initialize the total size of the current directory to 0
        dir_sizes[current_dir] = 0
        
        # Process each file or directory in the current directory
        for i in range(1, len(words), 2):
            # If the entry is a file, add its size to the total
            if words[i + 1][-4:] != ".txt":
                dir_sizes[current_dir] += int(words[i])
            # If the entry is a directory, add its size to the total (if it has been processed already)
            else:
                dir_name = current_dir + "/" + words[i + 1][:-4]
                if dir_name in dir_sizes:
                    dir_sizes[current_dir] += dir_sizes[dir_name]

# Find all directories with a size of 100000 or less and sum their sizes
total_size = 0
for dir_name, dir_size in dir_sizes.items():
    if dir_size <= 100000:
        total_size += dir_size

# Print the result
print(total_size)
