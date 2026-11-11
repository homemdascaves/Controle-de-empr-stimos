from datetime import datetime

from emprestimo import Emprestimo
from livro import Livro
from pessoa import Pessoa


class CadastroBiblioteca:
    """Gerencia cadastros e aplica as regras de validação dos empréstimos.

    Todos os métodos de operação imprimem uma mensagem e retornam
    True (sucesso) ou False (operação inválida bloqueada).
    """

    def __init__(self):
        self.pessoas = []
        self.livros = []
        self.emprestimos = []

    # ---------- Cadastros ----------
    def cadastrar_pessoa(self, nome, matricula):
        if not nome.strip() or not matricula.strip():
            print("Nome e matrícula são obrigatórios!")
            return False
        if self.buscar_pessoa(matricula):
            print("Matrícula já cadastrada!")
            return False
        self.pessoas.append(Pessoa(nome, matricula))
        print("Pessoa cadastrada com sucesso!")
        return True

    def cadastrar_livro(self, titulo, autor, codigo):
        if not titulo.strip() or not autor.strip() or not codigo.strip():
            print("Título, autor e código são obrigatórios!")
            return False
        if self.buscar_livro(codigo):
            print("Código já cadastrado!")
            return False
        self.livros.append(Livro(titulo, autor, codigo))
        print("Livro cadastrado com sucesso!")
        return True

    # ---------- Buscas ----------
    def buscar_pessoa(self, matricula):
        return next((p for p in self.pessoas if p.matricula == matricula), None)

    def buscar_livro(self, codigo):
        return next((l for l in self.livros if l.codigo == codigo), None)

    # ---------- Empréstimo e devolução ----------
    def emprestar(self, matricula, codigo):
        pessoa = self.buscar_pessoa(matricula)
        livro = self.buscar_livro(codigo)

        if pessoa is None:
            print("Pessoa não encontrada!")
            return False
        if livro is None:
            print("Livro não encontrado!")
            return False
        if not livro.disponivel:
            print("Livro já está emprestado!")
            return False

        livro.disponivel = False
        self.emprestimos.append(Emprestimo(pessoa, livro))
        print(f"Empréstimo de '{livro.titulo}' para {pessoa.nome} registrado!")
        return True

    def devolver(self, codigo):
        livro = self.buscar_livro(codigo)

        if livro is None:
            print("Livro não encontrado!")
            return False
        if livro.disponivel:
            print("Este livro não está emprestado!")
            return False

        for emp in self.emprestimos:
            if emp.livro is livro and emp.ativo:
                emp.data_devolucao = datetime.now()
        livro.disponivel = True
        print(f"Devolução de '{livro.titulo}' registrada!")
        return True

    # ---------- Listagens ----------
    def listar_livros(self):
        print("\n--- Livros ---")
        if not self.livros:
            print("Nenhum livro cadastrado.")
        for livro in self.livros:
            print(livro)

    def listar_pessoas(self):
        print("\n--- Pessoas ---")
        if not self.pessoas:
            print("Nenhuma pessoa cadastrada.")
        for pessoa in self.pessoas:
            print(pessoa)

    def listar_emprestimos(self):
        print("\n--- Histórico de empréstimos ---")
        if not self.emprestimos:
            print("Nenhum empréstimo registrado.")
        for emp in self.emprestimos:
            print(emp)
