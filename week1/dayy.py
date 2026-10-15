import csv
import json
import io
shopping_list = ['milk', 'eggs', 'dabur',
                 'butter', 'nuts', 'sugar', 'salt']
for item in shopping_list:
    if item != 'butter' and item != 'sugar':
        print(f'{item} in stock')
    else:
        print(f'{item} is out of stock')

students = [{'name': 'Stephen Mbugua', 'age': 22, 'gender': 'male', 'city': 'Nakuru'},
            {'name': 'Peter Gitau', 'age': 25, 'gender': 'male', 'city': 'Nairobi'},
            {'name': 'Moses Muniu', 'age': 20, 'gender': 'male', 'city': 'Nakuru'},
            {'name': 'linews Kurgat', 'age': 23, 'gender': 'male', 'city': 'Nakuru'}]
for student in students:
    if student['city'] == 'Nakuru':
        print(f'{student['name']} is from {student['city']} and he has an electrical background'
              f' working for KENYA ORDNANCE')
    else:
        print(f'{student['name']} is from {student['city']} and he has an electrical background'
              f' but does not work for KENYA ORDNANCE')
count = 0
for number in range(1, 15):
    if number % 2 == 1:
        count += 1
        print(number)
print(f'we have {count} odd numbers')


def greet():
    print("Hi there")
    print('Feel at home')


greet()


def greet(fname, lname):
    print(f'Hi {fname} {lname}')
    print('welcome home')


greet('Benita', 'Wangui')
greet('Timon', 'Ithibu')


def increment(number, by):
    return number + by


print(increment(2, by=18))


def increment(number, by=6):
    return number + by


print(increment(3, 2))


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        print(number)
    return total


print(multiply(2, 3, 4, 5))


def greet(name):
    print(f'Hello {name}')


greet('Amerix')
greet('SMP Member')
greet('Guest')
print('////////')
file_content = io.StringIO()
file_content.write('steps: 9200\n')
file_content.write('water: 8glasses\n')
file_content.write('protocol: OMAD\n')
file_content.write('cold shower : yes\n')

print('File written.contents:')
print(file_content.getvalue())

print('\\///')

file_data = """steps: 9200
water:8 glasses
protocol:OMAD
cold shower: yes
 sleep houre:8 """
f = io.StringIO(file_data)
content = f.read()
print('FULL FILE CONTENT:')
print(content)

print('XXXXXX')

x = '{"name":"John", "age": 33 , "city": "Nakuru"}'
y = json.loads(x)
print(y['age'])
print(y['city'])

l = {"name": "John", "age": 33, "city": "Nakuru"}
p = json.dumps(l, indent=2, separators=(".", "="))
print(p)

print('XXXXX')
daily_log = {"steps": 17341, "water glasses": 8,
             "cold shower": True, "sleeping hours": 7.5}
# convert to JSON string
json_text = json.dumps(daily_log)
print("type", type(json_text))
print("JSON", json_text)

# print with indentation
pretty = json.dumps(daily_log, indent=2)
print("\nprettyJSON", pretty)

print('\n')
# convert to python
daily_logg = '{"steps": 17341, "water glasses": 8, "cold shower": true, "sleeping hours": 7.5}'
data = json.loads(daily_logg)
print("Steps:", data["steps"])
print('Water glasses', data['water glasses'])
print('\n')

# simulate writing
daily_loggs = {"steps": 17341, "water glasses": 8,
               "cold shower": True, "sleeping hours": 7.5}
json_string = json.dumps(daily_loggs, indent=2)
print('saved JSON:')
print(json_string)

# simulate reading it back
loaded_data = json.loads(json_string)
print('\nRead back as python dict:')
for key, value in loaded_data.items():
    print(f'{key}: {value}')
print('\n')

# simulate with nested data
api_json = ''' {"client": "James Omondi", "week":1, "daily_log": [{"day":"Monday", "steps": 8341, "water glasses": 8, "cold shower": true, "sleeping hours": 7.5}, {"day":"Tuesday", "steps": 17341, "water glasses": 8, "cold shower": true, "sleeping hours": 7},{"day":"Wednesday", "steps": 9341, "water glasses": 8, "cold shower": true, "sleeping hours": 7},{"day":"Thursday", "steps": 17341, "water glasses": 8, "cold shower": true, "sleeping hours": 7.5},{"day":"Friday", "steps": 17341, "water glasses": 8, "cold shower": true, "sleeping hours": 7.5},{"day":"Saturday", "steps": 17341, "water glasses": 8, "cold shower": true, "sleeping hours": 7.5},{"day":"Sunday", "steps": 17341, "water glasses": 8, "cold shower": true, "sleeping hours": 7.5}]}'''
data = json.loads(api_json)
print("Client:", data["client"])
print("Week:", data["week"])
for log in data["daily_log"]:
    status = "Good" if log["steps"] >= 8000 else "Bad"
    print(f"{log['day']}: {log['steps']} steps ({status})")
    print(f"{log['day']}: {log['water glasses']} water glasses")
print('\n')
# A welding workshop stores job records as JSON.
job_json = '''{"workshop": "Gatimu metalworks", "location": "Nakuru",
"jobs":[{"client": "Irene", "item":"gate", "material": "mild steel", "paid": true},
{"client": "Muiga", "item":"window grills",
    "material": "angle iron", "quote_kes": 8000, "paid": false},
{"client": "Rono", "item": "door frame", "material": "hollow tube", "quote_kes": 12000, "paid": true}]}'''
data = json.loads(job_json)
print("workshop:", data['workshop'])
print("location:", data['location'])
print()

total = 0
paid = 0
for job in data['jobs']:
    status = "PAID" if job['paid'] else "NOT PAID"
    print(f"{job['client']}: {job['item']}")
print('\n')


csv_data = """name,phone,skill,city 
James Kamau, 07245,welding, Nairobi
Sandra Mueni, 07456, officer, Kitui
patrick Otieno, 07948, technician, Migori 
Alex Mwala, 07534, capentery, Ruiru"""
f = io.StringIO(csv_data)
reader = csv.reader(f)
for row in reader:
    print(row)
print('\n')

csv_data = """name,phone,skill,city
James Kamau, 07245, welding, Nairobi
Sandra Mueni, 07456, officer, Kitui
patrick Otieno, 07948, technician, Migori
Alex Mwala, 07534, capentery, Ruiru"""
f = io.StringIO(csv_data)
reader = csv.reader(f)
next(reader)  # skip header row
for row in reader:
    name, phone, skill, city = row
    print(f"{name}  {skill}  {city}")

print('\n')
csv_data = """name,steps,water,protocol,cold_shower
Ann Karuti, 8900, 8,OMAD,True
Evans Kipto, 13900,9,2mad,True
John Kiarie, 13567,9,OMAD,False
Grace Aloo, 6780,7,Autophagy Marathon,True"""
f = io.StringIO(csv_data)
reader = csv.DictReader(f)

for row in reader:
    steps = int(row["steps"])
    status = "Goal hit" if steps >= 8000 else "Below goal"
    print(f"{row['name']}: {steps} steps | {row['protocol']} | {status}")
print('\n')

output = io.StringIO()
writer = csv.writer(output)
# write header
writer.writerow(["name", "steps", "protocol", "goal_hit"])
# write data row
data = [["James", 9200, "OMAD", True],
        ["Sandra", 10500, "2MAD", True],
        ["Patrick", 7600, "OMAD", False],
        ["Grace", 11000, "Autophagy Marathon", True],]
for row in data:
    writer.writerow(row)
print("Generated csv:")
print(output.getvalue())
print("\n")

clients = [{"name": "James", "skill": "welding", "city": "Nairobi", "sessions": 4},
           {"name": "Sandra", "skill": "tiling", "city": "Mombasa", "sessions": 3},
           {"name": "Grace", "skill": "copywriting", "city": "Kisumu", "sessions": 2},]
output = io.StringIO()
fieldnames = ["name", "skill", "city", "sessions"]
writer = csv.DictWriter(output, fieldnames=fieldnames)
writer.writeheader()
writer.writerows(clients)
print(output.getvalue())
print('\n')

harvest_csv = """field,crop,harvested_bags,target_bags
Northplot,maize,48,50
Southplot,beans,22,30
centre plot,sorghum,44,40"""

reader = csv.DictReader(io.StringIO(harvest_csv))
print(f"{'Field':<15} {'crop':<10} {'Harvested':>10} {'Target':>8} {'Status':>12}")
print("-" * 60)
for row in reader:
    harvested = int(row["harvested_bags"])
    target = int(row["target_bags"])
    pct = (harvested / target) * 100
    status = "On target" if harvested >= target else f"short by {target - harvested} bags"
    print(
        f"{row['field']:<15} {row['crop']:<10} {harvested:>10} {target:>8} {status:>12}")
print('\n')


csv_data = """name,score1,score2,score3
James,85,90,78
Sandra,72,,88
patrick,91,87,94
Grace,60,bad data,70
Brian,55,48,62"""

f = io.StringIO(csv_data)
reader = csv.DictReader(f)
for row in reader:
    print(dict(row))
