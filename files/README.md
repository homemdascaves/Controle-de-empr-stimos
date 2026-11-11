# Sistema de Controle de Empréstimos de Equipamentos

Projeto em Python com **Programação Orientada a Objetos (POO)** que registra
empréstimos e devoluções, impedindo operações inválidas.

## O problema
O controle manual de empréstimos (papel ou planilha) costuma gerar:

- **Inconsistência nos registros:** vulnerável a falhas humanas e perda de histórico.
- **Falta de rastreabilidade:** é difícil identificar quem é responsável por cada item.
- **Empréstimos duplicados:** não há como verificar instantaneamente a disponibilidade real dos itens.

## A solução em objetos
As regras ficam no próprio código, e cada empréstimo é um objeto que liga formalmente uma pessoa a um item.

| Classe | Arquivo | Responsabilidade |
|---|---|---|
| `Pessoa` | `pessoa.py` | Quem pega emprestado (nome, matrícula) |
| `Livro` | `livro.py` | Item emprestável (título, autor, código, disponibilidade) |
| `Emprestimo` | `emprestimo.py` | Liga uma `Pessoa` a um `Livro`, com datas de empréstimo e devolução |
| `CadastroBiblioteca` | `cadastro_biblioteca.py` | Gerencia cadastros e aplica as validações |

### Validações implementadas
- Matrícula e código de livro **únicos**.
- Campos obrigatórios não podem ser vazios.
- Empréstimo **bloqueado** se o livro já estiver emprestado, ou se a pessoa ou o livro não existirem.
- Devolução **bloqueada** se o livro não estiver emprestado ou não existir.
- O histórico de empréstimos é preservado após as devoluções (rastreabilidade).

## Como executar
Requer Python 3.8 ou superior. Não há dependências externas.

```bash
git clone <url-do-repositorio>
cd <pasta-do-projeto>
python main.py
```

### Rodar os testes
```bash
python -m unittest test_biblioteca -v
```

## Estrutura do projeto
```
.
├── main.py                  # menu interativo
├── pessoa.py
├── livro.py
├── emprestimo.py
├── cadastro_biblioteca.py   # regras de negócio e validações
├── test_biblioteca.py       # testes automatizados
├── docs/
│   ├── uml.md               # diagrama UML (Mermaid)
│   └── casos_de_teste.md    # testes válidos e inválidos
└── README.md
```

## Documentação
- Diagrama UML: [`docs/uml.md`](docs/uml.md)
- Casos de teste: [`docs/casos_de_teste.md`](docs/casos_de_teste.md)

## Autores
<nomes do grupo>
