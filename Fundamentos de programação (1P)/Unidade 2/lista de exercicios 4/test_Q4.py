import unittest
import io
import sys
import os
from contextlib import redirect_stdout

class TestQ4(unittest.TestCase):

    def setUp(self):
        """Apaga o arquivo antes de cada teste."""
        if os.path.exists("Q4_nomes.txt"):
            os.remove("Q4_nomes.txt")

    def run_program(self, inputs):
        """Executa o código da Q4 simulando entradas e captura a saída."""
        import importlib.util

        sys.stdin = io.StringIO("\n".join(inputs) + "\n")
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            spec = importlib.util.spec_from_file_location("Q4", "Q4.py")
            Q4 = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(Q4)

        return captured_output.getvalue()

    def test_nomes_repetidos(self):
        """Testa se o programa detecta nomes repetidos corretamente."""
        entradas = [
            "Ana",
            "ana",
            "Carlos",
            "Beatriz",
            "carlos",
            "Sair"
        ]

        saida = self.run_program(entradas)

        # Verifica se os nomes repetidos aparecem na saída
        self.assertIn("ana", saida)
        self.assertIn("carlos", saida)
        # Verifica se mostra a contagem de repetições
        self.assertRegex(saida, r"ana: ?\d+ vezes")
        self.assertRegex(saida, r"carlos: ?\d+ vezes")

    def test_nenhum_repetido(self):
        """Testa o caso em que não há nomes repetidos."""
        entradas = [
            "João",
            "Maria",
            "Pedro",
            "Sair"
        ]

        saida = self.run_program(entradas)

        # Como não há repetição, o programa só deve listar uma vez cada nome
        self.assertIn("joão", saida.lower())
        self.assertIn("maria", saida.lower())
        self.assertIn("pedro", saida.lower())
        self.assertNotIn("vezes", saida.lower())

    def test_entrada_vazia(self):
        """Testa se o programa lida com entradas vazias."""
        entradas = [
            "",
            "Lucas",
            "Sair"
        ]

        saida = self.run_program(entradas)

        self.assertIn("Entrada inválida", saida)

if __name__ == "__main__":
    unittest.main()
