#open("newfile.txt","r")
#aynı dizinde bu dosya bulunmadığında çalışmaz
#result=open("newfile.txt","w")
#print(result)
#file=open("newfile.txt","w")
#file.close()
file =open("newfile.txt","a",encoding="utf-8")
file.write("\nSadık Turan")
file.close()
