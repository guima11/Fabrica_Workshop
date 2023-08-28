##------------------------------------------------------------------------------------------------
# Autor: Lucas Guimarães 

# Crie um programa que leia uma temperatura em Celsius e a converta para Fahrenheit

##------------------------------------------------------------------------------------------------

# Entrada de Dados

TempC = float(input("Entre com a temperatura em Celcius: "))

# Cálculo da Temperatura em Fahrenheit

TempF = TempC * (9/5) + 32

# Saída de dados

print("A temperatura {}ºC é equivalente a {}ºF.".format(TempC, TempF))