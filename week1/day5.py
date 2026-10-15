weekly_steps=[9200, 7400, 10500, 8800, 6900, 11000, 9600]
for steps in weekly_steps:
    if steps >=8000:
        print(steps, '- Goal hit')
    else:
        print(steps, '- Below goal')
print('Days tracked:', len(weekly_steps))

skills=['welding', 'tiling', 'upholstery']
print('Before', skills)
skills.append('mechanicist')
print('After', skills)
habits=['jogging', 'walking', 'reading', 'calling', 'working']
print('These are my habits:', habits)
habits.append('dreaming')
print(habits)
habits.append('baking')
print(habits)
habits.insert(3,'printing')
print(habits)
habits.remove('calling')
print(habits)
print('This week steps:', weekly_steps)


