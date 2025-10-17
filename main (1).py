# Leitura dos três números
prod1 = float(input("Digite o valor do primeiro produto: "))
prod2 = float(input("Digite o valor do segundo produto: "))
prod3 = float(input("Digite o valor do terceiro produto: "))

# Comparação para encontrar o maior número
if prod1 >= prod2 and prod1 >= prod3:
    maior = prod1
elif prod2 >= prod1 and prod2 >= prod3:
    maior = prod2
else:
    maior = prod3
#Descobrindo o menor número
if prod1 <= prod2 and prod1 <= prod3:
    menor = prod1
elif prod2 <= prod1 and prod2 <= prod3:
    menor = prod2
else:
    menor = prod3
# Exibição do maior número
print("O maior valor é:", maior)
print("O menor valor é:", menor, "Opte por este")