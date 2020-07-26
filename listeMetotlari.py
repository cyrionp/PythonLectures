numbers=[1,10,5,16,4,9,10]
letters=['a','g','s','b','y','a','s']
print(min(numbers))
print(max(numbers))
print(min(letters))
print(max(letters))

print(numbers[3:6])

numbers[4]=40
print(numbers)

numbers.append(49)
print(numbers)

numbers.insert(2,30) #ilk yazılan indexe ikinci yazılan eklenir
print(numbers)
numbers.insert(-1,999)
print(numbers)

numbers.pop(-1)
print(numbers)

numbers.remove(10)
print(numbers)

numbers.sort()
print(numbers)
letters.sort()
print(letters)

numbers.reverse()
print(numbers)
letters.reverse()
print(letters)

print(numbers.count(10))
print(letters.count('a'))

numbers.clear()
print(numbers)
