import re
import tkinter as tk
from pathlib import Path
from dotenv import load_dotenv

caminho = "tests/test_main.py"

padroes_de_chaves = {
    "Openai":    r'([A-Za-z_][A-Za-z0-9_]*)\s*=\s*["\']?(sk-[a-zA-Z0-9_-]{20,})',
    # Antropic usa um esquema parecido e apenas ajusta o padrao da OPENAI
    "AWS":       r'([A-Za-z_][A-Za-z0-9_]*)\s*=\s*["\']?(AKIA[A-Z0-9]{16})',
    "Firebase":  r'([A-Za-z_][A-Za-z0-9_]*)\s*=\s*["\']?(AIza[0-9A-Za-z_-]{35})',
    "LangSmith": r'([A-Za-z_][A-Za-z0-9_]*)\s*=\s*["\']?(lsv2_[a-zA-Z0-9_-]{20,})',
}

def procurar_chaves(caminho_arquivo):
    chaves_encontradas = []

    with open(caminho_arquivo, "r") as arquivo:
        for linha in arquivo:
            for servico, padrao in padroes_de_chaves.items():
                match = re.search(padrao, linha)
                if match:
                    servico_real = "Anthropic" if servico == "Openai" and match.group(2).startswith("ant-") else servico
                    print(f"chave do(a) {servico_real} encontrada!")
                    chaves_encontradas.append({
                        "servico" : servico_real,
                        "nome_var": match.group(1),
                        "valor": match.group(2)
                    })

    return chaves_encontradas


def limpar_arquivo(caminho_arquivo, chaves):
    with open(caminho_arquivo, "r") as arquivo:
        conteudo = arquivo.read()

    for chave in chaves:
        padrao = r'["\']?' + re.escape(chave["valor"]) + r'["\']?'
        conteudo = re.sub(padrao, f'os.environ.get("{chave["nome_var"]}")', conteudo)
        print(f"{chave['nome_var']} substituída no arquivo!")

    if "import os" not in conteudo:
        conteudo = "import os\n" + conteudo

    #Reescreve o arquivo com as chaves ocultadas
    with open(caminho_arquivo, "w") as f:
        f.write(conteudo)


chaves = procurar_chaves(caminho)
print("\n")

if chaves:
    modo = "a" if Path(".env").exists() else "w"

    with open(".env", modo) as arquivo_env:
        for chave in chaves:
            arquivo_env.write(f"{chave['nome_var']}={chave['valor']}\n")
            print(f"{chave['nome_var']} do servico {chave['servico']} escrita no .env!")

    print("\n")
    limpar_arquivo(caminho, chaves)

else:
    print("Não foi localizada nenhuma API KEY, finalizando...")