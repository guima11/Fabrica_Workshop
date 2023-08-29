##------------------------------------------------------------------------------------------------
# Autor: Lucas Guimarães 

# Crie um programa que leia o nome de três pessoas: João Maia, João Abrantes e Pedro. Para os respectivos nomes imprima:'oi eu sou joao maia', 'oi eu sou joao abrantes', 'oi eu sou pedro', e caso o nome nao seja nenhum dos tres imprima 'oi meu nome é {nome}'.

##------------------------------------------------------------------------------------------------

# Entrada de Dados

Nome1 = "João Maia"

Nome2 = "João Abrantes"

Nome3 =  "Pedro"

Nome = input("Insira seu nome: ")

# Obtenção do Nome e Saída:

if Nome == Nome1:
    Nome = Nome1
    print("Oi, eu sou {}.".format(Nome))
elif Nome == Nome2:
    Nome = Nome2
    print("Oi, eu sou {}.".format(Nome))
elif Nome == Nome3:
    Nome = Nome3
    print("Oi, eu sou {}.".format(Nome))
else:
    print("Oi, eu sou {}.".format(Nome))