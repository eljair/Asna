import unittest
from core import AsnaAgent

class TestAsnaAgent(unittest.TestCase):
    def setUp(self):
        self.agent = AsnaAgent()

    def test_add_skill(self):
        def mock_skill(input_data: str) -> str:
            return f"Mock skill executed with {input_data}"
        
        self.agent.add_skill("mock", "Mock skill", mock_skill)
        self.assertIn("mock", self.agent.skills)

    def test_use_skill(self):
        def mock_skill(input_data: str) -> str:
            return f"Mock skill executed with {input_data}"
        
        self.agent.add_skill("mock", "Mock skill", mock_skill)
        result = self.agent.use_skill("mock", "test input")
        self.assertEqual(result, "Mock skill executed with test input")

    def test_memory_remember(self):
        self.agent.memory.remember("Test entry")
        self.assertIn("Test entry", self.agent.memory.log[-1])

    def test_memory_retrieve(self):
        for i in range(10):
            self.agent.memory.remember(f"Entry {i}")
        recent_entries = self.agent.memory.retrieve(5)
        self.assertEqual(len(recent_entries), 5)
        self.assertEqual(recent_entries, self.agent.memory.log[-5:])

    def test_processar_evento(self):
        evento = {"tipo": "mensagem_usuario", "dados": {"nome": "Teste"}}
        self.agent.processar_evento(evento)
        self.assertIn(evento, self.agent.memoria_curta)
        self.assertIn("hora", self.agent.log_interacoes[-1])
        self.assertEqual(self.agent.log_interacoes[-1]["tipo"], "mensagem_usuario")

if __name__ == "__main__":
    unittest.main()

python -m unittest discover -s tests -p "test_*.py"

{
  "python.analysis.extraPaths": ["./AsnaCore/src"]
}