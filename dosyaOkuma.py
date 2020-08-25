'''
try:
    file=open("newfile2.txt","")
    print(file)
except: FileNotFoundError: print("Dosya Okuma Hatası")
###
file=open("newfile.txt","r",encoding="utf-8")
for i in file:
    print(i,end="")
file.close()
'''
###
file=open("newfile.txt","r",encoding="utf-8")
content1=file.read()
print("İçerik 1")
print(content1)
content2=file.read()
print("İçerik 2")
print(content2)
file.close()
