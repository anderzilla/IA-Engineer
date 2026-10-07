# 12 · Preparação para entrevista

> **Extra · Tempo:** 1 sessão por bloco · **Pré-requisitos:** lições 01–11

## 🎯 Objetivo
Responder perguntas técnicas sobre agentes de forma clara, curta e honesta, em português e em inglês simples (nível B2).

## 🗺️ Mapa

```mermaid
flowchart LR
  A[Resposta curta<br/>20 segundos] --> B[Exemplo do seu projeto<br/>30 segundos]
  B --> C[Trade-off ou limite<br/>10 segundos]
```
Formato para toda resposta: **definição → exemplo seu → limite**.

## 📖 Perguntas e respostas-modelo
Abra cada uma **depois** de tentar responder em voz alta.

<details><summary>1. O que é um agente de IA, diferente de um chatbot?</summary>

**PT:** Um agente usa um LLM para decidir passos e chamar ferramentas em laço até cumprir um objetivo. Um chatbot só responde mensagens. No meu projeto, o agente lê o diff, busca documentação e propõe um comentário.
**EN:** An agent uses an LLM to decide steps and call tools in a loop until it reaches a goal. A chatbot only replies to messages.
**Limite:** mais autonomia = mais risco, por isso aprovação humana.
</details>

<details><summary>2. Por que LangGraph em vez de um laço simples?</summary>

**PT:** Para ter estado explícito, checkpoint, pausa/retomada e testes por nó. Usei para aprovação humana antes de escrever no GitHub.
**EN:** For explicit state, checkpoints, pause/resume and per-node tests. I used it for human approval before writing to GitHub.
</details>

<details><summary>3. Como funciona o human-in-the-loop no seu projeto?</summary>

**PT:** O nó de aprovação chama <code>interrupt</code>. O grafo salva o estado e devolve o pedido. Quando o humano decide, retomo a mesma thread com <code>Command(resume=...)</code>. A escrita só acontece depois.
**Limite:** o nó reinicia na retomada, então nenhum efeito colateral antes do interrupt.
</details>

<details><summary>4. O que é MCP e por que usar?</summary>

**PT:** Protocolo aberto que padroniza como modelos acessam ferramentas e dados. Escrevi um servidor uma vez e usei no meu agente, no Claude Code e no Cursor.
**EN:** An open protocol that standardizes how models access tools and data. I wrote one server and used it from my agent, Claude Code and Cursor.
</details>

<details><summary>5. MCP vs A2A?</summary>

MCP liga modelo a ferramentas/dados. A2A liga agente a agente entre serviços.
</details>

<details><summary>6. Como funciona RAG e como você mediu a qualidade?</summary>

**PT:** Quebro documentos em pedaços, gero embeddings, guardo no Qdrant, busco os mais próximos da pergunta e coloco no prompt. Medi com hit rate num conjunto de perguntas com documento esperado, e comparei tamanhos de chunk.
**Limite:** conjunto pequeno; os números valem para aquele conjunto.
</details>

<details><summary>7. O que é prompt injection e como você mitigou?</summary>

**PT:** Instruções escondidas em conteúdo que o agente lê. Mitiguei em camadas: dado delimitado, allowlist de tools, token de leitura, escrita só com aprovação, validação do comentário e testes com diffs maliciosos.
**Limite:** nenhuma defesa de prompt é completa; as estruturais importam mais.
</details>

<details><summary>8. Como você testa algo não determinístico?</summary>

**PT:** Pirâmide: unitários sem LLM, integração com modelo falso, evals com LLM real e conjunto fixo, e testes de segurança verificando propriedades (nenhuma tool de escrita chamada).
</details>

<details><summary>9. Quando você NÃO usaria multiagente?</summary>

**PT:** Quando um prompt único resolve com qualidade parecida. Multiagente multiplica custo e latência. Eu mediria antes de adotar.
</details>

<details><summary>10. Memória de curto vs longo prazo?</summary>

Curto: estado e checkpoint da thread. Longo: store com namespace, entre execuções. Cuidado com envenenamento e isolamento entre times.
</details>

<details><summary>11. Como trocar de provedor de LLM?</summary>

Pela variável de ambiente <code>LLM_PROVIDER</code> e <code>LLM_MODEL</code>, usando <code>init_chat_model</code>. O resto do código não muda. Limite: recursos como tool calling e saída estruturada variam em qualidade entre modelos, então reavalio.
</details>

<details><summary>12. Conte um problema que você enfrentou e como resolveu.</summary>

Prepare **o seu** (use os reais): por exemplo o reducer que duplicava itens, ou o efeito colateral antes do interrupt. Formato: situação → causa → correção → o que aprendi.
</details>

## 🗣️ Perguntas para fazer ao entrevistador
- Como os agentes são avaliados hoje (evals, métricas)?
- Como lidam com segurança e aprovação humana em ações de escrita?
- Qual a stack de observabilidade (traces, custo por execução)?
- Como é o fluxo da squad (revisão de PR, deploy)?

## ✅ Checagem
<details><summary>Qual o formato de toda resposta?</summary>

Definição, exemplo do seu projeto e limite ou trade-off.
</details>

## 🔨 Tarefa
Grave-se respondendo 5 perguntas (1 minuto cada). Ouça e corte o que for desnecessário. Repita em inglês simples.
