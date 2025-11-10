import unittest
import io
import sys
import os
from contextlib import redirect_stdout

class TestQ2(unittest.TestCase):

    def setUp(self):
        """Remove o arquivo antes de cada teste."""
        if os.path.exists("Q2_votos.txt"):
            os.remove("Q2_votos.txt")

    def run_program(self, inputs):
        """Executa o programa Q2 simulando entradas e captura a saída."""
        import importlib.util

        sys.stdin = io.StringIO("\n".join(inputs) + "\n")
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            spec = importlib.util.spec_from_file_location("Q2", "Q2.py")
            Q2 = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(Q2)

        return captured_output.getvalue()

    def test_votacao_star_wars_ganha(self):
        """Teste: maioria vota em Star Wars."""
        entradas = ["1", "1", "1", "2", "1", "1", "2", "1", "1", "1"]
        saida = self.run_program(entradas)

        self.assertIn("Ganhador: Star Wars", saida)
        self.assertIn("Votos nulos: 0", saida)

    def test_votacao_star_trek_ganha(self):
        """Teste: maioria vota em Star Trek."""
        entradas = ["2", "2", "2", "2", "1", "2", "2", "1", "2", "2"]
        saida = self.run_program(entradas)

        self.assertIn("Ganhador: Star Trek", saida)
        self.assertIn("Votos nulos: 0", saida)

    def test_empate(self):
        """Teste: empate entre os dois filmes."""
        entradas = ["1", "2", "1", "2", "1", "2", "1", "2", "1", "2"]
        saida = self.run_program(entradas)

        self.assertIn("Empate", saida)
        self.assertIn("Votos nulos: 0", saida)

    def test_votos_nulos(self):
        """Teste: votos inválidos são contados como nulos."""
        entradas = ["1", "2", "5", "0", "7", "1", "2", "x", "3", "2"]
        saida = self.run_program(entradas)

        self.assertIn("Votos nulos", saida)
        # deve haver pelo menos 3 votos nulos
        self.assertTrue("Votos nulos: 4" in saida or "Votos nulos: 5" in saida)

if __name__ == "__main__":
    unittest.main()
