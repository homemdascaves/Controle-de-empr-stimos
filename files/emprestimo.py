from datetime import datetime


class Emprestimo:
    """Vínculo formal entre uma Pessoa e um Livro, com histórico de datas."""

    def __init__(self, pessoa, livro):
        self.pessoa = pessoa
        self.livro = livro
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None

    @property
    def ativo(self):
        return self.data_devolucao is None

    def __str__(self):
        inicio = self.data_emprestimo.strftime("%d/%m/%Y %H:%M")
        if self.ativo:
            situacao = "em aberto"
        else:
            situacao = "devolvido em " + self.data_devolucao.strftime("%d/%m/%Y %H:%M")
        return f"{self.livro.titulo} | {self.pessoa.nome} | {inicio} | {situacao}"
