number = (1, 2, 3, 5)
string = ('nico', 'zule', 'santis', 'nico')
print(number)
print('0 => ', number[0])
print('-1 => ', number[-1])
print(type(number))

print(string)
print(type(string))

#CRUD
# munber.append(10)
print(number)

#number[1] = 'change'

print(string)
print(string.index('zule')) # adiere a la tupla un string
print(string.count('nico'))  # cuenta cuantos elementos contiene

my_list = list(string) # transforma de tuplas a listas con este codigo
print(my_list)
print(type(my_list))

my_list[1] = 'juli'  # adiere un elemento a la lista
print(my_list)

my_tuple = tuple(my_list) # convierte una lista a tupla con esta linea de codigo 
print(my_tuple)
print(type(my_tuple))
