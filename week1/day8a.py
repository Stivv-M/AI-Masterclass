contacts = [{'name': 'Stephen Mbugua', 'phone': '0722542814', 'skill': 'programmimg', 'city': 'Nakuru'}, {'name': 'Peter Gitau', 'phone': '0729352789', 'skill': 'cybering', 'city': 'Nairobi'}, {
    'name': 'Moses Muniu', 'phone': '0721354254', 'skill': 'baking', 'city': 'Kiambu'}, {'name': 'linews Kurgat', 'phone': '0716512521', 'skill': 'packaging', 'city': 'Eldoret'}]
print("==== CONTACT BOOK ====")
for i, contact in enumerate(contacts):
    print(f"\n{i+1}.{contact['name']}")
    print(f"  phone : {contact['phone']}")
    print(f"  skill : {contact['skill']}")
    print(f"  city : {contact['city']}")
