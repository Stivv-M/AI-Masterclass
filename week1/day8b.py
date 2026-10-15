client = {'name': 'James', 'weight-kg': 85.4, 'goal': 'fat loss',
          'fasting-protocol': '2mad', 'bench-press-kg': 80, 'weekly_sessions': 4}
print('CLIENT PROFILE')
for key, value in client.items():
    print(f'{key} * {value}')
if client['bench-press-kg'] >= 80:    print('Bench press goal achieved')
