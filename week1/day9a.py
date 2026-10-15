def show_daily_goal():
    print('step goal: 8000 steps')
    print('water goal: 8 glasses')
    print('cold shower:yes')
show_daily_goal()
print('****')
show_daily_goal()
print('####')
show_daily_goal()
print('====')
def get_greeting():
    return'Hello from a pal'
msg=get_greeting()
print(msg)
print('&&&&')
def my_function(fname):
    print(fname + 'Ithibu')
my_function('Robert ')
my_function("Jeniffer ")
my_function('Anthony ')
my_function('Stephen ')
print('$$$$$')
def check_steps(steps):
    if steps >=10000:
        print(steps, 'steps - Goal exceeded')
    elif steps>=8000:
        print(steps, 'steps - Goal hit')
    else:
        print(steps, 'steps - Below goal') 
check_steps(9200)
check_steps(7500)
check_steps(11000)
print('++++++')
def log_day(day,steps,protocol):
    print(f'{day}: {steps} steps | protocol:{protocol}')
log_day('Monday', 9200, 'OMAD')
log_day('Tuesday', 10500, '2MAD')
log_day('Wednesday', 8800, 'Autophagy Marathon')
print('>>>>')
def my_function(y="x"):
    print('Hello', y)
my_function()
my_function("Rose")
my_function('John')
my_function('Phil')

def my_function(first_name,second_name='Steve'):
    print('hello', first_name, second_name)
my_function('Joseph',' Mwangi')
my_function('James', 'Kamau')
my_function('philo' 'Chege')

def my_function(fname):
    print('Hello ', fname + ' Mbugua')
my_function('Timon')
my_function('Benita')
my_function('Joseph')

def myfunction(fname):
    print('hello', fname + ' Kamau')
myfunction('John Mwangi')
myfunction("Chloe Njeri")

def myfunction(country='Kenya'):
    print('Hello I am from', country)
myfunction('Ghana.')
myfunction('Japan.')
myfunction('Sudan')

def myfunction(animal,name):
    print('I have a', animal)
    print('My', animal + "'s name is", name)
myfunction(animal='dog', name='Tico')