##------------------------------------------------------------------------------------------------
# Autor: Lucas Guimarães 

# Crie um programa que receba uma idade e retorne se pode obter carteira de motorista(CNH)

##------------------------------------------------------------------------------------------------

# Entrada de Dados

Idade = int(input("Insira a idade do avaliado: "))

# Avaliação dos dados

if Idade >= 18:
    CNH = "Viável"
else:
    CNH = "Inviável temporariamente"

# Saída de dados

print("A CNH do indivíduo é: {}.".format(CNH))