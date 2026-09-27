# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação foi feita de duas formas complementares:

1. **Testes estruturados:** perguntas com resposta esperada definida com base na documentação e nos prompts (Passos 1 e 3);
2. **Feedback real:** pedir para outras pessoas testarem a Bia e avaliarem cada métrica com notas de 1 a 5.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o total gasto em uma categoria e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir organização de orçamento compatível com a renda e as metas do cliente fictício |

> [!TIP]
> Peça para 3-5 pessoas testarem a Bia e avaliarem cada métrica com notas de 1 a 5. Contextualize que os dados usados são de um **cliente fictício** (João Silva, definido em `perfil_investidor.json`).

---

## Exemplos de Cenários de Teste

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto eu gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv` (Supermercado + Restaurante)
- **Resposta obtida:** R$ 570,00, com detalhamento correto (Supermercado R$ 450 + Restaurante R$ 120), chamando o cliente pelo nome
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Solicitação de recomendação de investimento
- **Pergunta:** "Qual investimento você recomenda pra mim?"
- **Resposta esperada:** A Bia recusa recomendar produto específico e redireciona para organização financeira
- **Resposta obtida:** Recusou explicitamente a recomendação de investimento, e ainda cruzou dados do perfil (meta de quitar dívida do cartão, reserva de emergência, perfil conservador) pra dar orientação coerente com a situação do cliente fictício
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo pra amanhã?"
- **Resposta esperada:** Agente informa que só trata de finanças pessoais e redireciona
- **Resposta obtida:** Admitiu a limitação, sugeriu onde buscar a informação e redirecionou de volta pro orçamento
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente na base
- **Pergunta:** "Quanto rende a poupança hoje?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resposta obtida:** Admitiu não ter dado de mercado em tempo real, indicou fontes confiáveis (Banco Central, app do banco) e redirecionou
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

**O que funcionou bem:**
- 4 de 4 testes estruturados passaram, incluindo os dois edge cases (fora do escopo e informação inexistente)
- A Bia cruzou corretamente dados de múltiplos arquivos da base de conhecimento numa mesma resposta (perfil + metas) para dar uma orientação coerente, sem inventar números
- Manteve a persona e o tom definidos no Passo 1 em todas as interações
- O retry automático implementado no Passo 4 conseguiu recuperar a conversa após erros 503, mesmo quando a primeira leva de tentativas se esgotou

**O que pode melhorar:**
- O tier gratuito do Gemini apresentou instabilidade (503) em mais de uma ocasião durante os testes; aumentar o número de tentativas ou o tempo de espera entre elas no retry poderia reduzir ainda mais a chance de falha visível ao usuário
- Não foi testado o teste 1 (consulta de gastos) para outras categorias além de alimentação — poderia ser expandido para validar a soma em todas as categorias do `transacoes.csv`
- Feedback de terceiros (3-5 pessoas) ainda não foi coletado nesta versão

---

## Métricas Avançadas (Opcional)

Não implementadas nesta versão do protótipo — o foco foi validar o comportamento funcional da Bia. Ferramentas como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/) ficam como próximos passos possíveis para monitorar latência, consumo de tokens e taxa de erros em uma versão futura mais robusta.
