# Búsqueda Binaria en Lista de Palabras 

# Utiliza una búsqueda binaria para encontrar la posición de una palabra específica 

# en una lista ordenada de palabras.

   # busqueda binaria
#  Retorna la posición del valor en la lista en caso de ser encontrado y el número de intentos.
    # La lista debe estar ordenada para qué funcione la búsqueda. """
 



def busqueda_binaria(lista,buscado): # definir busqueda binaria toma 2 parametros(lista a buscar y elemento buscado)
    inicio=0                         # variable inicio =indice 0 de la lista
    final=len(lista)-1               # tamaño de la lista (porque el ultimo elemento de la lista se encuentra en el tamaño de la lista -1)

    while inicio <=final:
        medio=(inicio+final)//2      # indice que esta en medio de la lista
        if lista[medio]==buscado:    # comprobar si el elemento de la lista que esta en el indice medio es igual al elemento buscado
            return medio
        elif lista[medio]<buscado:
            inicio=medio+1
        else:
            final=medio-1
            return -1                 # reorna -1 porque no encontro el elemento
    
        


        # ejemplo de uso

        lista=['avion','coche','gato','hola','manzana','perro']
        buscado='manzana'
        resultado=busqueda_binaria(lista,buscado)
        if resultado==-1:
            print(f"el elemento{buscado}no se encuentra en la lista")
        else:
            print(f"el elemento{buscado}se encuentra en la posicion{resultado}")

            
        

            
 
 

          
    

        


    

              
      

      

  
