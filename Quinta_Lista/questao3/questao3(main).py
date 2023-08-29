##------------------------------------------------------------------------------------------------
# Autor: Lucas Guimarães 

# Crie um programa que receba uma quantidade de canetas pretas e azuis. A caneta azul vale R$2.00, a caneta preta vale R$2.50. Mostre a quantidade final a ser paga.

##------------------------------------------------------------------------------------------------

# Entrada de Dados

from caneta import caneta

Azul = int(input("Insira o número de canetas azuis a serem compradas: "))

Preto = int(input("Insira o número de canetas pretas a serem compradas: "))

PriceAz = 2 # Valor das Canetas azuis

PricePre = 2.5 # Valor das Canetas pretas

# Cálculo dos Preços

Valor = caneta(Azul, Preto, PriceAz, PricePre)

# Saída de Dados

print("O Valor gasto em canetas foi de R$ {}.".format(Valor))