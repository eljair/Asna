# Asna - Assistente Virtual

## Sobre
Asna é uma assistente virtual desenvolvida para ser acessível e interativa, capaz de se comunicar através de voz e texto. Ela utiliza tecnologias modernas para oferecer uma experiência amigável e eficiente.

## Requisitos do Sistema
- **Python**: Versão 3.8 ou superior
- **Sistema Operacional**: Windows 10/11 (ou compatível)
- **Hardware**:
  - Microfone (para comandos de voz)
  - Alto-falantes ou fones de ouvido (para respostas de voz)

## Estrutura do Projeto
Asna/
├── asna_app.py              # Código principal da interface gráfica
├── system_check.py          # Sistema de verificação e correção de dependências
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação do projeto

---

### **O que Este `README.md` Inclui**
1. **Descrição Geral**:
   - Explica o que é a Asna e suas capacidades.

2. **Requisitos do Sistema**:
   - Lista os pré-requisitos para executar o projeto.

3. **Instruções de Instalação**:
   - Passos claros para configurar o ambiente e testar o sistema.

4. **Como Usar**:
   - Explica como iniciar a interface web e interagir com a Asna.

5. **Estrutura do Projeto**:
   - Mostra a organização dos arquivos e diretórios.

6. **Funcionalidades**:
   - Lista os principais recursos da Asna.

7. **Contribuição e Licença**:
   - Incentiva contribuições e informa sobre a licença do projeto.

---

## Instalação

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu-usuario/Asna.git
   cd Asna
   ```

2. **Instale as Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a Interface Gráfica**:
   ```bash
   python src/asna_interface.py
   ```

---

### **Próximos Passos**
1. **Atualizar o Repositório**:
   - Substitua o conteúdo atual do `README.md` pelo texto acima.

2. **Testar as Instruções**:
   - Certifique-se de que todos os comandos e instruções funcionam corretamente.

3. **Adicionar Mais Funcionalidades**:
   - Expanda a seção de funcionalidades à medida que o projeto evolui.

Se precisar de mais ajuda ou ajustes, é só avisar! 🚀

```python
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import pyttsx3
from datetime import datetime
from system_check import SystemCheck
import sys

class AsnaApp:
    def __init__(self):
        # Verificação do sistema
        self.system_check = SystemCheck()
        if not self.system_check.check_system():
            sys.exit(1)

        # Configuração da janela principal
        try:
            self.window = tk.Tk()
            self.window.title("Asna - Sua Assistente")
            self.window.geometry("800x600")
            self.window.configure(bg='#f0f0f0')

            # Tratamento de erros para voz
            try:
                self.setup_voice()
            except Exception as e:
                messagebox.showwarning("Aviso", "Sistema de voz não disponível")
                self.engine = None

            self.setup_interface()
            self.welcome_message()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao iniciar: {str(e)}")
            sys.exit(1)

    def setup_voice(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if "portuguese" in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break

    def setup_interface(self):
        # Configuração da interface com tratamento de erros
        try:
            self.chat_frame = ttk.Frame(self.window)
            self.chat_frame.pack(expand=True, fill='both', padx=10, pady=5)

            self.chat_area = scrolledtext.ScrolledText(
                self.chat_frame, 
                wrap=tk.WORD, 
                font=("Arial", 12)
            )
            self.chat_area.pack(expand=True, fill='both')

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

        except Exception as e:
            raise Exception(f"Erro na interface: {str(e)}")

    def welcome_message(self):
        welcome = "Olá! Eu sou a Asna, sua assistente! Como posso ajudar? 😊"
        self.add_message("Asna", welcome)
        self.speak(welcome)

    def add_message(self, sender, message):
        timestamp = datetime.now().strftime("%H:%M")
        self.chat_area.insert(tk.END, f"[{timestamp}] {sender}: {message}\n")
        self.chat_area.see(tk.END)

    def speak(self, text):
        if self.engine:
            try:
                self.engine.say(text)
                self.engine.runAndWait()
            except:
                messagebox.showwarning("Aviso", "Erro ao falar")

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
        try:
            self.window.mainloop()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro na execução: {str(e)}")

if __name__ == "__main__":
    try:
        app = AsnaApp()
        app.run()
    except Exception as e:
        messagebox.showerror("Erro Fatal", str(e))
```

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asna - Assistente Virtual</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        input, button {
            padding: 10px;
            margin: 10px;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <h1>Asna - Assistente Virtual</h1>
    <form method="POST">
        <input type="text" name="pergunta" placeholder="Faça sua pergunta..." required>
        <button type="submit">Enviar</button>
    </form>
    <p><strong>Resposta:</strong> {{ resposta }}</p>
</body>
</html>
```

## Dependências do Projeto

As dependências do projeto estão listadas no arquivo `requirements.txt`. Certifique-se de instalar todas as dependências antes de executar o projeto.

### Conteúdo do `requirements.txt`:
```
flask
pyttsx3
tkinter
pyinstaller
```

## Configuração de Depuração

Adicione o seguinte arquivo `launch.json` na raiz do projeto para configurar a depuração no Visual Studio Code:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Arquivo Atual",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}
```
````

