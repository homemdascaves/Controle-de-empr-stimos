from cadastro_biblioteca import CadastroBiblioteca


def carregar_dados_iniciais(biblioteca):
    biblioteca.cadastrar_pessoa("Ana", "001")
    biblioteca.cadastrar_pessoa("João", "002")
    biblioteca.cadastrar_livro("Dom Casmurro", "Machado de Assis", "L01")
    biblioteca.cadastrar_livro(
        "O Pequeno Príncipe", "Antoine de Saint-Exupéry", "L02"
    )
    biblioteca.cadastrar_livro("A Revolução dos Bichos", "George Orwell", "L03")


def menu():
    print("\n=== Sistema de Controle de Empréstimos ===")
    print("1. Cadastrar pessoa")
    print("2. Cadastrar livro")
    print("3. Listar livros")
    print("4. Listar pessoas")
    print("5. Registrar empréstimo")
    print("6. Registrar devolução")
    print("7. Histórico de empréstimos")
    print("0. Sair")
    return input("Escolha uma opção: ").strip()


def main():
    biblioteca = CadastroBiblioteca()
    print("Carregando dados iniciais...")
    carregar_dados_iniciais(biblioteca)

    while True:
        opcao = menu()

        if opcao == "1":
            nome = input("Nome: ")
            matricula = input("Matrícula: ")
            biblioteca.cadastrar_pessoa(nome, matricula)
        elif opcao == "2":
            titulo = input("Título: ")
            autor = input("Autor: ")
            codigo = input("Código: ")
            biblioteca.cadastrar_livro(titulo, autor, codigo)
        elif opcao == "3":
            biblioteca.listar_livros()
        elif opcao == "4":
            biblioteca.listar_pessoas()
        elif opcao == "5":
            matricula = input("Matrícula da pessoa: ")
            codigo = input("Código do livro: ")
            biblioteca.emprestar(matricula, codigo)
        elif opcao == "6":
            codigo = input("Código do livro a devolver: ")
            biblioteca.devolver(codigo)
        elif opcao == "7":
            biblioteca.listar_emprestimos()
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
