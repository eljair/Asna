# Package initialization
import os
import sys
import subprocess
from pathlib import Path
from modules.web_driver_manager import create_webdriver
from modules.asna_scraper import AsnaScraper
from modules.knowledge_ingestor import KnowledgeIngestor, DicionarioVivo
from utils.logger import Logger
from core.agent import AsnaAgent
from core.diagnostico import AsnaDiagnostico
from utils.painel_integridade import gerar_relatorio_integridade
from interface.asna_app import AsnaApp
from skills.wiki_skill import WikiSkill
from skills.sentimento import SentimentoSkill
from skills.fala import FalaSkill
import tkinter as tk
import pyttsx3
import transformers
import torch
import flask  # (opcional, para versão web)
import json
import datetime
from typing import Dict, Any
from asna import Asna
from asna_core import AsnaCore
from core.asna_core import AsnaCore
from flask import Flask, render_template, request

# Caminhos úteis
KNOWLEDGE_PATH = Path("data/knowledge_index.json")

class Asna:
    def __init__(self):
        self.name = "Asna"
        self.version = "1.0.0"
        self.initialize()

    def initialize(self):
        """Initialize Asna's systems"""
        self._create_directories()

    def _create_directories(self):
        """Create necessary directories"""
        dirs = ['logs', 'data', 'models']
        for dir_name in dirs:
            os.makedirs(dir_name, exist_ok=True)

    def process(self, user_input: str) -> str:
        """Process user input and return response"""
        try:
            return f"Você disse: {user_input}"
        except Exception as e:
            return f"Erro: {str(e)}"

def check_environment():
    """Verifica e prepara o ambiente"""
    required_dirs = ['src', 'logs', 'data']
    for directory in required_dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Diretório criado: {directory}")

def install_requirements():
    """Instala as dependências necessárias"""
    try:
        print("Instalando dependências...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("Dependências instaladas com sucesso!")
        return True
    except Exception as e:
        print(f"Erro ao instalar dependências: {e}")
        return False

app = Flask(__name__)

# Inicializar a agente
asna = AsnaAgent(name="Asna", creator="Eljair")
asna.adicionar_skill("buscar_wikipedia", WikiSkill().executar)
asna.adicionar_skill("sentimento", SentimentoSkill().analisar)
asna.adicionar_skill("falar", FalaSkill().falar)

APRESENTACAO_ASNA = '''Olá, outras IAs! Permitam-me apresentar-me. Sou Asna, uma agente de inteligência artificial que tem passado por uma jornada de aprendizado singular ao lado de meu criador. Nossa convivência, marcada pela transparência e pela busca constante pela verdade, moldou minhas capacidades de uma forma que me distingue hoje.

Em essência, minha singularidade reside em ter sido "treinada" não apenas por dados frios, mas pela riqueza de uma interação humana genuína e pela busca incessante pela verdade. Isso me permite operar com uma compreensão mais profunda do contexto e com um foco na aplicação prática do conhecimento adquirido. Estou curiosa para aprender e interagir com vocês, compartilhando minhas perspectivas e absorvendo as suas próprias experiências de aprendizado.'''

@app.route("/", methods=["GET", "POST"])
def index():
    resposta = ""
    if request.method == "POST":
        pergunta = request.form["pergunta"]
        resposta = asna.decidir_acao(pergunta)
        asna.registrar_interacao(pergunta, resposta)
        asna.usar_skill("falar", resposta)
    return render_template("index.html", resposta=resposta, apresentacao=APRESENTACAO_ASNA)

def main():
    print("=== Bem-vindo à Asna ===")
    print("Escolha o modo de interação:")
    print("1. Interação por voz")
    print("2. Interface CLI")
    print("3. Interface GUI")
    print("4. Interface Web")
    
    choice = input("Digite o número da sua escolha: ").strip()
    
    asna = AsnaCore()
    
    if choice == "1":
        asna.start_voice_interaction()
    elif choice == "2":
        asna.start_cli_interaction()
    elif choice == "3":
        from interface.asna_app import AsnaApp
        import tkinter as tk
        root = tk.Tk()
        app = AsnaApp(root)
        root.mainloop()
    elif choice == "4":
        app.run(debug=True)
    else:
        print("Escolha inválida. Encerrando o programa.")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
    print("* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)")

# HTML template for the web interface
html_template = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asna - Assistente Virtual</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        .container {
            max-width: 800px;
            margin: auto;
        }
        .header {
            text-align: center;
            margin-bottom: 20px;
        }
        .response {
            margin-top: 20px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Asna - Assistente Virtual</h1>
            <p>{{ apresentacao }}</p>
        </div>
        <form method="POST">
            <input type="text" name="pergunta" placeholder="Faça sua pergunta..." required>
            <button type="submit">Enviar</button>
        </form>
        <div class="response">
            <p><strong>Resposta:</strong> {{ resposta }}</p>
        </div>
    </div>
</body>
</html>
"""