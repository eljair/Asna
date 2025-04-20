import tkinter as tk
from tkinter import ttk
from pathlib import Path
import json
import pyttsx3
from core.memory import Memory
from skills.wiki_skill import WikiSkill
import os
import datetime
import speech_recognition as sr
from typing import Dict, Any
from config.config import CONFIG
from asna import Asna
import sys
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG = {
    "name": "Asna",
    "version": "1.0.0",
    "voice_enabled": False,
    "log_path": os.path.join(BASE_DIR, "logs"),
    "data_path": os.path.join(BASE_DIR, "data"),
    "models_path": os.path.join(BASE_DIR, "models")
}

class Asna:
    def __init__(self):
        self.name = CONFIG["name"]
        self.version = CONFIG["version"]
        self.memory = {}
        self.initialize_system()

    def initialize_system(self):
        """Initialize all necessary systems"""
        self._create_directories()
        self._load_memory()

    def _create_directories(self):
        """Create necessary directories if they don't exist"""
        for path in [CONFIG["log_path"], CONFIG["data_path"], CONFIG["models_path"]]:
            os.makedirs(path, exist_ok=True)

    def _load_memory(self):
        """Load previous memory if exists"""
        memory_file = os.path.join(CONFIG["data_path"], "memory.json")
        if os.path.exists(memory_file):
            with open(memory_file, 'r', encoding='utf-8') as f:
                self.memory = json.load(f)

    def process_command(self, command: str) -> str:
        """Process user commands"""
        command = command.lower().strip()

        if "hello" in command or "hi" in command:
            return f"Hello! I'm {self.name}, your AI assistant."
        elif "how are you" in command:
            return "I'm functioning well, thank you for asking!"
        elif "help" in command:
            return self._get_help_message()
        else:
            return "I'm still learning to process this type of command."

    def _get_help_message(self) -> str:
        return """
        I can help you with:
        - Basic conversation (hello, how are you)
        - System information
        - More features coming soon!
        """

class DicionarioVivo:
    def __init__(self, caminho_arquivo="knowledge_index.json"):
        self.caminho = Path(caminho_arquivo)
        if self.caminho.exists():
            with open(self.caminho, "r", encoding="utf-8") as f:
                self.conteudo = json.load(f)
        else:
            self.conteudo = {}

    def responder(self, termo: str) -> str:
        termo = termo.lower().strip()
        item = self.conteudo.get(termo)
        if not item:
            return f"Ainda não aprendi sobre '{termo}'."
        resposta = f"🧠 {termo.title()}:\n{item['definicao']}\n"
        if item.get("relacionados"):
            resposta += f"\n🔗 Relacionados: {', '.join(item['relacionados'])}"
        return resposta

class AsnaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teste AsnaApp")
        self.root.geometry("300x200")
        tk.Label(root, text="Interface funcionando!").pack(pady=20)

def test_asna():
    try:
        # Inicializa o sistema de voz
        engine = pyttsx3.init()
        
        # Teste de comunicação
        print("=== Teste de Comunicação com Asna ===")
        engine.say("Olá! Aqui é a Asna. Você está me ouvindo?")
        engine.runAndWait()
        
        return True
    except Exception as e:
        print(f"Erro na comunicação: {e}")
        return False

def main():
    print("Iniciando Asna...")
    print("Asna v1.0.0 iniciada com sucesso!")
    print("Digite 'help' para ver os comandos disponíveis")
    print("Digite 'exit' para sair")

    asna = Asna()

    while True:
        try:
            user_input = input("\nVocê > ").strip()

            if user_input.lower() == 'exit':
                print("Até logo!")
                break

            response = asna.process_command(user_input)
            print(f"\nAsna > {response}")

        except KeyboardInterrupt:
            print("\nPrograma finalizado pelo usuário")
            break
        except Exception as e:
            print(f"Erro: {str(e)}")

if __name__ == "__main__":
    test_asna()
    main()

# Required dependencies
# SpeechRecognition==3.8.1
# pyaudio==0.2.11
# numpy==1.21.0
# requests==2.26.0
# python-dotenv==0.19.0
# pyttsx3
# tkinter