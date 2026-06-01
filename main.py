import os
import re
import tkinter as tk
from pathlib import Path
from dotenv import load_dotenv

padroes_de_chaves = {
    "Openai": r"sk-[a-zA-Z0-9_-]{20,}",
    "Anthropic": r"sk-ant-[a-zA-Z0-9_-]{20,}",
    "AWS": r"AKIA[A-Z0-9]{16}",
    "Firebase": r"AIza[0-9A-Za-z_-]{35}",
    "LangSmith": r"lsv2_[a-zA-Z0-9_-]{20,}"
}

def procurar_chaves(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        for linha in arquivo:
            for servico, padrao in padroes_de_chaves.items():
                match = re.search(padrao, linha)
                if match:
                    print(f"chave do(a) {servico} encontrada!")

caminho = "tests/test_main.py"

procurar_chaves(caminho)