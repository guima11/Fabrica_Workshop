##------------------------------------------------------------------------------------------------
# Autor: Lucas Guimarães 

# Crie um programa que peça um numero e mostre o seu sucessor e antecessor

##------------------------------------------------------------------------------------------------

# Entrada de Dados

Num = int(input('Insira um número Inteiro qualquer: '))

# Cálculo do Antecessor e Sucessor

NumS = Num + 1

NumA = Num - 1

# Saída de Dados

print("O Sucessor de {} é {} e o seu Antecessor é {}." .format(Num, NumS, NumA))