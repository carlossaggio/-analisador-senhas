import unittest

from analisador_senhas import analisar_senha, contem_repeticao, contem_sequencia


class TestAnalisadorSenhas(unittest.TestCase):
    def test_senha_vazia(self):
        resultado = analisar_senha("")
        self.assertEqual(resultado["nivel"], "Muito fraca")

    def test_senha_comum(self):
        resultado = analisar_senha("12345678")
        self.assertLessEqual(resultado["pontuacao"], 10)

    def test_senha_longa(self):
        resultado = analisar_senha("Aero#Roxo?H27_trilho")
        self.assertEqual(resultado["nivel"], "Forte")

    def test_senha_curta_nao_recebe_nota_alta(self):
        resultado = analisar_senha("Ab3!")
        self.assertLessEqual(resultado["pontuacao"], 20)

    def test_reconhece_sequencia(self):
        self.assertTrue(contem_sequencia("Teste5678!"))
        self.assertTrue(contem_sequencia("Zyxw!2026"))

    def test_reconhece_repeticao(self):
        self.assertTrue(contem_repeticao("CasaAAAA2026"))
        self.assertTrue(contem_repeticao("abcabcabc#"))

    def test_sem_sequencia_previsivel(self):
        self.assertFalse(contem_sequencia("Vento#Nuvem29"))

    def test_sem_repeticao(self):
        self.assertFalse(contem_repeticao("Vento#Nuvem29"))

    def test_nao_altera_entrada(self):
        senha = "MeuTeste#527!"
        analisar_senha(senha)
        self.assertEqual(senha, "MeuTeste#527!")


if __name__ == "__main__":
    unittest.main()
