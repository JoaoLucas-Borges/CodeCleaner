<img width="1500" height="500" alt="Code Cleaner" src="https://github.com/user-attachments/assets/62ac6dfa-a16c-4ae1-a0a0-99a28715e6f7" />

<br>
<br>
TO DO documentação:<br>
Badges? (Python version, license, etc.)<br>
Descrição do problema<br>
Arquitetura + diagramas inline (você coloca as imagens direto no markdown com ![alt](caminho))<br>
Requisitos e instalação<br>
Como usar<br>
Bibliotecas<br>
<br>

# O problema:
Atualmente a produção moderna de software utiliza diversos serviços de terceiros, como aplicações em nuvem, bancos de dados, LLMs e outros. Para realizar a conexão entre esses serviços é comum o uso das chamadas API Keys (chaves de acesso) — um sistema eficiente, porém com um risco relevante: as API Keys são geradas e associadas a uma conta, pois os serviços de terceiros utilizam modelos de cobrança baseados no consumo dessas chaves. O problema está exatamente aí — caso os valores dessas API Keys fiquem expostos, podem ser utilizados por agentes maliciosos para consumir esses serviços sem custo algum, sendo que quem arca com as cobranças é o titular da chave. Por mais cauteloso seja o programador é comum que haja algum commit acidental em repositórios públicos no GitHub.
# A solução:
Com base nisso surgiu a ideia do Code Cleaner: uma ferramenta que lê códigos localmente e, caso encontre API Keys expostas, as trata da maneira correta — salva os valores no arquivo .env e substitui as ocorrências no código fornecido por os.getenv("variavel"), retornando o arquivo limpo e o .env devidamente preenchido.

## Diagrama de Arquitetura
<img width="1500" height="500" alt="Diagrama_de_Arquitetura" src="https://github.com/user-attachments/assets/832d7928-e195-4316-b56c-3d7299ae9c64" />

<br>

## Fluxograma
<img width="1500" height="500" alt="Fluxograma" src="https://github.com/user-attachments/assets/f07c1823-c236-45de-a526-8186b9b1615b" />

<br>

## Diagrama de casos de uso
<img width="1500" height="500" alt="Diagrama_de_casos_de_uso" src="https://github.com/user-attachments/assets/3f5520ae-0780-4f0f-bc92-4399e9245b08" />



