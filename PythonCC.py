import sys #python library
#creation of the ceaser cypher

letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#length = 26 letters of alph

shift = sys.argv
#shift = int(input("Enter the number of character shifts wanted: "))

message = input("Input message: ")
message= message.upper()
empty_string = ""
minimum_shift = 27 - shift

for i in sys.stdin:
    if i == " ":
        empty_string += i
    else:
        for j in i:
            position = letters.index(j)
            if position < minimum_shift:
                position = position + shift
                empty_string+= letters[position]
            elif position >= minimum_shift:
                position = position + shift - 26
                empty_string += letters[position]
length = len(empty_string)
counter = 0
