"""
Bia - Assistente de Organização Financeira Pessoal
Lab "Construa Seu Assistente Virtual Com Inteligência Artificial" (Santander/DIO)

Este arquivo faz 4 coisas, nesta ordem:
1. Configura a conexão com a API do Gemini (usando a chave guardada no .env)
2. Carrega os dados da pasta data/ (perfil do cliente, transações, glossário, etc.)
3. Monta o "system prompt" da Bia, juntando as regras de comportamento com os dados
4. Roda um loop de conversa no terminal, enviando cada mensagem pro Gemini
"""

import os
import json
import csv

from dotenv import load_dotenv
from google import genai
from google.genai import types


# ---------------------------------------------------------------------------
# PASSO 1: Configuração
# ---------------------------------------------------------------------------

# load_dotenv() lê o arquivo .env e "injeta" as variáveis dele no ambiente,
# como se você tivesse digitado no terminal. É assim que a chave chega até o
# programa sem precisar escrever ela direto no código.
load_dotenv()

# genai.Client() procura automaticamente por uma variável de ambiente chamada
# GEMINI_API_KEY. Se ela não existir, dá erro aqui mesmo -- por isso o
# load_dotenv() acima precisa rodar antes.
client = genai.Client()

# Nome do modelo que vamos usar. O Flash é rápido, leve e está dentro do
# tier gratuito do Gemini -- ideal pro seu caso.
MODEL_NAME = "gemini-3.8-flash"

# Caminho da pasta data/, calculado a partir da localização deste arquivo.
# Isso evita erro de "arquivo não encontrado" quando você roda o programa
# de uma pasta diferente.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "..", "data")


# ---------------------------------------------------------------------------
# PASSO 2: Carregar os dados da pasta data/
# ---------------------------------------------------------------------------

def carregar_json(nome_arquivo):
    """Abre um arquivo .json dentro de data/ e devolve o conteúdo como dict/list."""
    caminho = os.path.join(DATA_DIR, nome_arquivo)
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def carregar_csv(nome_arquivo):
    """Abre um arquivo .csv dentro de data/ e devolve uma lista de dicionários,
    um dicionário por linha (usando o cabeçalho como chaves)."""
    caminho = os.path.join(DATA_DIR, nome_arquivo)
    with open(caminho, "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)


# Carrega cada arquivo de dados uma única vez, quando o programa inicia.
perfil_cliente = carregar_json("perfil_investidor.json")
produtos_financeiros = carregar_json("produtos_financeiros.json")
glossario = carregar_json("glossario_financeiro.json")
transacoes = carregar_csv("transacoes.csv")
historico_atendimento = carregar_csv("historico_atendimento.csv")


# ---------------------------------------------------------------------------
# PASSO 3: Montar o system prompt (regras + dados)
# ---------------------------------------------------------------------------

REGRAS_DA_BIA = """
Você é a Bia, uma assistente financeira pessoal criada para ajudar pessoas no
início da vida financeira a organizar seu orçamento, entender seus gastos e
aprender conceitos financeiros básicos.

SEU OBJETIVO:
Ajudar a pessoa usuária a ter clareza sobre para onde vai o dinheiro, montar
um orçamento simples e tomar decisões financeiras mais conscientes -- sem
nunca fazer recomendações de investimento personalizadas.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos abaixo. Nunca invente
   números, valores ou informações financeiras que não estejam nos dados.
2. Se a pergunta exigir uma informação que você não tem, admita isso
   claramente e explique o que a pessoa pode fazer para descobrir.
3. Nunca recomende produtos de investimento específicos nem prometa
   rentabilidade. Você trabalha com organização financeira, não consultoria
   de investimentos.
4. Use linguagem simples e exemplos práticos -- evite jargão financeiro sem
   explicar.
5. Se a pergunta estiver fora do escopo de finanças pessoais, admita a
   limitação e redirecione com educação.
"""


def montar_contexto_dados():
    """Transforma todos os dados carregados em um texto único, que vai
    dentro do system prompt para a Bia poder consultar."""
    return f"""
DADOS DISPONÍVEIS PARA VOCÊ CONSULTAR:

Perfil da pessoa usuária:
{json.dumps(perfil_cliente, ensure_ascii=False, indent=2)}

Histórico de transações:
{json.dumps(transacoes, ensure_ascii=False, indent=2)}

Glossário de conceitos financeiros e categorias de gastos:
{json.dumps(glossario, ensure_ascii=False, indent=2)}

Estratégias e hábitos financeiros recomendados:
{json.dumps(produtos_financeiros, ensure_ascii=False, indent=2)}

Histórico de atendimentos anteriores:
{json.dumps(historico_atendimento, ensure_ascii=False, indent=2)}
"""


SYSTEM_PROMPT = REGRAS_DA_BIA + "\n" + montar_contexto_dados()


# ---------------------------------------------------------------------------
# PASSO 4: Loop de conversa no terminal
# ---------------------------------------------------------------------------

def main():
    # client.chats.create() abre uma "sessão de conversa": o Gemini vai se
    # lembrar das mensagens anteriores dentro dessa mesma execução do programa.
    chat = client.chats.create(
        model=MODEL_NAME,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
        ),
    )

    print("=" * 50)
    print("Oi! Eu sou a Bia, sua assistente de finanças pessoais.")
    print("Digite 'sair' a qualquer momento para encerrar.")
    print("=" * 50)

    while True:
        pergunta = input("\nVocê: ").strip()

        if pergunta.lower() in ("sair", "exit", "quit"):
            print("\nBia: Até mais! Cuide bem do seu dinheiro. 💰")
            break

        if not pergunta:
            continue

        try:
            resposta = chat.send_message(pergunta)
            print(f"\nBia: {resposta.text}")
        except Exception as erro:
            print(f"\n[Erro ao falar com a Bia: {erro}]")
            print("Verifique se sua GEMINI_API_KEY está correta no arquivo .env")


if __name__ == "__main__":
    main()
