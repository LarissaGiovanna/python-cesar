import unittest
import io
import sys
import os
from contextlib import redirect_stdout

class TestQ3(unittest.TestCase):

    def setUp(self):
        """Remove o arquivo antes de cada teste."""
        if os.path.exists("Q3_numeros.txt"):
            os.remove("Q3_numeros.txt")

    def run_program(self, inputs):
        """Executa o programa Q3 simulando entradas e captura a saída."""
        import importlib.util

        sys.stdin = io.StringIO("\n".join(inputs) + "\n")
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            spec = importlib.util.spec_from_file_location("Q3", "Q3.py")
            Q3 = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(Q3)

        return captured_output.getvalue()

    def test_escrita_numeros_maiores(self):
        """Testa se apenas números maiores são salvos."""
        entradas = [
            "3",      # escolhe escrever
            "5",      # primeiro número
            "2",      # menor -> não será salvo
            "10",     # maior -> será salvo
            "a",      # sai da escrita
            "1"       # sair do menu
        ]

        saida = self.run_program(entradas)

        # Verifica se mensagem de rejeição aparece
        self.assertIn("Número menor ou igual aos números já existentes", saida)

        # Lê o conteúdo do arquivo gerado
        with open("Q3_numeros.txt", "r") as f:
            conteudo = f.read().strip().splitlines()

        # Apenas os números 5 e 10 devem estar salvos
        self.assertEqual(conteudo, ["5", "10"])

    def test_leitura_arquivo(self):
        """Testa se o programa consegue ler o conteúdo do arquivo."""
        # Cria arquivo manualmente
        with open("Q3_numeros.txt", "w") as f:
            f.write("1\n2\n3\n")

        entradas = [
            "2",  # opção para ler o arquivo
            "1"   # sair
        ]

        saida = self.run_program(entradas)

        self.assertIn("Conteúdo do arquivo", saida)
        self.assertIn("1", saida)
        self.assertIn("2", saida)
        self.assertIn("3", saida)

    def test_arquivo_nao_existe(self):
        """Testa o caso em que o arquivo ainda não existe."""
        entradas = [
            "2",      # tentar ler o arquivo
            "nao",    # não criar novo
            "1"       # sair
        ]

        saida = self.run_program(entradas)

        self.assertIn("não foi encontrado", saida.lower())
        self.assertIn("quer criar um agora", saida.lower())

if __name__ == "__main__":
    unittest.main()
