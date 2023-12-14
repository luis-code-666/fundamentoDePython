my_dict = {}
print(type(my_dict))

my_dict = {
    'avion': "bla bla bla",
    'name': "Luis",
    'last_name': "Banda",
    'age': 30
}
print(my_dict)
print(len(my_dict))

print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age'))  # el get no muestra error solo lo deja corre no es como el que no se pone el get y muestra un error y no deja que corra el sistema 

print('avion' in my_dict) # esto sirve para que no muestre un error y paralice el sistema 
print('otroqueno' in my_dict)