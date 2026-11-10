# Sistema de Biblioteca - atv.py
import monitoramento

usuarios = {}  # {id_usuario: nome}
livros = {}    # {id_livro: {'titulo': titulo, 'disponivel': True/False}}


@monitoramento.monitorar("cadastrar_usuario")
def cadastrar_usuario(id_u, nome):
    if id_u in usuarios:
        return False, f"Erro: Utilizador com ID {id_u} já existe."
    usuarios[id_u] = nome
    return True, f"Utilizador '{nome}' (ID: {id_u}) cadastrado com sucesso!"


@monitoramento.monitorar("cadastrar_livro")
def cadastrar_livro(id_l, titulo):
    if id_l in livros:
        return False, f"Erro: Livro com ID {id_l} já existe."
    livros[id_l] = {'titulo': titulo, 'disponivel': True}
    return True, f"Livro '{titulo}' (ID: {id_l}) cadastrado com sucesso!"


@monitoramento.monitorar("emprestar_livro")
def emprestar_livro(id_l, id_u):
    if id_u not in usuarios:
        return False, "Erro: Utilizador não cadastrado."
    if id_l not in livros:
        return False, "Erro: Livro não cadastrado."
    if not livros[id_l]['disponivel']:
        return False, f"Erro: O livro '{livros[id_l]['titulo']}' já está emprestado."

    livros[id_l]['disponivel'] = False
    return True, f"Livro '{livros[id_l]['titulo']}' emprestado para '{usuarios[id_u]}'."


@monitoramento.monitorar("devolver_livro")
def devolver_livro(id_l):
    if id_l not in livros:
        return False, "Erro: Livro não cadastrado."
    if livros[id_l]['disponivel']:
        return False, f"Aviso: O livro '{livros[id_l]['titulo']}' já está disponível na biblioteca."

    livros[id_l]['disponivel'] = True
    return True, f"Livro '{livros[id_l]['titulo']}' devolvido com sucesso!"


def menu():
    while True:
        print("\n=== SISTEMA DE BIBLIOTECA ===")
        print("1. Cadastrar Utilizador")
        print("2. Cadastrar Livro")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Listar Livros")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                id_u = input("ID do Utilizador: ")
                nome = input("Nome do Utilizador: ")
                _, msg = cadastrar_usuario(id_u, nome)
                print(msg)

            case "2":
                id_l = input("ID do Livro: ")
                titulo = input("Título do Livro: ")
                _, msg = cadastrar_livro(id_l, titulo)
                print(msg)

            case "3":
                id_l = input("ID do Livro: ")
                id_u = input("ID do Utilizador: ")
                _, msg = emprestar_livro(id_l, id_u)
                print(msg)

            case "4":
                id_l = input("ID do Livro: ")
                _, msg = devolver_livro(id_l)
                print(msg)

            case "5":
                print("\n--- Catálogo de Livros ---")
                if not livros:
                    print("Nenhum livro cadastrado.")
                else:
                    for id_l, info in livros.items():
                        status = "Disponível" if info['disponivel'] else "Emprestado"
                        print(f"ID: {id_l} | Título: {info['titulo']} | Status: {status}")

            case "0":
                print("A sair do sistema...")
                break

            case _:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    monitoramento.iniciar_monitoramento()
    menu()