fruits=['mango','banana','apple','orange','grape']
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.append('kiwi')
fruits.remove('apple')
print(fruits)
students=[{'name':'Eric', 'grade':'A'}, {'name':'Rose', 'grade':'B'}, {'name':'David', 'grade':'C'}]
print('\033[4mRESULTS\033[0m')
for s in students:
    print(f'{s['name']}:{s['grade']}')
phonebook={'Eric' : '0785674890', 'Daniel':'0758904876', 'Sarah' : '0987543235'}
print('===CONTACTS===')
for name, number in phonebook.items():
    print(f'{name}:{number}')