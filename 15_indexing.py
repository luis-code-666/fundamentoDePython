text = "Ella sabe Python"
print(text[0])
print(text[1])
#print(text[999])

size = len(text)
print('size => ', size )
print(text[size-1])
print(text[-1])

# slicing
print(text[0:5])
print(text[10:16]) 
print(text[:10]) #comienza desde el primero hasta la letra numero 10
print(text[5:-1]) # Aca puede haber un error por que el -1 no se entiende 
print(text[5:]) #comienza desde la letra numero 5 hasta el fin 
print(text[:]) #realiza el copiado desde el principio hasta el fin 
print(text[10:16:1]) #saltar un elemento
print(text[10:16:2]) #saltar dos elementos 
print(text[::2]) #saltar de dos elementos 

