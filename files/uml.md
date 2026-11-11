# Diagrama UML

Diagrama de classes do sistema (Mermaid). O GitHub renderiza este bloco automaticamente.
Para exportar como imagem, cole o código em https://mermaid.live e baixe o PNG
(salve como `docs/uml.png`).

```mermaid
classDiagram
    class Pessoa {
        +str nome
        +str matricula
    }
    class Livro {
        +str titulo
        +str autor
        +str codigo
        +bool disponivel
    }
    class Emprestimo {
        +Pessoa pessoa
        +Livro livro
        +datetime data_emprestimo
        +datetime data_devolucao
        +ativo() bool
    }
    class CadastroBiblioteca {
        +list pessoas
        +list livros
        +list emprestimos
        +cadastrar_pessoa(nome, matricula) bool
        +cadastrar_livro(titulo, autor, codigo) bool
        +buscar_pessoa(matricula) Pessoa
        +buscar_livro(codigo) Livro
        +emprestar(matricula, codigo) bool
        +devolver(codigo) bool
        +listar_livros()
        +listar_pessoas()
        +listar_emprestimos()
    }
    CadastroBiblioteca "1" o-- "*" Pessoa
    CadastroBiblioteca "1" o-- "*" Livro
    CadastroBiblioteca "1" *-- "*" Emprestimo
    Emprestimo "*" --> "1" Pessoa
    Emprestimo "*" --> "1" Livro
```

## Relacionamentos
- **Agregação (◇):** `CadastroBiblioteca` agrupa `Pessoa` e `Livro`, que existem como entidades próprias.
- **Composição (◆):** `CadastroBiblioteca` é dona dos `Emprestimo`, que só existem dentro do cadastro.
- **Associação (→):** cada `Emprestimo` liga exatamente uma `Pessoa` a um `Livro`.
