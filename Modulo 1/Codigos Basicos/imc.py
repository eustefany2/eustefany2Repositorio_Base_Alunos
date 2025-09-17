nome = str(input("qual o seu nome?"))
peso = float(input("qual o seu peso?"))
altura = float(input("qual a sua altura"))

imc = peso / (altura*altura)

if imc <= 18.5:
    print(f"{nome}esta abaixo do peso {imc} ")
elif imc <= 24.9:
    print(f"{nome}esta com peso normal {imc}")
elif imc <= 34.9: 
    print(f"{nome}esta com obesidade grau 1 {imc}")
elif imc <= 39.9:
    print(f"{nome} esta com obesidade grau 2 {imc}")
else:
    print(f"{nome}esta com obesidade grau 3 (mórbida) {imc}")
