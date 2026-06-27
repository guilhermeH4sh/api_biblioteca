from typing import Annotated
livros = []

while True: 

    try:
        opcao = int(input("""
---------------------------------
1. Cadastro de livros
2. Listar livros
3. Buscar livro por ID
4. Remover livro
5. Sair
---------------------------------
Escolha uma opção: """))

    except ValueError:
        print("Digite apenas números! ")
        continue


    match opcao:
        case 1:
            print("Você escolheu Cadastro de livros ")
            
            try:
                titulo = input("Título: ")
                autor = input("Autor: " )
                ano = int(input("Ano: "))
            except ValueError:
                print("Digitos inválidos! ")
                continue

            livro = {
                "id": len(livros) + 1,
                "titulo": titulo,
                "autor": autor,
                "ano": ano,
                "disponivel": True
            }

            livros.append(livro)

            print("Livro cadastrado! ")
            print(livros)
        case 2:
            print("Você escolheu Listar livros \n")

            if len(livros) == 0:
                print("A lista está vazia! ")
            else: 
                for livro in livros:
                    print(f"""
---------------------------------
ID: {livro["id"]}
Título: {livro["titulo"]}
Autor: {livro["autor"]}
Ano: {livro["ano"]}
Disponível: {livro["disponivel"]}
---------------------------------
""")
        case 3:
            encontrado = False

            print("Você escolheu Buscar livro por ID ")
            opcao_id = int(input("Digite o ID do livro: "))

            for livro in livros:
                if livro["id"] == opcao_id:
                    print(f"""
ID: {livro['id']}
Título: {livro['titulo']}
Autor: {livro['autor']}
Ano: {livro['ano']}
Disponível: {livro['disponivel']}
""")

                    encontrado = True

                    break

                if not encontrado:
                    print("Livro não existe no banco de dados! ")
        case 4:
            print("Você escolheu Remover livro ")

            if len(livros) == 0:
                    print("Não existem livros na sua estante... ")
            else:
                try:
                    id_remover = int(input("Digite o ID do livro que será removido: "))
                except ValueError:
                    print("Digite apenas números! ")

                encontrado = False

                for livro in livros:
                    if livro["id"] == id_remover:
                        livros.remove(livro)
                        print(f"""
---------------------------------
ID: {livro["id"]}
Título: {livro["titulo"]}
Autor: {livro["autor"]}
Ano: {livro["ano"]}
Disponível: {livro["disponivel"]}
---------------------------------
""")
                        print("Livro removido com sucesso! ")

                        encontrado = True
                    else:
                        print("Digite um ID válido! ")

                    break

                    if not encontrado:
                        print("ID do livro não encontrado na base de dados! ")

        case 5: 
            break
        case _:
            print("Opção inválida!")