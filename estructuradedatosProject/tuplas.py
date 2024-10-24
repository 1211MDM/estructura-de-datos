#Tuplas
tupla1 = () #definir una tupla vacia
print(tupla1)

tupla2 = ("Una cadena",123,4.9,True) #Una tupla heterogenea
print(tupla2)
print(tupla2[1])

tupla3 = (0,1,2,3)
tupla4 = ("A","B","C")
tupla5 = (tupla3,tupla4)
print(tupla5)
print(tupla5[0][1])
print(tupla5[1][1])
print(tupla5[1][2])

tupla6 = ("A","B","C","D","E")
tupla7 = (1,2,3,4,5)
tupla8 = tupla6 + tupla7 #concatenar
print(tupla8[3])

#repetir una tupla
tupla9 = (1,2,3,4,5)
tupla10 = tupla9 * 3
print(tupla10)

#Compara una tupla
tupla11 = ("Rojas",)
tupla12 = (123,)
tupla13 = ("Rosas",)
tupla14 = ("rosas",)
print((tupla11,tupla12) < (tupla13,tupla14))
print((tupla13,tupla14) == (tupla11,tupla12))