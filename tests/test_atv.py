import unittest
import atv

class TestSistemaBiblioteca(unittest.TestCase):

    def setUp(self):
        # Limpa as variáveis globais antes de cada teste
        atv.usuarios.clear()
        atv.livros.clear()

    def test_cadastrar_usuario(self):
        sucesso, _ = atv.cadastrar_usuario("1", "Thiago")
        self.assertTrue(sucesso)
        self.assertIn("1", atv.usuarios)

        # Teste de duplicidade
        sucesso_duplicado, _ = atv.cadastrar_usuario("1", "Outro Nome")
        self.assertFalse(sucesso_duplicado)

    def test_cadastrar_livro(self):
        sucesso, _ = atv.cadastrar_livro("101", "Clean Code")
        self.assertTrue(sucesso)
        self.assertIn("101", atv.livros)

        # Teste de duplicidade
        sucesso_duplicado, _ = atv.cadastrar_livro("101", "Outro Livro")
        self.assertFalse(sucesso_duplicado)

    def test_emprestar_livro(self):
        atv.cadastrar_usuario("1", "Thiago")
        atv.cadastrar_livro("101", "Clean Code")

        sucesso, _ = atv.emprestar_livro("101", "1")
        self.assertTrue(sucesso)
        self.assertFalse(atv.livros["101"]["disponivel"])

        # Teste emprestar livro já emprestado
        sucesso_segundo_emprestimo, _ = atv.emprestar_livro("101", "1")
        self.assertFalse(sucesso_segundo_emprestimo)

    def test_devolver_livro(self):
        atv.cadastrar_usuario("1", "Thiago")
        atv.cadastrar_livro("101", "Clean Code")
        atv.emprestar_livro("101", "1")

        sucesso, _ = atv.devolver_livro("101")
        self.assertTrue(sucesso)
        self.assertTrue(atv.livros["101"]["disponivel"])

if __name__ == "__main__":
    unittest.main()