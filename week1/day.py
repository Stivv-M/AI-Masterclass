import math
course = 'python pragramming'
print(len(course))
print(course[1])
print(course[2:16])
print(course[:9])
print(course[6:])
article = "The \"boy was there \n what boy?"
print(article)
first = 'Steve'
last = 'Mbugua'
full = first + " " + last
fully = f'{first} {last}'
print(full)
print(fully)
print(course.upper())
print(course.title())
print(article.title())
print(course.find('pra'))
print(course.replace('a', 'o'))
print(course.replace('y', 'i'))
print('pra' in course)
print('pro' in course)
print(course, '\N{face with tears of joy}')

print(10//3)
print(10 % 3)
x = 10
x += 3
print(x)
print(round(2.3))
print(abs(8.9))
print(abs(-78))

print(math.ceil(2.3))
print(math.ceil(2.7))
print(math.fabs(2.7))
print(math.floor(2.7))
x = '2'
y = int(x)+7
print(f'x: {x} y:{y}')

temperature = 20
if temperature > 34:
    print('doff sweater')
    print('drink water')
elif temperature <= 20:
    print('don sweater')
    print('on heater')
    print("don't go out")
    print('close doors')
elif temperature < 10:
    print('eat matoke')
    print('switch AC')
else:
    print('put on music')

age = 22+9
message = 'no marriage' if age <= 27 else 'marry'
print(message)

for number in range(1, 10, 3):
    print('tried', number, (number) * ',')

successful = False
for number in range(4):
    print('attempt')
    if successful:
        print('successful')
        break
else:
    print('attempted 4 times and failed-Sorry')

for x in range(5):
    for y in range(3):
        print(f'({x},{y})')

shopping_list = ['milk', 'eggs', 'dabur',
                 'butter', 'nuts', 'sugar', 'salt', 'flour']
for item in shopping_list:
    if item == 'sugar':
        print('sugar is out of stock')
        continue
    print(item)
count = 0
for number in range(1, 20):
    if number % 2 == 0:
        count += 1
        print(number)
print(f'I have {count} even numbers')

count = 0
for number in range(1, 10):
    if number % 2 != 0:
        count += 1
        print(number)
print(f'I have {count} odd numbers')
