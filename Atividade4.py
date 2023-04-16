lista_de_compras = []

while True:
    print("Digite '1' para adicionar um item à lista")
    print("Digite '2' para apagar um item da lista")
    print("Digite '3' para listar todos os itens da lista")
    print("Digite '4' para sair")

    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        item = input("Digite o item que deseja adicionar: ")
        lista_de_compras.append(item)
        print("Item adicionado com sucesso!")

    elif opcao == 2:
        item = input("Digite o item que deseja apagar: ")
        if item in lista_de_compras:
            lista_de_compras.remove(item)
            print("Item removido com sucesso!")
        else:
            print("Item não encontrado na lista.")

    elif opcao == 3:
        if lista_de_compras:
            print("Lista de compras:")
            for item in lista_de_compras:
                print("-", item)
        else:
            print("A lista está vazia.")

    elif opcao == 4:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")