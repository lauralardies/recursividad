def tabla_ordenada (tabla):
    # Esta función determina si la tabla introducida está ordenada correctamente. 
    # Si está ordenada devuelve el booleano True, de lo contrario devuelve False.

    r = True 
    for i in range (len(tabla) - 1):
        if tabla[i] > tabla[i + 1]:
            r = False
            break

    return r

def dicotomia_recursiva (tabla, i, j, t):
    m = (i + j) // 2 # La posición que se encuentra en la mitad de la lista
    posicion_t = -1 # La posición todavía no se ha encontrado.

    if j >= i:
   
        if tabla[m] == t:
            posicion_t = m

        elif tabla[m] < t:
            posicion_t = dicotomia_recursiva(tabla, m+1, j, t) # Sabemos que el número es mayor que la mitad inferior de la tabla. Por lo tanto, reducimos la búsqueda.

        elif tabla[m] > t:
            posicion_t = dicotomia_recursiva(tabla, i, m-1, t) # Sabemos que el número es menor que la mitad superior de la tabla. Por lo tanto, reducimos la búsqueda.

    if (posicion_t != -1):
        return posicion_t

    if tabla[m] == t:
        posicion_t = m
    else:
        posicion_t = -1

    return posicion_t

while True:
    print("Crea una lista de números enteros de menor a mayor seguidos.")

    tabla = []
    n = int(input("Introduce el número de elementos que quieres en tu lista: "))
    for i in range (0, n):
        ele = int(input())
        tabla.append(ele)

    if tabla_ordenada(tabla) == True:
        while True:
            t = int(input("¿Qué número quieres buscar en tu tabla?: "))
            indice = dicotomia_recursiva(tabla, 0, len(tabla) -1, t)

            if indice == -1:
                print("El valor que buscas no está en la tabla introducida.")
            else: 
                print("El valor que buscas se encuentra en la posición " + str(indice) + " de la tabla.")
            
            respuesta = input("¿Quieres buscar otro número de la tabla?: [Y]/N ")
            respuesta = respuesta.capitalize()
            if respuesta == "N":
                break  
        break  

    else:
        print("Tienes que introducir una tabla ordenada.")