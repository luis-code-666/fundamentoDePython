# CRUD Create, Read, Update, Delete

numbers = [1, 2, 3, 4, 5]
print(numbers[1])

numbers[-1] = 100  # con esto se actualiza el lado que se equibocaron 
print(numbers)

numbers.append(700) #esto agrega en el append en la posicion final 
print(numbers)

numbers.insert(0, 'Hola')  # esto inserta en cualquier posicion para agregar
print(numbers)

numbers.insert(3, 'change')  # esto inserta en cualquier posicion para agregar
print(numbers)

tasks = ['todo 1', 'todo 2', 'todo 3'] # esto fuciona a la lista que se agrego anteriormente
new_list = numbers + tasks
print(new_list)

#como saber en que pocision esta cada elemento 

pocision = new_list.index('todo 2')

new_list[pocision]= 'mi cambio'
print(new_list)

#como eleliminar elementos 

new_list.remove('todo 1') # con esto se elimina la posicion deacuerdo al nombre que se coloca 
print(new_list)

new_list.pop() # elimina la posicion de ultimo element sin colocar numeracion
print(new_list)

new_list.pop(0) # elimina la posicion que se le asigna numericamente 
print(new_list)

new_list.reverse() #  este sirve para colocar al sentido contrario de la lista 
print(new_list)

numbers_a = [1, 5, 6, 2]
numbers_a.sort()  #ordena con el sort 
print(numbers_a)


strings = ['re', 'ab', 'ad']
strings.sort()
print(strings)

# el sort no puede mezclar enteros con string




