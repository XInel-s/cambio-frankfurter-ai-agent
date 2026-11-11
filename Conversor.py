import os
import requests
from google import genai
from google.genai import types

'''client = genai.Client(api_key="GEMINI_API_KEY")'''
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def consult_cotacao(orig_coin: str, dest_coin: str, val: float) -> dict:
    ''' Consulta a taxa de câmbio atual usando a API frankfurter e calcula a conversão.

        - orig_coin: codigo base de origem como o 'USD'.
        - dest_coin: codigo base de destino como o 'BRL'.
        - val: quantidade a ser convertida.
    '''
    try:
        url = f"https://api.frankfurter.dev/v2/rates?base={orig_coin.lower()}&quotes={dest_coin.lower()}"
        resposta = requests.get(url, timeout=10).json()

        if isinstance(resposta, list) and len(resposta) > 0:
            xat = resposta[0]["rate"]
            dat = resposta[0]["date"]
            convertido = val * xat

            return {
                "sucesso": True,
                "resultado": f"{val} {orig_coin.upper()} equivalem a {convertido:.2f} {dest_coin.upper()} em {dat}."
            }
        else:
            return {"sucesso": False, "erro": "resposta invalida da API"}

    except Exception as erro:
        return {"erro": str(erro)}

chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config=types.GenerateContentConfig(
        tools=[consult_cotacao],
        temperature=0.0
    )
)

print("digite a cotação que deseja converter (ou 'sair' para encerrar),\n")

while True:
    try:
        pergunta = input("> ")

        if pergunta.lower() in ["sair", "tchau", "exit", "quit"]:
            print("bye, bye")
            break

        if not pergunta.strip():
            continue

        resposta = chat.send_message(pergunta)
        print(f"[Agente]: {resposta.text}\n")

    except (KeyboardInterrupt, EOFError):
        print("bye, bye")
        break
