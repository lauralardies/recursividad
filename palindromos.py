# En este ejercicio vamos a crear un algoritmo que sea capaz de reconocer palíndromos como "Oso" o "Logré ver el gol".
# Esto lo vamos a realizar en cuatro sencillos pasos:
#   1) Filtramos el texto para que se conserven únicamente los caracteres alfanuméricos.
#   2) Cambiamos aquellos caracteres que tienen acento por el mismo pero sin acento.
#   3) Cambiar cada letra mayúscula por la misma letra pero en minúscula.
#   4) Verificar que el texto filtrado es igual a su imagen. 

class Palindromo():

    def __init__(self, frase) -> None:
        self.frase_inicial = frase
        self.frase_mod = frase
        self.precondicion = True
        if len(self.frase_inicial) == 0:
            self.precondicion = False        

        self.frase_mod = self.alfanumerico(self.frase_inicial)
        self.frase_mod = self.mayusculas(self.frase_mod)

    def alfabetico(self, c):
        return str(c).isalpha
    
    def cifra(self, c):
        return str(c).isdigit

    def alfanumerico(self, ca):
        resultado = ""

        if len (ca) == 0: 
            return resultado 

        if self.alfabetico(ca[0]) == True or self.cifra(ca[0]) == True: 
            resultado = ca[0] + self.alfanumerico(ca[1:])
        else: 
            resultado = self.alfanumerico(ca[1:])
        
        return resultado

    def mayusculas(self, ca):
        return str(ca).lower

    def acento(self, ca):
