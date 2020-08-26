with open("newfile.txt","r",encoding="utf-8") as file:
    content=file.read()
    print(content)
    print(file.tell())
    file.seek(0) #Cursor returns to the given index
    print(file.tell())
    content2=file.read(10) #Returns first 10 index
    print(content2)
