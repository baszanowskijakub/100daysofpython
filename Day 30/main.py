# FileNotFound
try:
    file = open("a_file.txt")
except:
    file = open("a_file", "w")
    file.write("Something")

# KeyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["faasafs"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

