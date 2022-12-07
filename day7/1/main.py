
class File():
    name=""
    size=0

    def __init__(self, name, size):
        self.name=name
        self.size=size

    def __len__(self):
        return self.size

    def __str__(self):
        return self.name

class Directory():
    name=""
    directories=None
    files=None
    parent=None
    smalldirs=[]

    def __init__(self, name):
        self.name=name
        self.directories=[]
        self.files=[]

    def __str__(self):
        return self.name
    
    def get_directory(self, name):
        for directory in self.directories:
            if directory.name == name:
                return directory

    def append_directory(self, directory):
        directory.parent=self
        self.directories.append(directory)

    def append_file(self, file):
        self.files.append(file)

    def contains_directory(self, name):
        for directory in self.directories:
            if directory.name==name:
                return True
        return False

    def size(self):
        size=0
        for file in self.files:
            size+=file.size
        for dir in self.directories:
            size+=dir.size()
        return size

    def print_tree(self):
        print(f"{self.name} - {self.size()}")
        print("------_Directories---------")
        for directory in self.directories:
            directory.print_tree()
        print("------_Files......---------")
        for file in self.files:
            print(f"{file} - {file.size}")

    def get_small_dirs(self):
        if self.size()<=100000:
            self.smalldirs.append(self)
        for directory in self.directories:
            directory.get_small_dirs()
        return self.smalldirs

f = open("input.txt", "r")
lines = f.read().splitlines()

def is_command(line):
    return line.startswith("$")


current_folder=""
current_directory=None
root_node=None
for line in lines:
    if is_command(line):
        if line=="$ cd ..":
            print(f"Exiting from directory {current_directory} to {current_directory.parent}")
            current_directory=current_directory.parent
        elif line.startswith("$ cd "):
            current_folder=line.split("$ cd ")[1]
            if current_folder=="/":
                directory=Directory("/")
                current_directory=directory
                root_node=current_directory
                print(f"Entering directory {current_directory.name}")
            elif current_directory is not None and not current_directory.contains_directory(current_folder):
                directory=Directory(current_folder)
                current_directory.append_directory(directory)
                current_directory=directory
                print(f"Entering directory {current_directory.name}")
    else:
        if not line.startswith("dir"):
            file=File(line.split(" ")[1],int(line.split(" ")[0]))
            current_directory.append_file(file)
            print(f"Appending file {line.split(' ')[1]} to directory {current_directory.name}")

root_node.print_tree()
smalldirs=root_node.get_small_dirs()

sum_size=0
for dir in smalldirs:
    sum_size+=dir.size()
print(sum_size)
# print(smalldirs)
# directory=root_node.get_directory("d")
# print_tree(directory)