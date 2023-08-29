##------------------------------------------------------------------------------------------------
# Autor: Lucas Guimarães 

# Utilizando estrutura de repeticao while crie um programa que peça vários nomes e só pare quando for digitado "parar"

##------------------------------------------------------------------------------------------------

# Entrada de Dados
i = True

# Estrutura de Loop para nomes

while i == True:
    Nome = input("Digite o nome (caso queira parar, escreva 'parar'): ")
    if Nome == "parar":
        i = False

    
