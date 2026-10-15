def check_steps(steps, goal=8000):
    if steps<=goal:
        print(f"{steps} steps - Goal of {goal} hit.")
    else:
        print(f"{steps} steps - Goal of {goal} missed.")
    # uses default goal of 8000 
check_steps(9200)
check_steps(7500)
# override the default goal
check_steps(9200, goal=10000)
check_steps(11500, goal=10000)

def log_day(steps, water=8, protocol='OMAD'):
    print(f'steps:-{steps} | water:- {water} glasses | protocol:-{protocol}')
log_day(9200)
log_day(10500, water=9)
log_day(8800,water=7, protocol='2MAD')

def client_report(name, goal, sessions=4, bench_kg=80 ):
    print(f'{name} | Goal: {goal} | Sessions/week: {sessions} | Bench: {bench_kg}KG')
client_report('George', 'fat loss')
client_report(goal='muscle gain', name='Stephen', bench_kg=100)
client_report('Lucy', 'endurance, bench_kg=30')

step_goal=8000
def check_today(steps):
    result='hit' if steps>=step_goal else 'missed'
    print(f'Goal {result}: {steps} steps')
check_today(9200)
check_today(7000)

def calculate_bmi(weight_kg, height_m):
    bmi=weight_kg/(height_m**2)
    return round(bmi, 1)
def bmi_category(bmi):
    if bmi < 18.5:
        return 'underweight'
    elif bmi < 25:
        return 'normal'
    elif bmi < 30:
        return 'overweight'
    else:
        return 'obese'
weight=75
height=1.7
bmi=calculate_bmi(weight, height)
category=bmi_category(bmi)
print(f'Weight: {weight}kg | Height: {height}m')
print(f'BMI: {bmi}| category: {category}')
