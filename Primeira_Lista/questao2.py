##------------------------------------------------------------------------------------------------
# Autor: Lucas Guimarães 

# Crie um programa que leia dois números e exiba a soma dos dois números, a subtração, multiplicação e divisão

##------------------------------------------------------------------------------------------------

# Entrada de Dados

Num1 = float(input("Insira o primeiro número para os cálculos: "))

Num2 = float(input("Insira o segundo número para os cálculos: "))

# Cálculo de dados

Soma = Num1 + Num2 # Soma entre os dados

Sub = Num1 - Num2 # Subtração entre os dados

Mult = Num1 * Num2 # Multiplicação entre os dados

Div = Num1 / Num2 # Divisão entre os dados

# Saída dos dados

print("O resultado da soma é: {}." .format(Soma))
print("O resultado da divisão é: {}." .format(Sub))
print("O resultado da multiplicação é: {}." .format(Mult))
print("O resultado da divisão é: {}." .format(Div))