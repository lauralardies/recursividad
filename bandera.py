# En este problema vamos a resolver el problema de la bandera de Dijkstra.

# Tenemos una fila de fichas que cada una puede ser de un único color: roja, verde o azul. Están colocadas en un orden cualquiera
# y tenemos que ordenarlas de manera que quede, de izquierda a derecha, los colores ordenados primero en rojo, luego verde y por
# último azul. La organización se obtiene mediante intercambios sucesivos, pero el color de la ficha sólo se comprueba una vez.

def intercambiar(bandera, x, y):
    temporal = bandera[x]
    bandera[x] = bandera[y]
    bandera[y] = temporal

def permutar(bandera, i, j, k):
    if k != j:
        if bandera[j+1] == "R":
            intercambiar(bandera, i+1, j+1)
            permutar(bandera, i+1, j+1, k)
        elif bandera[j+1] == "V":
            permutar(bandera, i, j+1, k)
        elif bandera[j+1] == "A":
            intercambiar(bandera, j+1, k)
            permutar(bandera, i, j, k-1)
        else: 
            print("Has introducido una ficha inválida")
            exit()

    return bandera

bandera = [""]
n = int(input("Introduce el número de elementos que quieres en tu bandera a ordenar: "))
print("Ahora introduce las fichas aleatoriamente (ficha roja = R, ficha verde = V, ficha azul = A)")
for i in range (0, n):
    ele = input()
    ele = ele.capitalize()
    bandera.append(ele)

bandera_ordenada = permutar(bandera, 0, 0, len(bandera) - 1)
bandera_ordenada.pop(0)

print("¡Esta es tu bandera ordenada!\n" + str(bandera_ordenada))