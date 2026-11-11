class Livro:
    """Representa o item emprestável e controla sua disponibilidade."""

    def __init__(self, titulo, autor, codigo):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"[{self.codigo}] {self.titulo} - {self.autor} -> {status}"
