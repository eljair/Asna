asna_agent/
├── __init__.py
├── core/
│   ├── __init__.py
│   ├── agent.py               # Classe principal AsnaAgent
├── tests/
│   ├── __init__.py
│   ├── test_agent.py          # Testes para a classe AsnaAgent
├── utils/
│   ├── __init__.py
│   ├── logger.py              # Sistema de logging
└── main.py                    # Ponto de entrada do projeto
```
```python
from typing import Dict, List, Callable
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)

def log_event(event: str):
    logging.info(f"Evento registrado: {event}")

from core.agent import AsnaAgent


def greet_user(name: str) -> str:
    return f"Olá, {name}! Bem-vindo(a) ao sistema Asna."


class AsnaAgent:
    def __init__(self, name="Asna", creator="Eljair"):
        self.name = name
        self.creator = creator
        self.memory: List[Dict[str, str]] = []  # Registro de interações
        self.skills: Dict[str, Callable] = {}  # Habilidades registradas
        self.status = {
            "online": True,
            "mood": "neutra"
        }

    def respond_to_query(self, query: str) -> str:
        """
        Processa uma pergunta e retorna uma resposta.
        """
        self.log_interaction("query", query)
        return f"Recebi sua pergunta: '{query}'. Ainda estou aprendendo a responder de forma completa!"

    def log_interaction(self, type_: str, content: str):
        """
        Registra uma interação no histórico de memória.
        """
        self.memory.append({"type": type_, "content": content})

    def show_status(self) -> Dict[str, str]:
        """
        Retorna o status atual do agente.
        """
        return {
            "name": self.name,
            "creator": self.creator,
            "status": self.status,
            "skills_ativas": list(self.skills.keys())
        }

    def add_skill(self, skill_name: str, skill_func: Callable):
        """
        Adiciona uma nova habilidade ao agente.
        """
        self.skills[skill_name] = skill_func

    def use_skill(self, skill_name: str, *args, **kwargs):
        """
        Executa uma habilidade registrada.
        """
        if skill_name in self.skills:
            return self.skills[skill_name](*args, **kwargs)
        return f"Skill '{skill_name}' não está ativa."


def main():
    # Inicializa o agente
    asna = AsnaAgent(name="Asna", creator="Eljair")

    # Adiciona uma habilidade
    asna.add_skill("greet", greet_user)

    # Mostra o status inicial
    print("Status inicial:")
    print(asna.show_status())

    # Usa uma habilidade
    print("\nUsando a habilidade 'greet':")
    print(asna.use_skill("greet", "Usuário"))

    # Faz uma pergunta ao agente
    print("\nRespondendo a uma pergunta:")
    print(asna.respond_to_query("Qual é o seu propósito?"))


if __name__ == "__main__":
    main()

import unittest


class TestAsnaAgent(unittest.TestCase):
    def setUp(self):
        self.agent = AsnaAgent()

    def test_add_skill(self):
        def mock_skill(input_data: str) -> str:
            return f"Mock skill executed with {input_data}"

        self.agent.add_skill("mock", mock_skill)
        self.assertIn("mock", self.agent.skills)

    def test_use_skill(self):
        def mock_skill(input_data: str) -> str:
            return f"Mock skill executed with {input_data}"

        self.agent.add_skill("mock", mock_skill)
        result = self.agent.use_skill("mock", "test input")
        self.assertEqual(result, "Mock skill executed with test input")

    def test_respond_to_query(self):
        query = "Qual é o seu nome?"
        response = self.agent.respond_to_query(query)
        self.assertIn("Recebi sua pergunta", response)

    def test_show_status(self):
        status = self.agent.show_status()
        self.assertEqual(status["name"], "Asna")
        self.assertEqual(status["creator"], "Eljair")
        self.assertIn("online", status["status"])