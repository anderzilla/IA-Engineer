# rn-pr-review-agent

An AI agent that reviews pull requests of React Native / Expo apps.

It reads a PR diff through an MCP tool, grounds its findings in React Native and Expo
documentation retrieved from a vector database (RAG), and drafts a review comment covering
performance, re-renders, state management, accessibility and security. Any write action
(such as posting the comment) requires explicit human approval.

> **Status:** early development. Not usable yet.

## Planned architecture

- **Orchestration:** LangGraph (stateful graph, checkpointing, human-in-the-loop interrupt)
- **Tools:** custom MCP server built with FastMCP (read diff, list files, post comment)
- **Retrieval:** Qdrant with embedded React Native / Expo docs
- **Memory:** LangMem for per-reviewer preferences
- **LLM:** provider-agnostic (Anthropic, OpenAI or Gemini), selected via environment variables

## Development

```bash
uv sync
cp .env.example .env   # fill in your API key
uv run pytest
uv run ruff check .
```
