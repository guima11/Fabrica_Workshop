##------------------------------------------------------------------------------------------------
# Autor: Lucas Guimarães 

# Crie um programa que leia tres números e mostre qual deles e o maior e o menor

##------------------------------------------------------------------------------------------------

# Entrada de Dados

from selecao import selecao

Num1 = float(input("Insira o primeiro número: "))

Num2 = float(input("Insira o segundo número: "))

Num3 = float(input("Insira o terceiro número: "))

# Descobrindo o maior número entre eles:

maior, menor = selecao(Num1, Num2, Num3)

# Saída de Dados

print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")