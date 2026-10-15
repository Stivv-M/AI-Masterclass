daily_log={'step': 10200, 'water_glasses': 8, 'cold_shower': True, 'fasting_protocol': 'OMAD', 'sleeping_hours': 8}
print(daily_log)
print(daily_log['step'])
print('today slept hours:', daily_log['step'])
print('Fasting Method:', daily_log['fasting_protocol'])
print(daily_log.get('step'))
daily_log['pages_read']=6
print('The new dict:', daily_log)
daily_log['fasting_protocol']='2mad'
print('After updating fasting_protocol', daily_log)
daily_log['kicks']=1000 
daily_log['prayers']=3
print('Final dict', daily_log) 
del daily_log['kicks']
print(daily_log)
if 'step'in daily_log:
    print('steps recorded:', daily_log['step'])
if 'press_ups' not in daily_log:
    print('press_up not recorded yet')
for key, value in daily_log.items():
    print(key, ':', value)
thisdict={'brand':'ford', 'model':'audi', 'year': 2025, 'owner':'Mbugua'}
for key, value in thisdict.items():
    print(key, '-:',value)
for q,w in thisdict.items():
    print(q, ':', w)
