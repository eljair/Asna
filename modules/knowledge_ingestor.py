class DicionarioVivo:
    def __init__(self, caminho_arquivo="knowledge_index.json"):
        self.caminho_arquivo = Path(caminho_arquivo)
        self.conteudo = self._carregar() if self.caminho_arquivo.exists() else {}

    def _carregar(self):
        with open(self.caminho_arquivo, "r", encoding="utf-8") as f:
            return json.load(f)

    def _salvar(self):
        with open(self.caminho_arquivo, "w", encoding="utf-8") as f:
            json.dump(self.conteudo, f, ensure_ascii=False, indent=2)

    def registrar_conhecimento(self, termo, definicao, fonte=None, relacionados=None):
        termo = termo.lower().replace("_", " ").strip()
        if termo not in self.conteudo:
            self.conteudo[termo] = {
                "definicao": definicao[:1000],
                "fontes": [fonte] if fonte else [],
                "relacionados": relacionados or [],
                "exemplos": []
            }
        else:
            if fonte and fonte not in self.conteudo[termo]["fontes"]:
                self.conteudo[termo]["fontes"].append(fonte)
            if relacionados:
                self.conteudo[termo]["relacionados"].extend(
                    [rel for rel in relacionados if rel not in self.conteudo[termo]["relacionados"]]
                )
        self._salvar()

    def consultar(self, termo):
        return self.conteudo.get(termo.lower().replace("_", " ").strip(), "Ainda não aprendi sobre 'termo desconhecido'.")

# Example usage
dicionario = DicionarioVivo()
dicionario.registrar_conhecimento(
    termo="inteligência artificial",
    definicao="A inteligência artificial é o campo da ciência da computação voltado para criar sistemas capazes de simular comportamentos inteligentes.",
    fonte="Wikipedia",
    relacionados=["redes neurais", "machine learning"]
)