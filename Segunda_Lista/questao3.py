##------------------------------------------------------------------------------------------------
# Autor: Lucas Guimarães 

# Crie um programa que leia tres números e mostre qual deles e o maior e o menor

##------------------------------------------------------------------------------------------------

# Entrada de Dados

Num1 = float(input("Insira o primeiro número: "))

Num2 = float(input("Insira o segundo número: "))

Num3 = float(input("Insira o terceiro número: "))

# Descobrindo o maior número entre eles:

maior = Num1

if Num2 > Num1 and Num2 > Num3:

    maior = Num2

if Num3 > Num1 and Num3 > Num2:

    maior = Num3

menor = Num1

if Num2 < Num3 and Num2 < Num1:

    menor = Num2

if Num3 < Num2 and Num3 < Num1:

    menor = Num3

# Saída de Dados

print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")