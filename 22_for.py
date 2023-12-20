for element in range(1,20):
    print (element)
    
my_list = [23,26, 68, 70]
for element in my_list:
    print(element)
    
my_tupla = ('nico', 'juli', 'santi')
for element in my_tupla:
    print(element)

product = {
    'name': 'camisa',
    'price': 100,
    'stock': 89
}
for key in product:
    print(key,  '=> ', product[key])
    
for key, value in product.items():
    print(key, '=> ', value)

people = [
    {
        'name': 'nico',
        'age': 34
    },
    {
        'name': 'zule',
        'age': 45
    },
    {
        'name': 'santi',
        'age': 4
    }
]

for person in people:
    print('name => ', person['name'])
    