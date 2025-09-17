import csv

teste = open("dados.csv")
arquivo = csv.DictReader(teste)

for carro in arquivo:
    if carro["Modelo"] == "ford":
        print(carro)
