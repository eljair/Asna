import os
import json
import datetime
from typing import Dict, Any, List, Callable
from transformers import pipeline
import tkinter as tk

class AsnaCore:
    def __init__(self):
        self.name = "Asna"
        self.version = "1.0.0"
        self.data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
        self.initialize()

    def initialize(self):
        self._setup_directories()

    def _setup_directories(self):
        directories = ['data', 'logs', 'models', 'config']
        base_path = os.path.dirname(os.path.dirname(__file__))
        for dir_name in directories:
            os.makedirs(os.path.join(base_path, dir_name), exist_ok=True)

    def process_input(self, user_input: str) -> str:
        try:
            return f"Processando: {user_input}"
        except Exception as e:
            return f"Erro no processamento: {str(e)}"

class AsnaAgent:
    def __init__(self, name="Asna", creator="Eljair"):
        self.name = name
        self.creator = creator
        self.version = "0.1"
        self.skills: Dict[str, Callable[[str], str]] = {}
        self.memory: List[Dict[str, str]] = []
        self.log_interactions: List[Dict[str, str]] = []

    def add_skill(self, name: str, description: str, execute: Callable[[str], str]):
        self.skills[name] = {"description": description, "execute": execute}

    def use_skill(self, skill_name: str, input_data: str) -> str:
        if skill_name in self.skills:
            print(f"Usuário perguntou: {input_data}")
            result = self.skills[skill_name]["execute"](input_data)
            self.memory.append({"skill": skill_name, "input": input_data, "result": result})
            return result
        return f"Habilidade '{skill_name}' não encontrada."

    def process_event(self, event: Dict[str, str]):
        self.log_interactions.append({"time": datetime.datetime.now().isoformat(), "event": event})
        if event["type"] == "greeting":
            return f"Olá, {event['data'].get('name', 'usuário')}!"
        return "Evento não reconhecido."

    def status(self) -> Dict[str, str]:
        return {
            "name": self.name,
            "creator": self.creator,
            "version": self.version,
            "skills": list(self.skills.keys()),
            "memory_count": len(self.memory),
        }

if __name__ == "__main__":
    print("Inicializando a interface...")
    print("Criando interface Tkinter...")
    root = tk.Tk()
    print("Criando a aplicação...")
    app = AsnaAgent()
    print("Executando o loop principal...")
    root.mainloop()