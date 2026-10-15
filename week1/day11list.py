weekly_steps=[9200,7500,10500,8800,6900,11000,9600]
goal_days=[]
for steps in weekly_steps:
    if steps>=8000:
        goal_days.append(steps)
        print(goal_days)

print('########')

weekly_steps=[9200, 7500, 10500, 8800, 6900, 11000, 9600]
goal_days = [steps for steps in weekly_steps if steps >= 8000]
print(goal_days)

print('$$$$$$')

weekly_steps=[9200, 7500, 10500, 8800, 6900, 11000, 9600]
#convert each step count to km
km_walked=[round(s * 1.3/1000,2) for s in weekly_steps]
print('steps:', weekly_steps)
print('KM :', km_walked)

print('\\\\\\')

#build a list of status strings for each day
statuses=['Goal hit' if s >=8000 else "Below" for s in weekly_steps]
for i, status in enumerate(statuses):
    print(f'Day {i+1}: {weekly_steps[i]} steps - {status}')