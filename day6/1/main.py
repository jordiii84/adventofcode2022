f = open("input.txt", "r")
lines = f.read().splitlines()

class Marker():

    input_str=""

    last_chars=[]

    def __str__(self):
        return(f"{self.input_str} - {self.last_chars}")

    def is_marker(self):
        if len(set(self.last_chars))==4:
            return True
        return False

    def put_character(self,character):
        self.input_str+=character

        if len(self.last_chars)==4:
            self.last_chars.pop(0)
        self.last_chars.append(character)

    def size_string(self):
        return len(self.input_str)

marker=Marker()
for charachter in lines[0]:
    marker.put_character(charachter)
    if marker.is_marker():
        break
    
print(marker.size_string())