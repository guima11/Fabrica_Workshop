##------------------------------------------------------------------------------------------------
# Autor: Lucas Guimarães 

# 4 Herança de Formas Geométricas 
# Crie uma classe base chamada FormaGeometrica com um método para calcular a área. 
# Em seguida, crie subclasses como Retangulo e Circulo que herdam de FormaGeometrica e implementam seus próprios métodos para calcular a área.

##------------------------------------------------------------------------------------------------

class FormaGeometrica():

    def calcular_area(self, raio):
        import numpy as np
        return np.pi*raio**2
    
class Circulo(FormaGeometrica):
    pass

class Retangulo(FormaGeometrica):    
    def calcular_area(self, base, altura):

        return base*altura
    

    
retangulo = Retangulo()
area1 = retangulo.calcular_area(5,10)
print(f'A área do retangulo é {area1}.')

circulo = Circulo()
area = circulo.calcular_area(5)
print(f'A área do círculo é {area}.')
