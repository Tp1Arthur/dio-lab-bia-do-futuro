# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `conceitos_financeiros.json` | JSON | Explicar termos financeiros básicos (juros, reserva de emergência, orçamento, etc.) quando a pessoa perguntar |
| `categorias_gastos.json` | JSON | Ajudar a classificar e organizar os gastos informados pela pessoa usuária |
| `regras_orcamento.json` | JSON | Sugerir formas de dividir a renda (ex: regra 50/30/20) conforme a situação relatada |
| `transacoes_exemplo.csv` | CSV | Dataset fictício de transações, usado como exemplo prático de categorização e análise de gastos |

> [!TIP]
> Não precisei usar datasets do Hugging Face — o escopo é simples o suficiente pra rodar com dados próprios, curados manualmente pro contexto do desafio.

---

## Adaptações nos Dados

Não usei os arquivos de exemplo do repositório de referência (`historico_atendimento.csv`, `perfil_investidor.json`, `produtos_financeiros.json`), porque o tema da Bia é organização financeira pessoal, não recomendação de investimentos. Criei uma base de conhecimento própria, com foco em conceitos, categorias de gastos e regras de orçamento — mais compatível com o público-alvo (iniciantes na vida financeira).

---

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos JSON e CSV são carregados no início da execução do programa e transformados em texto estruturado, que é incluído no *system prompt* enviado à IA junto com as instruções de comportamento da Bia.

### Como os dados são usados no prompt?
Os dados vão diretamente no *system prompt*, como contexto fixo (a base é pequena o suficiente para caber inteira). A Bia é instruída a responder apenas com base nesse conteúdo e a admitir quando não tem a informação, em vez de consultar os dados dinamicamente durante a conversa.

---

## Exemplo de Contexto Montado

```
Conceitos disponíveis:
- Reserva de emergência: valor guardado para imprevistos, recomendado entre 3 e 6 meses de gastos essenciais.
- Regra 50/30/20: 50% da renda para necessidades, 30% para desejos, 20% para poupança/investimento.

Categorias de gastos:
- Moradia, Alimentação, Transporte, Lazer, Saúde, Educação, Outros

Exemplo de transações da pessoa usuária:
- 01/11: Supermercado - R$ 450 (Alimentação)
- 03/11: Streaming - R$ 55 (Lazer)
- 05/11: Uber - R$ 32 (Transporte)
```
