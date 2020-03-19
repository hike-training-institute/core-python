
# Ex - 1
"""# r - reading the file
# r+ - read + write
# w+ - overwriting
# a+ - append

file_obj = open('names.txt' ,mode='r')
for i in file_obj.readlines():
    print(i)

file_obj.write("Hawx\n")
"""

#Ex - 2
"""file_obj = open('names.txt' ,mode='a+')
file_obj1 = open('names.txt' ,mode='a+')

file_obj1.write("Goutham Menon \n")
file_obj.write("Mani Ratnam\n")


file_obj.close()
file_obj1.close()

# Order of output depends in the close cmmnd."""

#Ex - 3
"""with open('names.txt' ,mode='a+') as f :
    f.write("Narendra Modi\n")
"""










