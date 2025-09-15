caixa = []
opcao = 0
while opcao != 3:
    opcao = int(input("Digite oq deseja fazer: \n 1- ver itens na caixa \n 2- ver albuns \n 3- ver dvd's "))
    if opcao == 1:
        print(f"itens na caixa: \n {caixa}")
    elif opcao == 2:
        item = input("adicione o nome do item: \n")
        caixa.append(item)
