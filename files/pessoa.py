class Pessoa:
    """Representa quem pega itens emprestados."""

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} (matrícula {self.matricula})"
