import unicodedata

class Palindromo():

    def __init__(self, frase) -> None:
        self.frase_inicial = frase
        self.frase_mod = frase

        self.frase_mod = self.alfanumerico(self.frase_inicial) # Eliminamos aquellos elementos que no sean alfanuméricos.
        self.frase_mod = self.mayusculas(self.frase_mod) # Cambiamos las mayúsculas a minúsculas.
        self.frase_mod = self.acento(self.frase_mod) # Eliminamos los acentos.

        self.resultado = self.es_palindromo(self.frase_mod) # True si es palíndromo, False si no lo es.
        
    def alfabetico(self, c): # Reconoce si un elemento es letra (True) o no (False).
        return str(c).isalpha()
    
    def cifra(self, c): # Reconoce si un elemento es cifra (True) o no (False).
        return str(c).isdigit()

    def alfanumerico(self, ca): # Esta función reconoce los elementos alfanuméricos de una frase y estos se van almacenando en la variable que hemos llamado resultado.
        resultado = ""

        if len(ca) == 0: # Nos salimos cuando hayamos analizado todos los elementos de nuestra frase.
            return resultado 

        if self.alfabetico(ca[0]) == True or self.cifra(ca[0]) == True: # Si es letra o cifra se almacena en el resultado y seguimos con el siguiente elemento.
            resultado = ca[0] + self.alfanumerico(ca[1:])
        else: # No es ni letra ni cifra y por lo tanto, se elimina.
            resultado = self.alfanumerico(ca[1:])
        
        return resultado

    def mayusculas(self, ca): # Esta función cambia todos los elementos de la frase a minúscula.
        return str(ca).lower()

    def acento(self, ca): # Esta función elimina todos los acentos de la frase, dejando las letras acentuadas sin acentuar.
        return ''.join((c for c in unicodedata.normalize('NFD', ca) if unicodedata.category(c) != 'Mn'))

    def es_palindromo(self, ca): # Esta función compara si nuestra frase modificada es igual a su imagen.
        if ca == ca[::-1]: # Si la condición se cumple, nuestra frase es un palindromo(True).
            return True
        else: # De lo contrario, no es un palíndromo (False).
            return False

while True:
    frase = input(" Introduce una frase cualquiera: ")
    p = Palindromo(frase)
    # En caso de que se introduzca un frase vacía o con sólo espacios, debemos saber identificarla porque sino el resultado que nos devuelve es que la frase es un palíndromo.
    if len(p.frase_mod) == 0: 
        print("¡Esto no es una frase!")
        exit()
    else:
        if p.resultado == True:
            print("Esta frase es un palindromo.")
        else:
            print("Esta frase no es un palindromo.")

    respuesta = input("¿Quieres mirar otra frase? [Y]/N: ")
    respuesta = respuesta.capitalize()
    if respuesta == "N":
        break