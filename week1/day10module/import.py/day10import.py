from datetime import datetime, date
import random
import math
# square root
print('square root of 144:', math.sqrt(144))
# round down and round up
print('floor of 7.9:', math.floor(7.9))
print('ceiling of 7.1:', math.ceil(7.1))
# pi
print('pi:', math.pi)
# power : 2 to the power of 10
print('2 to the 10th:', math.pow(2, 10))

print('random number:', random.randint(1, 10))
print('random float:', random.random())
skills = ['welding', 'tiling', 'upholstery', 'phone repair', 'copywriting']
print("Today's skill focus:", random.choice(skills))
random.shuffle(skills)
print('shuffled:', skills)

print('\033[4m simulated step counts for this week: \033[0m')
days = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
for day in days:
    steps = random.randint(5000, 13000)
    status = 'OK' if steps >= 8000 else 'low'
    print(f'{day}: {steps} steps({status})')

# today's date and time
now = datetime.now()
print('current datetime:', now)
# just the date
today = date.today()
print('today:', today)
print('year:', today.year)
print('month:', today.month)
print('day:', today.day)
# days between two dates
start = date(2026, 1, 1)
end = date(2026, 12, 31)
delta = end-start
print('days in 2026:', delta.days)
