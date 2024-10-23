<<<<<<< HEAD
from estoque import adicionar_produto, remover_produto, editar_produto, listar_produtos, pesquisar_produto, exportar_para_csv

def menu():
    while True:
        print("=== Gerenciador de Estoque ===")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Editar Produto")
        print("4. Listar Produtos")
        print("5. Pesquisar Produto")
        print("6. Exportar Relatório")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do Produto: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            adicionar_produto(nome, preco, quantidade)
            print("Produto adicionado com sucesso!")
        elif opcao == '2':
            produto_id = int(input("ID do Produto a remover: "))
            remover_produto(produto_id)
            print("Produto removido com sucesso!")
        elif opcao == '3':
            produto_id = int(input("ID do Produto a editar: "))
            nome = input("Novo Nome (pressione Enter para não alterar): ")
            preco = input("Novo Preço (pressione Enter para não alterar): ")
            quantidade = input("Nova Quantidade (pressione Enter para não alterar): ")
            editar_produto(produto_id, 
                           nome if nome else None, 
                           float(preco) if preco else None, 
                           int(quantidade) if quantidade else None)
            print("Produto editado com sucesso!")
        elif opcao == '4':
            listar_produtos()
        elif opcao == '5':
            criterio = input("Pesquisar por ID ou Nome? (id/nome): ").lower()
            valor = input("Digite o valor de pesquisa: ")
            pesquisar_produto(criterio, valor)
        elif opcao == '6':
            exportar_para_csv()
        elif opcao == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
=======
from estoque import adicionar_produto, remover_produto, editar_produto, listar_produtos, pesquisar_produto, exportar_para_csv

def menu():
    while True:
        print("=== Gerenciador de Estoque ===")
        print("1. Adicionar Produto")
        print("2. Remover Produto")
        print("3. Editar Produto")
        print("4. Listar Produtos")
        print("5. Pesquisar Produto")
        print("6. Exportar Relatório")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do Produto: ")
            preco = float(input("Preço: "))
            quantidade = int(input("Quantidade: "))
            adicionar_produto(nome, preco, quantidade)
            print("Produto adicionado com sucesso!")
        elif opcao == '2':
            produto_id = int(input("ID do Produto a remover: "))
            remover_produto(produto_id)
            print("Produto removido com sucesso!")
        elif opcao == '3':
            produto_id = int(input("ID do Produto a editar: "))
            nome = input("Novo Nome (pressione Enter para não alterar): ")
            preco = input("Novo Preço (pressione Enter para não alterar): ")
            quantidade = input("Nova Quantidade (pressione Enter para não alterar): ")
            editar_produto(produto_id, 
                           nome if nome else None, 
                           float(preco) if preco else None, 
                           int(quantidade) if quantidade else None)
            print("Produto editado com sucesso!")
        elif opcao == '4':
            listar_produtos()
        elif opcao == '5':
            criterio = input("Pesquisar por ID ou Nome? (id/nome): ").lower()
            valor = input("Digite o valor de pesquisa: ")
            pesquisar_produto(criterio, valor)
        elif opcao == '6':
            exportar_para_csv()
        elif opcao == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
>>>>>>> 0b853dd20a0d238227f6ecb2188868975cd6ccae
