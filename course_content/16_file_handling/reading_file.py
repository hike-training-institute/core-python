file_obj = open('names.txt' ,mode='a+')
file_obj1 = open('names.txt' ,mode='a+')

# print(dir(file_obj))
# for i in file_obj.readlines():
#                print(i)
# print(file_obj)

# print(file_obj.mode)
file_obj1.write("Goutham Menon \n")
file_obj.write("Mani Ratnam\n")

file_obj1.close()
file_obj.close()

#Write happens at the time of close command only, not when the write line is executed it can be observed by changing the
# sequence of close commands.
# If we dont give close command, the file is auto closed after the full code execution and
# write will be done in a sequence same as the sequence objects were opened.

with open('names.txt' ,mode='w') as f :
    f.write("Narendra Modi\n")