website="https://www.sadikturan.com"
course="Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

#1
hello=' Hello World '
print(hello)
hello2=hello.strip()
print(hello2)

#2
sadik='www.sadikturan.com'
print(sadik)
sadik2=sadik.replace('www.','').replace('.com','')
print(sadik2)
sadikList=sadik.split('.')
print(sadikList[1])

#3
print(course)
course2=course.lower()
print(course2)

#4
counta=website.count('a')
print(counta)

#5
isFound=website.startswith('www')
isFound2=website.endswith('com')
print(isFound)
print(isFound2)

#6
isSearch=website.find('.com')
print(isSearch)

#7
isAlphabetic=course.isalpha()
alfakurt='abcdefg'
isAlfakurt=alfakurt.isalpha()
print('Alfabetik mi?',isAlphabetic)
print('Alfakurt',isAlfakurt)
print('1234'.isdigit())


#8
print('Contents'.center(50,'*'))
print('Contents'.ljust(50,'*'))
print('Contents'.rjust(50,'*'))

#9
print(course.replace(' ','-'))

#10
print(hello.replace('World','There'))

#11
print(course.split(' ')[2])
