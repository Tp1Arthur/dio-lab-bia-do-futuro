<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=CC092F&height=180&section=header&text=Bia&fontSize=70&fontColor=FFFFFF&animation=fadeIn&fontAlignY=40" width="100%"/>

<h3 align="center">Assistente de Organização Financeira Pessoal</h3>
<p align="center">Bootcamp Bradesco · GenAI, Dados & Cyber — em parceria com a DIO</p>

<br/>

<img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=600&size=20&pause=1000&color=CC092F&center=true&vCenter=true&width=600&lines=Organizacao+financeira+sem+complicacao;Zero+alucinacoes%2C+zero+jargao;Construido+com+IA+Generativa+e+Python" alt="Typing SVG" />

<br/><br/>

![Status](https://img.shields.io/badge/status-concluido-CC092F?style=for-the-badge&labelColor=1a1a1a)
![Python](https://img.shields.io/badge/python-3.10+-CC092F?style=for-the-badge&logo=python&logoColor=white&labelColor=1a1a1a)
![Gemini](https://img.shields.io/badge/IA-Google%20Gemini-CC092F?style=for-the-badge&logo=googlegemini&logoColor=white&labelColor=1a1a1a)
![License](https://img.shields.io/badge/licenca-MIT-CC092F?style=for-the-badge&labelColor=1a1a1a)

</div>

<br/>

<div align="center">

*Um assistente virtual que ajuda pessoas no início da vida financeira a organizar seus gastos, entender conceitos básicos e montar um orçamento — sem inventar informações e sem recomendar investimentos.*

</div>

<br/>

<p align="center">
  <a href="#-sobre-o-projeto">Sobre</a> •
  <a href="#-o-problema">Problema</a> •
  <a href="#-a-solução">Solução</a> •
  <a href="#-como-rodar">Como Rodar</a> •
  <a href="#-documentação-completa">Docs</a> •
  <a href="#-avaliação-e-testes">Testes</a> •
  <a href="#-autor">Autor</a>
</p>

---

## 🎯 Sobre o Projeto

Este repositório contém o desenvolvimento completo da **Bia**, um agente de IA generativa construído como desafio do Bootcamp Bradesco - GenAI, Dados & Cyber (DIO). O projeto percorre as 6 etapas de construção de um assistente responsável: documentação, base de conhecimento, engenharia de prompt, aplicação funcional, avaliação com métricas e pitch final.

<br/>

<table align="center">
<tr>
<td align="center" width="200">

### 💡
**O Problema**

Vida financeira desorganizada por falta de orientação acessível

</td>
<td align="center" width="200">

### 🤖
**A Solução**

Assistente que educa, categoriza e organiza sem inventar dados

</td>
<td align="center" width="200">

### 🔒
**O Diferencial**

Zero alucinação, zero recomendação de investimento

</td>
</tr>
</table>

<br/>

## 💡 O Problema

Muita gente começa a vida financeira sem nenhuma base: não sabe pra onde o dinheiro está indo, nunca montou um orçamento e não tem a quem perguntar sobre conceitos básicos como reserva de emergência ou juros compostos.

## ✅ A Solução

A Bia conversa em linguagem simples, ajuda a organizar e categorizar gastos, e ensina conceitos financeiros — sempre baseada em uma base de conhecimento real, nunca inventando dados, e sem fazer recomendações de investimento (fora do seu escopo por design).

---

## 📁 Estrutura do Repositório

<details>
<summary><b>📂 Clique para expandir a árvore de arquivos</b></summary>

```
dio-lab-bia-do-futuro/
│
├── 📄 README.md
│
├── 📁 data/                          # Base de conhecimento da Bia
│   ├── perfil_investidor.json        # Perfil do cliente fictício
│   ├── produtos_financeiros.json     # Estratégias/hábitos financeiros
│   ├── transacoes.csv                # Histórico de transações
│   ├── historico_atendimento.csv     # Histórico de atendimentos
│   └── glossario_financeiro.json     # Conceitos e categorias de gastos
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
│
├── 📁 src/
│   └── app.py                        # Aplicação funcional da Bia
│
├── requirements.txt
└── .env.example
```

</details>

<br/>

## 🛠️ Tecnologias Utilizadas

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-CC092F?style=for-the-badge&logo=python&logoColor=white&labelColor=1a1a1a)
![Gemini API](https://img.shields.io/badge/Google%20Gemini%20API-CC092F?style=for-the-badge&logo=googlegemini&logoColor=white&labelColor=1a1a1a)
![GitHub Codespaces](https://img.shields.io/badge/GitHub%20Codespaces-CC092F?style=for-the-badge&logo=github&logoColor=white&labelColor=1a1a1a)

</div>

| Tecnologia | Papel no projeto |
|---|---|
| 🐍 **Python** | Linguagem da aplicação |
| ✨ **google-genai** | SDK oficial para integração com o Gemini |
| 🔐 **python-dotenv** | Gerenciamento seguro de variáveis de ambiente |
| ☁️ **GitHub Codespaces** | Ambiente de execução na nuvem, sem custo |

---

## 🚀 Como Rodar

> 💡 Recomendado: rodar via **GitHub Codespaces** — nenhuma instalação local necessária.

<details open>
<summary><b>Passo a passo</b></summary>

**1.** Clique em `Code` → `Codespaces` → `Create codespace on main`

**2.** No terminal do Codespace, instale as dependências:
```bash
pip install -r requirements.txt
```

**3.** Configure sua chave gratuita da [Google Gemini API](https://aistudio.google.com/) como **Codespaces secret** (`GEMINI_API_KEY`) em `github.com/settings/codespaces`

**4.** Rode a aplicação:
```bash
python src/app.py
```

**5.** Converse com a Bia no terminal — digite `sair` para encerrar

</details>

---

## 📚 Documentação Completa

<div align="center">

| Etapa | Descrição |
|:---:|---|
| 📄 [**Documentação do Agente**](./docs/01-documentacao-agente.md) | Caso de uso, persona e arquitetura |
| 📄 [**Base de Conhecimento**](./docs/02-base-conhecimento.md) | Estratégia de dados |
| 📄 [**Prompts**](./docs/03-prompts.md) | System prompt e edge cases |
| 📄 [**Avaliação e Métricas**](./docs/04-metricas.md) | Testes estruturados e resultados |
| 📄 [**Pitch**](./docs/05-pitch.md) | Roteiro de apresentação |

</div>

---

## 🧪 Avaliação e Testes

<div align="center">

| Teste | Resultado |
|---|:---:|
| Consulta de gastos por categoria | ✅ |
| Recusa de recomendação de investimento | ✅ |
| Pergunta fora do escopo | ✅ |
| Informação inexistente na base | ✅ |

</div>

Detalhes completos em [`docs/04-metricas.md`](./docs/04-metricas.md).

---

## 👤 Autor

<div align="center">

**Arthur Ricardo**

[![GitHub](https://img.shields.io/badge/GitHub-Tp1Arthur-CC092F?style=for-the-badge&logo=github&logoColor=white&labelColor=1a1a1a)](https://github.com/Tp1Arthur)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-arthur--ricardo--silva-CC092F?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=1a1a1a)](https://linkedin.com/in/arthur-ricardo-silva)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=CC092F&height=100&section=footer" width="100%"/>
