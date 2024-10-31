# Listas
lista = [] #Definir una lista vacia
print(lista)
lista1 = [1,2,3,4,5,"hola",4.5] # Una lista heterogenea
print(lista1)

#Enlazar las listas
lista2 = [0,1,2,3]
lista3 = ["A","B","C"]
lista4 = [lista2,lista3]
print(lista4)


#Concatenacion
listas = ["A", "B", "C", "E"]
lista9 = [1,2,3,4,5]
lista10 = listas + lista9
print(lista10)
print(lista10[2])

#El metodo extend agrega una lista al final de otra lista, la operacion afecta la lista invocante
nombres1 =["Antonio", "Maria", "Mabel"]
nombres2 =["Barry", "John", "Guttag"]
nombres3 =["Barry", "John", "Guttag"]
nombres1.extend(nombres2)
print (nombres1)
print (nombres2)


#Operaciones de listas
#repetir
lista10 = [1, 2, 3, 4, 5]
lista11 = lista10*3
print(lista11)

#comparacion
#usando los operadores convencionales(<, <=, >, >=, ==, !=)
print(['Rojas', 123] < ['Rosas', 123])
print(['Rosas', 123] == ['rosas', 123])
print(['Rosas', 123] > ['Rosas', 23])

#Es posible determinar si un elemento se encunetra en una lista
lista12 = ['cien', 'años', 'de', 'soledad']
if 'de' in lista12:
    print('Si esta en la lista')
else:
    print('No esta en la lista')

#Iterando una lista
lista13 = ['hola', 'amigos', 'mios']
for palabra in lista13: #para cada palabra de la lista
    print(palabra, end=',') # end evita salto de linea



