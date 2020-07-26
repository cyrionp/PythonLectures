website="https://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

courseLen=len(course)
print(f"Course dizisinde {len(course)} tane karakter bulunmaktadır.")
print(f"Course dizisinde {courseLen} tane karakter bulunmaktadır.")

print(f"{website[8:11]}")

websiteLen=len(website)
print(f"{website[len(website)-3:len(website)]}")
print(f"{website[websiteLen-3:websiteLen]}")

print(f"{course[0:14]} 'and' {course[courseLen-14:]}")

print(f"{course[::-1]}")

name, surname, age, job='Sude Sezen','Gengenç',26,'YÜKSEK YAZILIM MÜHENDİSİ'
print(f"Onun adı {name} {surname}, yaşı {age} ve o bir {job}!")

hello='Hello world'
print(hello)
result=hello[0:6]+'W'+hello[-4:]
print(result)

abc='abc'*3
print(f"{abc}")
