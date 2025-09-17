import csv

with open("dados.csv","a", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Ford","Bronco","2002","2,00"])
