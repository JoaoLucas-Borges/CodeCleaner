<img width="1500" height="500" alt="Code Cleaner" src="https://github.com/user-attachments/assets/62ac6dfa-a16c-4ae1-a0a0-99a28715e6f7" />

> A ferramenta local que detecta API Keys expostas no seu código e as trata da forma correta — sem que nenhum dado saia da sua máquina.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/Execução-100%25%20Local-success" alt="100% Local">
  <img src="https://img.shields.io/badge/Interface-Tkinter-orange" alt="Tkinter">
</p>

## O problema
 
A produção moderna de software depende de diversos serviços de terceiros: aplicações em nuvem, bancos de dados, LLMs e outros. A conexão entre eles costuma ser feita por **API Keys** (chaves de acesso) — um sistema eficiente, porém com um risco relevante.
 
Essas chaves são geradas e associadas a uma conta, já que os serviços de terceiros cobram com base no consumo. O problema está exatamente aí: caso o valor de uma API Key fique exposto, agentes maliciosos podem usá-la para consumir esses serviços livremente — e quem arca com as cobranças é o titular da chave.
 
Por mais cauteloso que o programador seja, um commit acidental em um repositório público no GitHub é mais comum do que parece.
 
## A solução
 
Daí surgiu a ideia do **Code Cleaner**: uma ferramenta que lê códigos localmente e, ao encontrar API Keys expostas, as trata da maneira correta:
 
1. Salva os valores em um arquivo `.env`
2. Substitui cada ocorrência no código por `os.getenv("variavel")`
3. Retorna o arquivo limpo e o `.env` devidamente preenchido
---
 
## Requisitos
 
### Funcionais
- Detectar API Keys *hardcoded* no código fornecido
- Substituir as chaves encontradas por `os.getenv("variavel")`
- Gerar arquivo `.env` com os valores das chaves
- Retornar o arquivo original limpo
### Não-funcionais
- **Execução 100% local** — nenhum dado é enviado para nenhum servidor de nenhuma natureza
- Compatível com Python 3.8+
- Interface simples e intuitiva via Tkinter
---
 
## Bibliotecas utilizadas
 
| Biblioteca | Função |
|------------|--------|
| `Tkinter` | Interface gráfica da aplicação |
| `re` | Detecção de padrões via regex — o coração da ferramenta |
| `pathlib` | Manipulação de caminhos de arquivos |
| `python-dotenv` | Leitura e escrita do `.env` |
 
---
 
## Como rodar
 
```bash
git clone https://github.com/joaolucas-borges/CodeCleaner
cd CodeCleaner
pip install python-dotenv
python ./app.py
```
 
---
 
## Diagrama de arquitetura
<img width="1500" height="500" alt="Diagrama_de_Arquitetura" src="https://github.com/user-attachments/assets/832d7928-e195-4316-b56c-3d7299ae9c64" />

## Fluxograma
<img width="1500" height="500" alt="Fluxograma" src="https://github.com/user-attachments/assets/f07c1823-c236-45de-a526-8186b9b1615b" />

## Diagrama de casos de uso 
<img width="1500" height="500" alt="Diagrama_de_casos_de_uso" src="https://github.com/user-attachments/assets/3f5520ae-0780-4f0f-bc92-4399e9245b08" />

---

## Como o re identifica uma API KEY via regex
Basicamente existe um dicionário contendo os padrões de chaves de cada serviço (No momento só estão disponíveis chaves da OpenAI, Anthropic, AWS, Firebase e LangSmith), definidos dessa forma: {"servico":"Formato da chave"}. Com base nisso, existe uma função que se chama `procurar_chaves()` onde o sistema utiliza o `re.search()` (da biblioteca re) e funciona rodando o arquivo_exposto.py + um modelo de chave do dicionário, caso o `re.search()` encontre algum termo semelhante ao modelo de chave a o código salva esse caso em uma lista de chaves encontradas com as informações de provedor, nome da variável e valor da variável(API KEY) e a função termina retornando essa lista de chaves encontradas

---

## Limitações:
A ferramenta cumpre bem seu propósito, mas tem limites conhecidos:
 
- Funciona apenas com arquivos `.py`
- Detecta somente chaves dos serviços atualmente cadastrados:
  - OpenAI
  - Anthropic
  - AWS
  - Firebase
  - LangSmith
