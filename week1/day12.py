import math
data = {"user_id": 1, "name": "James Omondi", "date": "2024-11-18", "steps": 9200,
        "water_glasses": 8, "fasting_protocol": "OMAD", "cold_shower": True,
        "sleep_hours": 7.5, "workout_completed": True}

print("name:", data["name"])
print("steps:", data["steps"])
print("water_glasses:", data["water_glasses"])
print("fasting_protocol:", data["fasting_protocol"])
print("cold_shower:", data["cold_shower"])
print("sleep_hours:", data["sleep_hours"])
print("workout_completed:", data["workout_completed"])
print("#" * 25)
print("\n")

data = {"user": {"id": 1, "name": "Sandra Wanjiku", "city": "Nairobi"},
        "metrics": {"steps": 10500, "sleeping_hours": 8, "bench_press_kg": 80},
        "skills": ["welding", "programming", "cooking", "painting"]}
print(data['user']['name'])
print(data["user"]["city"], 'Kenya')
print(data["metrics"]["steps"], 'steps')
print(data["metrics"]["bench_press_kg"], "kg bench press")
print('skills:', data["skills"])
print("first skill:", data["skills"][0])
print("user id:", data["user"]["id"])
print("#" * 25)

response = {"status": "success",
            "user": {"id": 42, "name": "Kevin Mwangi",
                     "location": {"city": "Kisumu", "country": "Kenya"}},
            "today": {"steps": 10800, "cold_shower": True, "fasting": {"protocol": "OMAD", "window_hours": 23},
                      "workout": {"completed": True, "bench_press_kg": 90, "duration_minutes": 45}}}
name = response["user"]["name"]
city = response["user"]["location"]["city"]
steps = response["today"]["steps"]
protocol = response["today"]["fasting"]["protocol"]
bench = response["today"]["workout"]["bench_press_kg"]
print(f"Name: {name}")
print(f"City: {city}")
print(f"Steps: {steps}")
print(f"Protocol: {protocol}")
print(f"Bench Press: {bench} kg")
print('\n')

name = "James"
age = 20
height = 1.75
is_student = True

print(name)
print(age)
print(height)
print(is_student)
print('\n')
age = 20

print(age > 18)

print("\n")

age = 20

print(age > 18)
print(age < 18)
print(age == 20)
print(age != 20)
print('@@@@@@@@')

age = 15
if age > 18:
    print("You are an adult")
print("This line is outside the if statement")

age = 18

if age > 18:
    print("You are an adult")
else:
    print("You are not an adult")
print('\n')
age = 18

if age > 18:
    print("You are an adult")
else:
    print("You are not an adult")
print('\n')
age = 16
student = False

if age < 18 or student:
    print("A")
else:
    print("B")
print('\n')
age = 20
student = False

if age >= 18 and student:
    print("A")
else:
    print("B")
print('######')
age = 25
student = False

if age < 18 or age > 30 and student:
    print("A")
else:
    print("B")

print('\n')
student = True

print(not student)

student = False

if student:
    print("A")
else:
    print("B")

age = 10
if age >= 18:
    print("You are an adult")
elif age >= 15:
    print("You are a teenager")
else:
    print("You are a child")
print('%%%%%%%%')
age = 16
student = False

if age >= 18:
    if student:
        print("Adult student")
    else:
        print("Adult, but not a student")
else:
    print("Not an adult")

    age = 15

while age < 25:
    print("You are not an adult")
    age = age + 2
print('%%%%%%%')
count = 3

while count < 5:
    print(count)
    count = count + 1

for name in ["John", "Mary", "Peter"]:
    print(name)
for name in ["John", "Mary", "Peter"]:
    print("Hello", name)

for number in (2, 4, 6):
    print(number * 3)
for number in (1, 2, 3):
    print(number)
    print("Hello")
for number in range(3):
    print(number + 1)

print("\n")

for number in range(2, 10, 3):
    print(number+1)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
print('%%%%%%%%')

list = ['cherry', 'mango', 'banana', 'grape']
list[2] = 'orange'
list.append('kiwi')
print(list)

fruits = ["apple", "banana", "orange"]

print("banana" in fruits)
print(fruits[1])
print("######")

items = ['apple', 'banana', 'orange ', 'grape']
print('kiwi' in items)
print('\n')
names = ["John", "Mary", "Peter"]

if "David" in names:
    print("David is here")
else:
    print("David is not here")

products = ['laptop', 'phone', 'tablet', 'monitor']
product = 'phone'

if product in products:
    print(f"{product} is available")
else:
    print(f"{product} is not available")

print('\n')

fruits = ["apple", "banana", "orange", "grape", "kiwi"]
fruits.pop()
fruits[1] = 'guava'
fruits.insert(2, 'pear')
print(fruits)

print('\n')

numbers = [1, 2, 3, 2, 4, 2, 5, 2, 2]
print(numbers.count(2))

numbers = [10, 20, 30, 20, 40]

print(numbers.index(20))

print('\n')

orders = [1001, 1002, 1003, 1004, 1005]
position = orders.index(1003)
print(f"Order 1003 is at position {position} in the list.")
print(orders[position])


print('\n')

products = ['sugar', 'salt', 'flour', 'rice', 'beans']
position = products.index('flour')
print(f'flour is at this position: {position} in the list.')

products = ["bread", "milk", "rice", "sugar"]
position = products.index("rice")
print(products[position])
print('\n')

prices = (11.99, 5.49, 3.99, 7.99)
print(max(prices))
print(min(prices))
print(sum(prices))
print(len(prices))
print('\n')

expenses = [100, 200, 150, 300, 250]
total = sum(expenses)
count = len(expenses)
average = total / count
print(f'average is {average}')
print(f"Total expenses: {total}")

print('\n')
numbers = [10, 20, 30, 40, 50]
average = sum(numbers) / len(numbers)
print(f"Average: {average}")

print('\n')

text = "I like my cat "
new_text = text.replace('cat', 'dog')
print(new_text)

print('\n')
text = "He picked up the card, looked at the card and then dropped the card on the table."
new_text = text.replace('card', 'book')
print(new_text)

print('\n')
text = "Hello Python"

print(text.find("Java"))

print('\n')
words = ' hello me'
print(words.isspace())
print(words.isdigit())
print(words.isalpha())
print(words.isalnum())

print('\n')

text = 'He picked up the boy called john, looked at the his card,\
    and called the doctor'
print(text.title())

print('\n')

names = ['John', 'Mary', 'tony', 'james']
print(names[2].capitalize())
names[2] = names[2].capitalize()
names[3] = names[3].capitalize()
print(names)
print('\n')
person = {
    "name": "John",
    "age": 25,
    "city": "Nairobi"}
print(person)
print('\n')
product = {"name": "sugar", "brand": "mumia", "weight": 5, 'color': 'brown'}
print(product['brand'])
product["weight"] = 7
print(product)
product['owner'] = 'kenya'
product.pop('color')
print(product)
print('city' in product)
if 'brand' in product:
    print('Brand exists')
else:
    print('Brand does not exist')
print(product.keys())
print(product.items())
for key, value in product.items():
    print(key, '=', value)
print(product.get('sugar'), 'not included')

print('\n')

student = {
    "name": "David",
    "age": 20, 'city': 'Nakuru'}

result = student.pop("age")
print(result)
del student['city']
print(student)
print('\n')

student = {"name": "Stephen", "age": 20}
student['course'] = 'Engineering'
student['helb'] = 'no'
student["city"] = "Nairobi"
student["age"] = 21
x = student.pop("name")

print(student)
print(x)
