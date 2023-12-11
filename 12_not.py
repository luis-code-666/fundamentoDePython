print(not True)
print(not False)

print("NOT AND")
print('not True and True => ', not (True and True))
print('not True and True => ', not (True and False))
print('not True and True => ', not (False and True))
print('not True and True => ', not (False and False))

stock = input('Ingrese el numero de stock => ')
stock = int(stock)

print(not (stock >= 100 and stock <=10000))