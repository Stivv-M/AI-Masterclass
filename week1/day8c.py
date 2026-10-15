contacts=[{'name':'James Omondi', 'phone': '0988757574', 'skill':'welding', 'city':'Kisumu'},
          {'name':'Sandra weru', 'phone':'09876545', 'skill': 'tiling', 'city':'Mombasa'},
          {'name':'patrick njiru', 'phone':'098877664', 'skill': 'driving', 'city':'Embu'},
          {'name':'Grace Avemo', 'phone':'099886456', 'skill':'copywriting','city':'Eldoret'},
          {'name':'Brian kamau', 'phone':'0988387983','skill':'upholstery', 'city':'Kiambu'}]
print('contacts stored:', len(contacts))
print(contacts[0])
print('***CONTACT BOOK***')
for x,contact in enumerate(contacts):
    print(f'\n{x+1}.{contact['name']}')
    print(f'phone:{contact['phone']}')
    print(f'skill:{contact['skill']}')
    print(f'city:{contact['city']}')
search_city='Kisumu'
print(f'contacts in {search_city}:')
for contact in contacts:
    if contact['city']==search_city:
        print(f'{contact['name']} | {contact['skill']} | {contact['phone']}')
search_skill='driving'
print (f'contacts in {search_skill}:')
for contact in contacts:
    if contact['skill']==search_skill:
        print(f'{contact['name']} | {contact["phone"]} | {contact["city"]}')
new_contact={'name':'Kevin Mwangi', 'phone':'0876543','skill':'beekeeping','city':'Meru'}
contacts.append(new_contact)
print('###CONTACT BOOK###')
for x,contact in enumerate(contacts):
    print(f'\n{x+1}*{contact['name']}')
    print(f'phone:{contact['phone']}')
    print(f'skill:{contact['skill']}')
    print(f'city:{contact['city']}')
