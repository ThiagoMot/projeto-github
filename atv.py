usuarios = {}  # {id_usuario: nome}
livros = {}    # {id_livro: {'titulo': titulo, 'disponivel': True/False}}

while True:
    print("\n=== SISTEMA DE BIBLIOTECA ===")
    print("1. Cadastrar Usuário")
    print("2. Cadastrar Livro")
    print("3. Emprestar Livro")
    print("4. Devolver Livro")
    print("5. Listar Livros")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            # Funcionalidade 1: Cadastro de usuários
            id_u = input("ID do Usuário: ")
            nome = input("Nome do Usuário: ")
            if id_u in usuarios:
                print(f"Erro: Usuário com ID {id_u} já existe.")
            else:
                usuarios[id_u] = nome
                print(f"Usuário '{nome}' (ID: {id_u}) cadastrado com sucesso!")
                
        case "2":
            # Funcionalidade 2: Cadastro de livros
            id_l = input("ID do Livro: ")
            titulo = input("Título do Livro: ")
            if id_l in livros:
                print(f"Erro: Livro com ID {id_l} já existe.")
            else:
                livros[id_l] = {'titulo': titulo, 'disponivel': True}
                print(f"Livro '{titulo}' (ID: {id_l}) cadastrado com sucesso!")

        case "3":
            # Funcionalidade 3: Empréstimo de livros
            id_l = input("ID do Livro: ")
            id_u = input("ID do Usuário: ")
            if id_u not in usuarios:
                print("Erro: Usuário não cadastrado.")
            elif id_l not in livros:
                print("Erro: Livro não cadastrado.")
            elif not livros[id_l]['disponivel']:
                print(f"Erro: O livro '{livros[id_l]['titulo']}' já está emprestado.")
            else:
                livros[id_l]['disponivel'] = False
                print(f"Livro '{livros[id_l]['titulo']}' emprestado para '{usuarios[id_u]}'.")

        case "4":
            # Funcionalidade 4: Devolução de livros
            id_l = input("ID do Livro: ")
            if id_l not in livros:
                print("Erro: Livro não cadastrado.")
            elif livros[id_l]['disponivel']:
                print(f"Aviso: O livro '{livros[id_l]['titulo']}' já está disponível na biblioteca.")
            else:
                livros[id_l]['disponivel'] = True
                print(f"Livro '{livros[id_l]['titulo']}' devolvido com sucesso!")

        case "5":
            # Listagem de livros
            print("\n--- Catálogo de Livros ---")
            if not livros:
                print("Nenhum livro cadastrado.")
            else:
                for id_l, info in livros.items():
                    status = "Disponível" if info['disponivel'] else "Emprestado"
                    print(f"ID: {id_l} | Título: {info['titulo']} | Status: {status}")

        case "0":
            print("Saindo do sistema...")
            break

        case _:
            print("Opção inválida. Tente novamente.")