##------------------------------------------------------------------------------------------------
# Autor: Lucas Guimarães 

# Crie um programa que leia uma velocidade de um carro e multe se passar com velocidade maior que 80km/h. mostre que ele foi multado. 
# A multa é de 7R$ por cada km acima do limite

##------------------------------------------------------------------------------------------------

# Entrada de Dados

Vel = float(input("Insira a velocidade do carro em km/h: "))

# Avaliação de multa

if Vel > 80:
    Multa = 7*(Vel - 80)
    print("A multa é de R${} por ter passado do limite de velocidade." .format(Multa))
else:
    print("Não constam multas por excesso de velocidade.")

