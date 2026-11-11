### Agente de Conversão de Moedas com IA

Um agente conversacional em Python que utiliza a API do [Frankfurter](https://frankfurter.dev/pt/) para consultar taxas de câmbio e responder perguntas em linguagem natural, utilizando a SDK oficial do google genAI (`google-genai`) com Function Calling

### Como Executar

### - Instalar as dependências
as dependencias são Python e instale os pacotes necessários:
```bash
pip install google-genai requests
```
#### - no terminal fish
```bash
set -x GEMINI_API_KEY "sua_API_aqui" && python3 Conversor.py
```
#### - no terminal bash
```bash
export GEMINI_API_KEY="sua_API_aqui" && python3 Conversor.py 
```
