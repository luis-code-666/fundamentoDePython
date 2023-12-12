numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['make a dishes', 'play videogames']
print(tasks)

types = [1, True, 'Hola']
print(types)

print(numbers[0])
print(tasks[0])

# No se puede mutar una palabra con esas pociciones
text = 'hola'
#text[0] ='w'

# esto si se puede modificar en las listas para corregir lo que contenga en una lista
tasks[0] = 'watch platzi courses'
print(tasks)

tasks[0] = 'do the dishes'
print(tasks)

print(numbers[:3])
print(True in types)
print('Hola' in types)
