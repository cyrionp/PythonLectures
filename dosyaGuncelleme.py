'''
with open("newfile.txt","r+",encoding="utf-8") as file: #Using r+ allows us to reading and writing on a file
    file.seek(5)
    file.write("deneme")

with open("newfile.txt","r+",encoding="utf-8") as file: #Using r+ allows us to reading and writing on a file
    print(file.read())

with open("newfile.txt","a",encoding="utf-8") as file: #Append text at finish
    file.write("\nDENEME")

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())


with open("newfile.txt","r+",encoding="utf-8") as file: #Append text at start
    content=file.read()
    content="Abdulkadir Durmaz\n"+content
    file.seek(0)
    file.write(content)
    print(content)

'''
with open("newfile.txt","r+",encoding="utf-8") as file:
    myList=file.readlines()
    myList.insert(1,"Ali Korkmaz")
    print(myList)
    for i in myList: file.write(i)
