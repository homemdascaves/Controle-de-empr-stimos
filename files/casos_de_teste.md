# Casos de teste

Os testes automatizados ficam em `test_biblioteca.py`. Para executar:

```bash
python -m unittest test_biblioteca -v
```

| # | Operação | Entrada | Resultado esperado | Tipo | Teste |
|---|---|---|---|---|---|
| 1 | Cadastrar pessoa | "Maria", "003" | "Pessoa cadastrada com sucesso!" | Válido | `test_01` |
| 2 | Cadastrar pessoa | "Outra", "001" (já existe) | "Matrícula já cadastrada!" | Inválido | `test_02` |
| 3 | Cadastrar livro | "1984", "L03" | "Livro cadastrado com sucesso!" | Válido | `test_03` |
| 4 | Cadastrar livro | código "L01" repetido | "Código já cadastrado!" | Inválido | `test_04` |
| 5 | Emprestar | matrícula "001", livro "L01" | Empréstimo registrado; livro indisponível | Válido | `test_05` |
| 6 | Emprestar | matrícula "002", livro "L01" (já emprestado) | "Livro já está emprestado!" | Inválido (duplicado) | `test_06` |
| 7 | Emprestar | matrícula "999", livro "L02" | "Pessoa não encontrada!" | Inválido | `test_07` |
| 8 | Emprestar | matrícula "001", livro "L99" | "Livro não encontrado!" | Inválido | `test_08` |
| 9 | Devolver | livro "L01" emprestado | Devolução registrada; livro disponível | Válido | `test_09` |
| 10 | Devolver | livro "L01" de novo | "Este livro não está emprestado!" | Inválido | `test_10` |
| 11 | Devolver | livro "L99" | "Livro não encontrado!" | Inválido | `test_11` |
| 12 | Cadastrar pessoa | nome vazio | "Nome e matrícula são obrigatórios!" | Inválido | `test_12` |
| 13 | Cadastrar livro | título vazio | "Título, autor e código são obrigatórios!" | Inválido | `test_13` |
| 14 | Emprestar, devolver e emprestar a outra pessoa | L01: Ana, depois João | 2 registros no histórico, nenhum perdido | Válido (rastreabilidade) | `test_14` |
