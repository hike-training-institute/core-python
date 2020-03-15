
file_obj = open('names.txt' ,mode='a+')
file_obj1 = open('names.txt' ,mode='a+')

# for i in file_obj.readlines():
#     print(i)

file_obj.write("Mani Ratnam\n")
file_obj1.write("Goutham Menon \n")

file_obj1.close()
file_obj.close()

with open('names.txt' ,mode='a+') as f :
    f.write("Narendra Modi\n")











