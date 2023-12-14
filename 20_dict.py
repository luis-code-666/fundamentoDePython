person = {
    'name': "Luis",
    'last_name': "Banda",
    'langs': ['python', 'javascript'],
    'age': 36
    }
print(person)
# en esta parte remplaza en la posicion que infdicamos 
person['name'] = 'guillermo'
print(person)
# en esta parte resta de esta manera al elemento que se esta mencionando
person['age'] -= 20
print(person)

# como aderir en un diccionario cuando tienen listas 
person['langs'].append('GO')
print(person)

# como eliminar tgenemos estas diferentes maneras

del person['las_name']
print(person)
# esto se puede eliminar con el pop y colocando su posicion para eliminarlo
person.pop('age')
print(person)

#esto debuelve una tupla 
print('items')
print(person.items())

#esto muesta las llaves osea seria la primera parte 
print('keys')
print(person.keys())

#esto muestra los valores esto muestra lo segundo 
print('values')
print(person.values())