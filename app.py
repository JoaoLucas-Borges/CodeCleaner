import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from cleaner import procurar_chaves, limpar_arquivo

# ─── Cores ────────────────────────────────────────────────────
FUNDO    = "#1e1e2e"
CARD     = "#2a2a3d"
ROXO     = "#7c6af7"
VERMELHO = "#e05c6e"
TEXTO    = "#cdd6f4"
CINZA    = "#6c7086"


# ─── Lógica ───────────────────────────────────────────────────
arquivo_atual = ""

def selecionar_arquivo():
    global arquivo_atual
    caminho = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if caminho:
        arquivo_atual = caminho
        label_arquivo.config(text=Path(caminho).name, fg=TEXTO)

def limpar_chaves():
    if not arquivo_atual:
        messagebox.showwarning("Aviso", "Selecione um arquivo primeiro.")
        return

    chaves = procurar_chaves(arquivo_atual)

    area_resultado.config(state="normal")
    area_resultado.delete("1.0", "end")

    if not chaves:
        area_resultado.insert("end", "Nenhuma chave encontrada.")
        area_resultado.config(state="disabled")
        return

    modo = "a" if Path(".env").exists() else "w"
    with open(".env", modo) as env:
        for chave in chaves:
            env.write(f"{chave['nome_var']}={chave['valor']}\n")
            area_resultado.insert("end", f"[{chave['servico']}]  {chave['nome_var']}  →  .env\n")

    limpar_arquivo(arquivo_atual, chaves)
    area_resultado.insert("end", "\n✓  Arquivo limpo com sucesso!")
    area_resultado.config(state="disabled")


# ─── Interface ────────────────────────────────────────────────
def criar_janela():
    janela = tk.Tk()
    janela.title("Code Cleaner")
    janela.geometry("560x480")
    janela.resizable(False, False)
    janela.configure(bg=FUNDO)
    return janela

def criar_titulo(janela):
    tk.Label(janela, text="Code Cleaner",
             font=("Segoe UI", 22, "bold"), bg=FUNDO, fg=ROXO).pack(pady=(28, 2))
    tk.Label(janela, text="Detecta e move chaves de API para o .env",
             font=("Segoe UI", 11), bg=FUNDO, fg=CINZA).pack()

def criar_secao_arquivo(janela):
    painel = tk.Frame(janela, bg=CARD)
    painel.pack(fill="x", padx=28, pady=20)

    tk.Label(painel, text="ARQUIVO ALVO",
             font=("Segoe UI", 9, "bold"), bg=CARD, fg=CINZA).pack(anchor="w", padx=16, pady=(14, 4))

    linha = tk.Frame(painel, bg=CARD)
    linha.pack(fill="x", padx=16, pady=(0, 14))

    label = tk.Label(linha, text="Nenhum arquivo selecionado",
                     font=("Segoe UI", 12), bg=CARD, fg=CINZA, anchor="w")
    label.pack(side="left", fill="x", expand=True)

    tk.Button(linha, text="Selecionar", command=selecionar_arquivo,
              font=("Segoe UI", 11), bg=ROXO, fg="white", relief="flat",
              padx=14, pady=6, cursor="hand2",
              activebackground="#6a5de0", activeforeground="white").pack(side="right")

    return label  # retornamos o label para poder atualizar o texto dele depois

def criar_botao_limpar(janela):
    tk.Button(janela, text="Limpar Chaves", command=limpar_chaves,
              font=("Segoe UI", 13, "bold"), bg=VERMELHO, fg="white", relief="flat",
              pady=12, cursor="hand2",
              activebackground="#c04a5c", activeforeground="white").pack(fill="x", padx=28)

def criar_secao_resultado(janela):
    painel = tk.Frame(janela, bg=CARD)
    painel.pack(fill="both", expand=True, padx=28, pady=20)

    tk.Label(painel, text="RESULTADO",
             font=("Segoe UI", 9, "bold"), bg=CARD, fg=CINZA).pack(anchor="w", padx=16, pady=(14, 4))

    area = tk.Text(painel, font=("Consolas", 12), bg=FUNDO, fg=TEXTO,
                   relief="flat", insertbackground=TEXTO, state="disabled", wrap="word")
    area.pack(fill="both", expand=True, padx=16, pady=(0, 16))

    return area  # retornamos a área para poder escrever nela depois


# ─── Início ───────────────────────────────────────────────────
janela        = criar_janela()
criar_titulo(janela)
label_arquivo = criar_secao_arquivo(janela)
criar_botao_limpar(janela)
area_resultado = criar_secao_resultado(janela)

janela.mainloop()
