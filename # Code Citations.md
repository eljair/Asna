# Code Citations

## License: unknown
https://github.com/ifpb/html-guide/tree/9750443f462abfb8a5d1192b6e69e6682dce9aa6/html/syntax/README.md

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asna - Assistente Virtual</title>
    <link rel="stylesheet" href="assets/style.css">
    <link rel="stylesheet" href="assets/style.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        h2, h3, h4 {
            color: #333;
        }
        form {
            margin-block-start: 20px;
        }
        input, button {
            padding: 10px;
            font-size: 16px;
            margin: 5px 0;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h2>🧠 Apresentação da Asna</h2>
    <p style="white-space: pre-wrap;">{{ apresentacao }}</p>

    <h3>Faça sua pergunta:</h3>
    <form method="post">
        <input type="text" name="pergunta" placeholder="Digite sua pergunta..." required />
        <button type="submit">Perguntar</button>
    </form>

    {% if resposta %}
        <h4>📣 Resposta:</h4>
        <p>{{ resposta }}</p>
    {% endif %}

    <script>
        document.querySelector("form").addEventListener("submit", function(event) {
            const pergunta = document.querySelector("input[name='pergunta']").value;
            if (!pergunta.trim()) {
                alert("Por favor, digite uma pergunta.");
                event.preventDefault();
            }
        });
    </script>
</body>
</html>
```


## License: unknown
https://github.com/ermogenes/aulas-programacao-web/tree/45b8f63884537fe1d1ac6cc8a44b423700f776e0/content/hello-world-gh-pages.md

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asna - Assistente Virtual</title>
    <link rel="stylesheet" href="assets/style.css">
    <link rel="stylesheet" href="assets/style.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        h2, h3, h4 {
            color: #333;
        }
        form {
            margin-block-start: 20px;
        }
        input, button {
            padding: 10px;
            font-size: 16px;
            margin: 5px 0;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h2>🧠 Apresentação da Asna</h2>
    <p style="white-space: pre-wrap;">{{ apresentacao }}</p>

    <h3>Faça sua pergunta:</h3>
    <form method="post">
        <input type="text" name="pergunta" placeholder="Digite sua pergunta..." required />
        <button type="submit">Perguntar</button>
    </form>

    {% if resposta %}
        <h4>📣 Resposta:</h4>
        <p>{{ resposta }}</p>
    {% endif %}

    <script>
        document.querySelector("form").addEventListener("submit", function(event) {
            const pergunta = document.querySelector("input[name='pergunta']").value;
            if (!pergunta.trim()) {
                alert("Por favor, digite uma pergunta.");
                event.preventDefault();
            }
        });
    </script>
</body>
</html>
```


## License: unknown
https://github.com/oak99x/Playing-with-HTML-CSS/tree/7f1172c13ce959ccb7e9030c68f37a2165760ff7/html-css-exercicio-post-instagram/README.md

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asna - Assistente Virtual</title>
    <link rel="stylesheet" href="assets/style.css">
    <link rel="stylesheet" href="assets/style.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        h2, h3, h4 {
            color: #333;
        }
        form {
            margin-block-start: 20px;
        }
        input, button {
            padding: 10px;
            font-size: 16px;
            margin: 5px 0;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h2>🧠 Apresentação da Asna</h2>
    <p style="white-space: pre-wrap;">{{ apresentacao }}</p>

    <h3>Faça sua pergunta:</h3>
    <form method="post">
        <input type="text" name="pergunta" placeholder="Digite sua pergunta..." required />
        <button type="submit">Perguntar</button>
    </form>

    {% if resposta %}
        <h4>📣 Resposta:</h4>
        <p>{{ resposta }}</p>
    {% endif %}

    <script>
        document.querySelector("form").addEventListener("submit", function(event) {
            const pergunta = document.querySelector("input[name='pergunta']").value;
            if (!pergunta.trim()) {
                alert("Por favor, digite uma pergunta.");
                event.preventDefault();
            }
        });
    </script>
</body>
</html>
```

Enumerating objects: X, done.
Compressing objects: 100% (X/X), done.
Writing objects: 100% (X/X), done.
To https://github.com/eljair/asna-v1.git
 * [new branch]      main -> main

