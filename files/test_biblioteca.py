import io
import unittest
from contextlib import redirect_stdout

from cadastro_biblioteca import CadastroBiblioteca


def executar(func, *args):
    """Executa func capturando o que ela imprime. Retorna (resultado, saida)."""
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        resultado = func(*args)
    return resultado, buffer.getvalue().strip()


class TestBiblioteca(unittest.TestCase):
    def setUp(self):
        self.b = CadastroBiblioteca()
        executar(self.b.cadastrar_pessoa, "Ana", "001")
        executar(self.b.cadastrar_pessoa, "João", "002")
        executar(self.b.cadastrar_livro, "Dom Casmurro", "Machado de Assis", "L01")
        executar(self.b.cadastrar_livro, "O Pequeno Príncipe", "Saint-Exupéry", "L02")

    # --- Cadastro de pessoa ---
    def test_01_cadastrar_pessoa_valida(self):
        ok, msg = executar(self.b.cadastrar_pessoa, "Maria", "003")
        self.assertTrue(ok)
        self.assertEqual(msg, "Pessoa cadastrada com sucesso!")

    def test_02_cadastrar_pessoa_matricula_duplicada(self):
        ok, msg = executar(self.b.cadastrar_pessoa, "Outra", "001")
        self.assertFalse(ok)
        self.assertEqual(msg, "Matrícula já cadastrada!")
        self.assertEqual(len(self.b.pessoas), 2)

    # --- Cadastro de livro ---
    def test_03_cadastrar_livro_valido(self):
        ok, msg = executar(self.b.cadastrar_livro, "1984", "George Orwell", "L03")
        self.assertTrue(ok)
        self.assertEqual(msg, "Livro cadastrado com sucesso!")

    def test_04_cadastrar_livro_codigo_duplicado(self):
        ok, msg = executar(self.b.cadastrar_livro, "Outro", "Autor", "L01")
        self.assertFalse(ok)
        self.assertEqual(msg, "Código já cadastrado!")
        self.assertEqual(len(self.b.livros), 2)

    # --- Empréstimo ---
    def test_05_emprestimo_valido(self):
        ok, msg = executar(self.b.emprestar, "001", "L01")
        self.assertTrue(ok)
        self.assertIn("registrado", msg)
        self.assertFalse(self.b.buscar_livro("L01").disponivel)
        self.assertEqual(len(self.b.emprestimos), 1)

    def test_06_emprestimo_duplicado(self):
        executar(self.b.emprestar, "001", "L01")
        ok, msg = executar(self.b.emprestar, "002", "L01")
        self.assertFalse(ok)
        self.assertEqual(msg, "Livro já está emprestado!")
        self.assertEqual(len(self.b.emprestimos), 1)

    def test_07_emprestimo_pessoa_inexistente(self):
        ok, msg = executar(self.b.emprestar, "999", "L02")
        self.assertFalse(ok)
        self.assertEqual(msg, "Pessoa não encontrada!")

    def test_08_emprestimo_livro_inexistente(self):
        ok, msg = executar(self.b.emprestar, "001", "L99")
        self.assertFalse(ok)
        self.assertEqual(msg, "Livro não encontrado!")

    # --- Devolução ---
    def test_09_devolucao_valida(self):
        executar(self.b.emprestar, "001", "L01")
        ok, msg = executar(self.b.devolver, "L01")
        self.assertTrue(ok)
        self.assertIn("registrada", msg)
        self.assertTrue(self.b.buscar_livro("L01").disponivel)
        self.assertIsNotNone(self.b.emprestimos[0].data_devolucao)

    def test_10_devolucao_de_livro_nao_emprestado(self):
        executar(self.b.emprestar, "001", "L01")
        executar(self.b.devolver, "L01")
        ok, msg = executar(self.b.devolver, "L01")
        self.assertFalse(ok)
        self.assertEqual(msg, "Este livro não está emprestado!")

    def test_11_devolucao_livro_inexistente(self):
        ok, msg = executar(self.b.devolver, "L99")
        self.assertFalse(ok)
        self.assertEqual(msg, "Livro não encontrado!")

    # --- Campos obrigatórios ---
    def test_12_cadastrar_pessoa_nome_vazio(self):
        ok, msg = executar(self.b.cadastrar_pessoa, "   ", "004")
        self.assertFalse(ok)
        self.assertEqual(msg, "Nome e matrícula são obrigatórios!")

    def test_13_cadastrar_livro_titulo_vazio(self):
        ok, msg = executar(self.b.cadastrar_livro, "", "Autor", "L10")
        self.assertFalse(ok)
        self.assertEqual(msg, "Título, autor e código são obrigatórios!")

    # --- Rastreabilidade ---
    def test_14_historico_preservado_apos_devolucao(self):
        executar(self.b.emprestar, "001", "L01")
        executar(self.b.devolver, "L01")
        executar(self.b.emprestar, "002", "L01")
        self.assertEqual(len(self.b.emprestimos), 2)
        self.assertEqual(self.b.emprestimos[0].pessoa.nome, "Ana")
        self.assertEqual(self.b.emprestimos[1].pessoa.nome, "João")


if __name__ == "__main__":
    unittest.main(verbosity=2)
