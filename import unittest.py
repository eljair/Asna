import unittest
from unittest.mock import MagicMock
from AsnaCore import AsnaAgent, Skill

# test_AsnaCore.py

class TestAsnaAgent(unittest.TestCase):
    def setUp(self):
        self.agent = AsnaAgent()
        self.mock_producer = MagicMock()
        self.agent.producer = self.mock_producer  # Mock Kafka producer

    def test_add_skill(self):
        def mock_skill(input_data: str) -> str:
            return f"Mock skill executed with {input_data}"
        
        skill = Skill(name="mock", description="Mock skill", execute=mock_skill)
        self.agent.add_skill(skill)
        self.assertIn("mock", self.agent.skills)
        self.assertEqual(self.agent.skills["mock"].description, "Mock skill")

    def test_use_skill(self):
        def mock_skill(input_data: str) -> str:
            return f"Mock skill executed with {input_data}"
        
        skill = Skill(name="mock", description="Mock skill", execute=mock_skill)
        self.agent.add_skill(skill)
        result = self.agent.use_skill("mock", "test input")
        self.assertEqual(result, "Mock skill executed with test input")

    def test_processar_evento_mensagem_usuario(self):
        evento = {
            "tipo": "mensagem_usuario",
            "dados": {"nome": "TestUser"}
        }
        self.agent.processar_evento(evento)
        self.mock_producer.send.assert_called_once_with(
            "asna_respostas",
            {"resposta": "Olá, TestUser! Estou aqui com você no BIGQD.IA 🌐"}
        )

    def test_status(self):
        status = self.agent.status()
        self.assertEqual(status["name"], "Asna")
        self.assertEqual(status["creator"], "Eljair")
        self.assertIn("recent_memory", status)

if __name__ == "__main__":
    unittest.main()import unittest
from unittest.mock import patch, MagicMock
from AsnaCore import AsnaAgent

# test_AsnaCore.py

class TestAsnaAgent(unittest.TestCase):
    def setUp(self):
        self.agent = AsnaAgent()

    @patch("AsnaCore.producer")
    def test_processar_evento_mensagem_usuario(self, mock_producer):
        evento = {
            "tipo": "mensagem_usuario",
            "dados": {"nome": "Teste"}
        }
        self.agent.processar_evento(evento)
        mock_producer.send.assert_called_with(
            "asna_respostas", {"resposta": "Olá, Teste! Estou aqui com você no BIGQD.IA 🌐"}
        )

    def test_processar_evento_generico(self):
        evento = {
            "tipo": "evento_generico",
            "dados": {"info": "Teste"}
        }
        with patch("builtins.print") as mock_print:
            self.agent.processar_evento(evento)
            mock_print.assert_called_with("[ASNA][...] Evento genérico recebido: {'tipo': 'evento_generico', 'dados': {'info': 'Teste'}}")

    def test_add_skill(self):
        def mock_skill(input_data: str) -> str:
            return f"Mock skill executed with {input_data}"
        
        skill = {"name": "mock", "description": "Mock skill", "execute": mock_skill}
        self.agent.add_skill(skill)
        self.assertIn("mock", self.agent.skills)

    def test_use_skill(self):
        def mock_skill(input_data: str) -> str:
            return f"Mock skill executed with {input_data}"
        
        skill = {"name": "mock", "description": "Mock skill", "execute": mock_skill}
        self.agent.add_skill(skill)
        result = self.agent.use_skill("mock", "test input")
        self.assertEqual(result, "Mock skill executed with test input")

if __name__ == "__main__":
    unittest.main()