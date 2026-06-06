<img width="1500" height="500" alt="Code Cleaner" src="https://github.com/user-attachments/assets/62ac6dfa-a16c-4ae1-a0a0-99a28715e6f7" />

<p align="center">
  <em>A ferramenta local que detecta API Keys expostas no seu código e as trata da forma correta — sem que nenhum dado saia da sua máquina.</em>
</p>

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
## Demonstração
 
<p align="center">
  <em><img width="1500" height="800" alt="DemoCodeCleaner" src="https://github.com/user-attachments/assets/58bd0fab-6ab5-4776-b26a-74630c3bf7c2" /></em>
  <!-- <img src="LINK_DO_SEU_GIF_AQUI" alt="Code Cleaner em ação" width="700"> -->
</p>
 
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
 
## Como funciona a detecção
 
A detecção é baseada em um **dicionário** que mapeia cada serviço ao padrão da sua chave, no formato `{"servico": "formato da chave"}`. Atualmente estão cadastrados os padrões da OpenAI, Anthropic, AWS, Firebase e LangSmith.
 
A função `procurar_chaves()` percorre esse dicionário e, para cada padrão, usa o `re.search()` (da biblioteca `re`) para varrer o conteúdo do arquivo fornecido. Quando o `re.search()` encontra um trecho que corresponde ao padrão de algum serviço, o caso é salvo em uma **lista de chaves encontradas** com três informações: o **provedor**, o **nome da variável** e o **valor da variável** (a API Key em si). Ao final da varredura, a função retorna essa lista.
 
---
 
## Diagramas
 
### Arquitetura 
<img width="1500" height="500" alt="Diagrama_de_Arquitetura" src="https://github.com/user-attachments/assets/832d7928-e195-4316-b56c-3d7299ae9c64" />

## Arquitetura

O CodeCleaner segue uma arquitetura em camadas, com separação clara
entre apresentação e lógica de negócio:

- **Camada de apresentação (`app.py`)** — interface gráfica em Tkinter.
  Responsável por receber o arquivo do usuário, acionar o processamento
  e exibir o resultado. Não contém regra de negócio.

- **Camada de lógica (`cleaner.py`)** — núcleo da ferramenta. A função
  `procurar_chaves()` varre o conteúdo via regex contra um dicionário de
  padrões por serviço; em seguida o código substitui cada chave por
  `os.getenv("variavel")` e grava o arquivo limpo junto ao `.env`.

### Fluxograma
<img width="1500" height="500" alt="Fluxograma" src="https://github.com/user-attachments/assets/f07c1823-c236-45de-a526-8186b9b1615b" />
<br>
**Fluxo de dados:** o usuário seleciona um arquivo `.py` → `app.py`
repassa o conteúdo para `cleaner.py` → detecção → substituição →
geração do arquivo limpo + `.env` → `app.py` exibe o retorno. Todo o
processamento ocorre localmente; nenhum dado sai da máquina.

### Casos de uso
<img width="1500" height="500" alt="Diagrama_de_casos_de_uso" src="https://github.com/user-attachments/assets/3f5520ae-0780-4f0f-bc92-4399e9245b08" />
 
## Limitações
 
A ferramenta cumpre bem seu propósito, mas tem limites conhecidos:
 
- Funciona apenas com arquivos `.py`
- Detecta somente chaves dos serviços atualmente cadastrados:
  - OpenAI
  - Anthropic
  - AWS
  - Firebase
  - LangSmith
