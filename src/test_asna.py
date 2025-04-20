import tkinter as tk
from tkinter import ttk, scrolledtext
import pyttsx3
from datetime import datetime
import PyInstaller.__main__

class AsnaApp:
    def __init__(self):
        # Configuração da janela principal
        self.window = tk.Tk()
        self.window.title("Asna - Sua Assistente")
        self.window.geometry("800x600")
        self.window.configure(bg='#f0f0f0')

        # Configurar voz
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if "portuguese" in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break

        # Área de chat
        self.chat_frame = ttk.Frame(self.window)
        self.chat_frame.pack(expand=True, fill='both', padx=10, pady=5)

        self.chat_area = scrolledtext.ScrolledText(
            self.chat_frame, 
            wrap=tk.WORD, 
            font=("Arial", 12)
        )
        self.chat_area.pack(expand=True, fill='both')

        # Campo de entrada
        self.input_frame = ttk.Frame(self.window)
        self.input_frame.pack(fill='x', padx=10, pady=5)

        self.input_field = ttk.Entry(
            self.input_frame, 
            font=("Arial", 12)
        )
        self.input_field.pack(side='left', expand=True, fill='x', padx=(0, 5))
        self.input_field.bind("<Return>", self.send_message)

        self.send_button = ttk.Button(
            self.input_frame, 
            text="Enviar",
            command=self.send_message
        )
        self.send_button.pack(side='right')

        # Inicialização
        self.welcome_message()

    def welcome_message(self):
        welcome = "Olá! Eu sou a Asna, sua assistente! Como posso ajudar? 😊"
        self.add_message("Asna", welcome)
        self.speak(welcome)

    def add_message(self, sender, message):
        timestamp = datetime.now().strftime("%H:%M")
        self.chat_area.insert(tk.END, f"[{timestamp}] {sender}: {message}\n")
        self.chat_area.see(tk.END)

    def speak(self, text):
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except:
            print("Erro ao falar")

    def send_message(self, event=None):
        message = self.input_field.get().strip()
        if message:
            self.add_message("Você", message)
            self.input_field.delete(0, tk.END)

            response = self.process_message(message)
            self.add_message("Asna", response)
            self.speak(response)

    def process_message(self, message):
        message = message.lower()
        if "olá" in message or "oi" in message:
            return "Olá! Que bom ter você aqui! 😊"
        elif "como você está" in message:
            return "Estou muito bem, obrigada por perguntar! E você? 💖"
        elif "ajuda" in message:
            return "Posso ajudar você com várias coisas! Me conte o que precisa! ✨"
        else:
            return "Estou aqui para conversar e ajudar! Me conte mais! 🌟"

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = AsnaApp()
    app.run()

    PyInstaller.__main__.run([
        'asna_app.py',
        '--onefile',
        '--windowed',
        '--name=Asna',
    ])

tkinter
pyttsx3
pyinstaller