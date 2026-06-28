# pyrefly: ignore [missing-import]
import services.livro_service as livro_service
# pyrefly: ignore [missing-import]
import services.usuario_service as usuario_service
# pyrefly: ignore [missing-import]
import services.emprestimo_service as emprestimo_service

def menu_livros():
    while True:
        try:
            opcao = int(input("""
=== MENU DE LIVROS ===
1. Cadastrar Livro
2. Listar Livros
3. Buscar Livro por ID
4. Remover Livro
5. Voltar ao Menu Principal
Escolha uma opção: """))
        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao == 1:
            print("\n--- Cadastro de Livro ---")
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            try:
                ano = int(input("Ano: "))
                livro = livro_service.cadastrar_livro(titulo, autor, ano)
                print(f"\nLivro cadastrado com sucesso! ID: {livro['id']}")
            except ValueError:
                print("Ano inválido!")
        elif opcao == 2:
            print("\n--- Lista de Livros ---")
            livros = livro_service.listar_livros()
            if not livros:
                print("Nenhum livro cadastrado.")
            else:
                for livro in livros:
                    status = "Disponível" if livro.get("disponivel", True) else "Emprestado"
                    print(f"ID: {livro['id']} | Título: {livro['titulo']} | Autor: {livro['autor']} | Ano: {livro['ano']} | Status: {status}")
        elif opcao == 3:
            print("\n--- Buscar Livro por ID ---")
            try:
                id_livro = int(input("Digite o ID do livro: "))
                livro = livro_service.buscar_livro_por_id(id_livro)
                if livro:
                    status = "Disponível" if livro.get("disponivel", True) else "Emprestado"
                    print(f"\nID: {livro['id']}")
                    print(f"Título: {livro['titulo']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Ano: {livro['ano']}")
                    print(f"Status: {status}")
                else:
                    print("Livro não encontrado.")
            except ValueError:
                print("ID inválido!")
        elif opcao == 4:
            print("\n--- Remover Livro ---")
            try:
                id_livro = int(input("Digite o ID do livro a ser removido: "))
                if livro_service.remover_livro(id_livro):
                    print("Livro removido com sucesso!")
                else:
                    print("Livro não encontrado.")
            except ValueError:
                print("ID inválido!")
        elif opcao == 5:
            break
        else:
            print("Opção inválida!")

def menu_usuarios():
    while True:
        try:
            opcao = int(input("""
=== MENU DE USUÁRIOS ===
1. Cadastrar Usuário
2. Listar Usuários
3. Remover Usuário
4. Voltar ao Menu Principal
Escolha uma opção: """))
        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao == 1:
            print("\n--- Cadastro de Usuário ---")
            nome = input("Nome: ").strip()
            email = input("E-mail: ").strip()
            try:
                usuario = usuario_service.cadastrar_usuario(nome, email)
                print(f"\nUsuário cadastrado com sucesso! ID: {usuario['id']}")
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == 2:
            print("\n--- Lista de Usuários ---")
            usuarios = usuario_service.listar_usuarios()
            if not usuarios:
                print("Nenhum usuário cadastrado.")
            else:
                for usuario in usuarios:
                    print(f"ID: {usuario['id']} | Nome: {usuario['nome']} | E-mail: {usuario['email']}")
        elif opcao == 3:
            print("\n--- Remover Usuário ---")
            try:
                id_usuario = int(input("Digite o ID do usuário a ser removido: "))
                if usuario_service.remover_usuario(id_usuario):
                    print("Usuário removido com sucesso!")
                else:
                    print("Usuário não encontrado.")
            except ValueError:
                print("ID inválido!")
        elif opcao == 4:
            break
        else:
            print("Opção inválida!")

def menu_emprestimos():
    while True:
        try:
            opcao = int(input("""
=== MENU DE EMPRÉSTIMOS ===
1. Pegar Livro Emprestado
2. Devolver Livro
3. Listar Empréstimos Ativos
4. Voltar ao Menu Principal
Escolha uma opção: """))
        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao == 1:
            print("\n--- Registrar Empréstimo ---")
            try:
                id_usuario = int(input("ID do Usuário: "))
                id_livro = int(input("ID do Livro: "))
                emprestimo = emprestimo_service.realizar_emprestimo(id_usuario, id_livro)
                print(f"\nEmpréstimo registrado com sucesso! ID Empréstimo: {emprestimo['id']} (Data: {emprestimo['data_emprestimo']})")
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == 2:
            print("\n--- Devolver Livro ---")
            try:
                id_emprestimo = int(input("Digite o ID do Empréstimo: "))
                if emprestimo_service.devolver_livro(id_emprestimo):
                    print("Livro devolvido com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == 3:
            print("\n--- Empréstimos Ativos ---")
            ativos = emprestimo_service.listar_emprestimos_ativos()
            if not ativos:
                print("Nenhum empréstimo ativo no momento.")
            else:
                for emp in ativos:
                    print(f"ID Empréstimo: {emp['id']} | ID Usuário: {emp['id_usuario']} | ID Livro: {emp['id_livro']} | Data Empréstimo: {emp['data_emprestimo']}")
        elif opcao == 4:
            break
        else:
            print("Opção inválida!")

def main():
    while True:
        try:
            opcao = int(input("""
===============================
=== SISTEMA DE BIBLIOTECA ===
===============================
1. Gerenciar Livros
2. Gerenciar Usuários
3. Gerenciar Empréstimos
4. Sair
===============================
Escolha uma opção: """))
        except ValueError:
            print("Digite apenas números!")
            continue

        if opcao == 1:
            menu_livros()
        elif opcao == 2:
            menu_usuarios()
        elif opcao == 3:
            menu_emprestimos()
        elif opcao == 4:
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()