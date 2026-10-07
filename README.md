# rn-pr-review-agent

🇬🇧 [English](#english) · 🇧🇷 [Português](#português)

---

## English

An AI agent that reviews pull requests of React Native / Expo apps.

It reads a PR diff through an MCP tool, grounds its findings in React Native and Expo documentation retrieved from a vector database (RAG), and drafts a review comment covering performance, re-renders, state management, accessibility and security. Any write action (such as posting the comment) requires explicit human approval.

> **Status:** early development. Not usable yet. Items below are planned unless marked ✅.

### Architecture (planned)

- **Orchestration:** LangGraph: stateful graph, checkpointing, human-in-the-loop interrupt
- **Multi-agent:** specialist sub-agents (performance, accessibility, security) coordinated by a supervisor
- **Tools:** custom MCP server built with FastMCP (read diff, list files, post comment)
- **Retrieval:** Qdrant with embedded React Native / Expo docs
- **Memory:** LangMem for per-team review preferences
- **Channels:** CLI, HTTP API and GitHub webhook
- **Security:** prompt-injection defenses, tool allowlist, least privilege, secrets outside code, attack tests
- **LLM:** provider-agnostic (Anthropic, OpenAI or Gemini) selected via environment variables
- **Delivery:** Docker Compose, GitHub Actions CI

### Tech stack

Python 3.12 · uv · LangChain · LangGraph · LangMem · MCP (Model Context Protocol) · Qdrant · Pydantic · pytest · ruff · Docker

### Implemented so far

- ✅ Project scaffold (uv, ruff, pytest, CI)

### Development

```bash
uv sync
cp .env.example .env   # fill in your API key
uv run pytest
uv run ruff check .
```

---

## Português

Um agente de IA que revisa pull requests de apps React Native / Expo.

Ele lê o diff do PR por meio de uma ferramenta MCP, fundamenta os apontamentos na documentação de React Native e Expo recuperada de um banco vetorial (RAG) e redige um comentário de revisão cobrindo performance, re-renders, gerenciamento de estado, acessibilidade e segurança. Qualquer ação de escrita (como postar o comentário) exige aprovação humana explícita.

> **Status:** em desenvolvimento inicial. Ainda não utilizável. Os itens abaixo são planejados, exceto os marcados com ✅.

### Arquitetura (planejada)

- **Orquestração:** LangGraph: grafo com estado, checkpoint e interrupção para aprovação humana
- **Multiagente:** subagentes especialistas (performance, acessibilidade, segurança) coordenados por um supervisor
- **Ferramentas:** servidor MCP próprio com FastMCP (ler diff, listar arquivos, postar comentário)
- **Recuperação:** Qdrant com a documentação de React Native / Expo
- **Memória:** LangMem para preferências de revisão por time
- **Canais:** CLI, API HTTP e webhook do GitHub
- **Segurança:** defesa contra prompt injection, allowlist de ferramentas, menor privilégio, segredos fora do código, testes de ataque
- **LLM:** independente de provedor (Anthropic, OpenAI ou Gemini) via variáveis de ambiente
- **Entrega:** Docker Compose, CI com GitHub Actions

### Stack

Python 3.12 · uv · LangChain · LangGraph · LangMem · MCP (Model Context Protocol) · Qdrant · Pydantic · pytest · ruff · Docker

### Já implementado

- ✅ Esqueleto do projeto (uv, ruff, pytest, CI)

### Desenvolvimento

```bash
uv sync
cp .env.example .env   # preencha sua chave de API
uv run pytest
uv run ruff check .
```
