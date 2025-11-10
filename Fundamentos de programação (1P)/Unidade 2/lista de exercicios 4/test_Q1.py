import unittest
import io
import sys
import os
from contextlib import redirect_stdout

class TestQ1(unittest.TestCase):

    def setUp(self):
        """Remove o arquivo antes de cada teste, se existir."""
        if os.path.exists("Q1_enderecos_ip.txt"):
            os.remove("Q1_enderecos_ip.txt")

    def run_program(self, inputs):
        """Executa o código da Q1 simulando entradas e captura a saída."""
        import importlib.util

        # Cria uma string com as entradas simuladas
        sys.stdin = io.StringIO("\n".join(inputs) + "\n")

        # Captura o que o programa imprime
        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            # Carrega dinamicamente o código do arquivo original
            spec = importlib.util.spec_from_file_location("Q1", "Q1.py")
            Q1 = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(Q1)

        return captured_output.getvalue()

    def test_ips_validos_invalidos(self):
        """Verifica se o programa classifica corretamente IPs válidos e inválidos."""
        entradas = [
            "200.135.80.9",   # válido
            "192.268.1.1",    # inválido
            "8.35.67.74",     # válido
            "257.32.4.5",     # inválido
            "85.345.1.2",     # inválido
            "1.2.3.4",        # válido
            "9.8.234.5",      # válido
            "192.168.0.256"   # inválido
        ]

        saida = self.run_program(entradas)

        # Verifica se os IPs válidos aparecem na saída
        for ip in ["200.135.80.9", "8.35.67.74", "1.2.3.4", "9.8.234.5"]:
            self.assertIn(ip, saida)

        # Verifica se os IPs inválidos aparecem na saída
        for ip in ["192.268.1.1", "257.32.4.5", "85.345.1.2", "192.168.0.256"]:
            self.assertIn(ip, saida)

        # Garante que o texto esperado esteja na saída
        self.assertIn("Válidos", saida)
        self.assertIn("Inválidos", saida)

if __name__ == "__main__":
    unittest.main()