# ordenamiento de palabras por longitud

# Ordena una lista de palabras según su longitud, utilizando cualquier algoritmo de 

# ordenamiento que elijas.


# ordenamiento de palabras  con la funcion sorted

# tenemos una lista ,llamamos a la variable palabras  
# imprimir la representacion en cadena de caracteres de la lista 
# realizar el ordenamiento 
# para ordenar de la A-z
# llamamos la funcion sorted
# ponemos el iterable palabras(de esta manera el ordenamiento se hace a partir de las cadenas almacenadas
# en la lista palabras
# imprimir la representacion en cadena de caracteres de palabras
# obtenemos el ordenamiento alfabetico de A-Z


# A-Z

palabras=['sombrilla','raton','sol','francisco','amor','tren','dado']
print(palabras)

print()

palabras_ordenadas=sorted(palabras)
print(palabras_ordenadas)

print()


# ordenamiento de palabras por longitud (menor a mayor)(ascendente)

palabras_ordenadas=sorted(palabras,key=len)
print(palabras_ordenadas)

print()

# ordenamiento de palabras por longitud (mayor a menor)(descendente)

palabras_ordenadas=sorted(palabras,key=len,reverse=True)     # en la funcion sorted especificamos reverse=True
print(palabras_ordenadas)

print()




