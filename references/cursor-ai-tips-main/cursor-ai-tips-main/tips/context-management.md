# Context Management Guide

[← Back to Main](../README.md)

> The AI is only as good as the context you provide.

---

## Overview

Effective context management is the difference between a helpful AI and a hallucinating one. This guide covers all the ways to provide context to Cursor.

---

## @ Symbol Reference

### Core Symbols

| Symbol | What It Does | Best For |
|--------|--------------|----------|
| `@Files` | Injects full file content | Active editing, specific references |
| `@Folders` | File tree + file summaries | Architecture questions |
| `@Codebase` | Semantic RAG search | "Where is X used?" queries |
| `@Docs` | External documentation | Third-party API usage |
| `@Git` | Git history and diffs | Commit context, blame |
| `@Web` | Live web search | Current information |

### Usage Examples

```
@Files auth.ts → "Refactor this authentication logic"
@Folders src/components → "What's the component structure?"
@Codebase "user validation" → "Find all user validation code"
@Docs prisma → "How do I create a many-to-many relation?"
@Git → "What changed in the last commit?"
```

---

## @Codebase Deep Dive

### How It Works

```
1. Query converted to vector embedding
2. Similarity search against indexed codebase
3. Top-K relevant snippets retrieved
4. Injected into context window
```

### Limitations

```
⚠️ @Codebase is PROBABILISTIC

If you call your function "Login" but the code says "SessionCreation",
RAG may fail to find it.

The search is semantic, not lexical.
```

### When @Codebase Fails

```
Problem: "Find the auth middleware"
Reality: Code is named "sessionValidator.ts"

Solution: Use explicit @Files for critical tasks
```

### Best Practices

```
✅ Use specific, descriptive queries
✅ Match terminology in your codebase
✅ Combine with @Files for precision
✅ Re-index after major refactors
```

---

## @Docs Integration

### Adding Documentation

1. Open Command Palette
2. "Cursor: Add Documentation"
3. Enter URL or select from suggestions

### Popular Docs to Add

```
- React: https://react.dev
- Next.js: https://nextjs.org/docs
- Prisma: https://www.prisma.io/docs
- Tailwind: https://tailwindcss.com/docs
- Supabase: https://supabase.com/docs
```

### Why @Docs Matters

```
Without @Docs:
AI uses training data → outdated API suggestions

With @Docs:
AI uses live documentation → accurate, current code
```

### Example

```
Query: "@Docs nextjs How do I use the new App Router?"
Result: AI references Next.js 14+ documentation, not outdated Pages Router
```

---

## @Files vs @Codebase

| Aspect | @Files | @Codebase |
|--------|--------|-----------|
| **Precision** | Exact file content | Probabilistic search |
| **Token Usage** | High (full file) | Lower (snippets) |
| **Best For** | Known files | Discovery |
| **Reliability** | 100% accurate | May miss relevant code |

### Decision Matrix

```
"Edit this specific file" → @Files
"Find where this is used" → @Codebase
"Refactor across codebase" → @Codebase + @Files for critical ones
```

---

## Notepads (Persistent Context)

### What They Are

Notepads are persistent text blocks that survive across chat sessions.

### Use Cases

```
1. Project Requirements (PRD)
2. Architecture decisions
3. Coding conventions
4. Prompt templates
5. Task specifications
```

### Creating a Notepad

1. Open Command Palette
2. "Cursor: Create Notepad"
3. Name it descriptively (e.g., `current_task_spec`)

### Referencing Notepads

```
@current_task_spec "Implement the next feature from the spec"
```

### Example: Task Spec Notepad

```markdown
# Current Sprint: Authentication

## Requirements
- OAuth2 with Google and GitHub
- Session management with Redis
- Rate limiting on login endpoint

## Constraints
- No external auth libraries (build from scratch)
- Must support SSO for enterprise

## Tech Stack
- Next.js 14 App Router
- Prisma ORM
- Redis for sessions
```

---

## Context Window Management

### The Token Budget

```
Claude 3.5 Sonnet: ~200K tokens
GPT-4o: ~128K tokens

But effective context is smaller:
- First 40K tokens: Highest attention
- Middle: "Lost in the middle" problem
- Last 10K: Secondary attention peak
```

### Strategies

```
1. Front-load important context
   - Put critical files first
   - State constraints early

2. Minimize noise
   - Don't add entire @Codebase for simple tasks
   - Use specific @Files over broad searches

3. Refresh context
   - Start new chat when context gets polluted
   - Summarize before continuing complex tasks
```

---

## The "Context Pollution" Problem

### Symptoms

```
- AI starts ignoring recent instructions
- Hallucinations increase
- Model suggests already-rejected solutions
```

### Causes

```
- Too many messages in one conversation
- Conflicting instructions accumulated
- @Codebase pulling in irrelevant code
```

### Solutions

```
✅ Start fresh chat after ~20 messages
✅ Summarize state before continuing
✅ Use specific @Files instead of broad @Codebase
✅ Create new Composer for new tasks
```

---

## Advanced: Context Layering

### The Hierarchy

```
Layer 1: .cursorrules / .mdc files (always present)
Layer 2: Notepads (persistent, user-referenced)
Layer 3: @Docs (external knowledge)
Layer 4: @Files / @Codebase (project-specific)
Layer 5: Current conversation (immediate context)
```

### Optimization

```
Static context (Layer 1-2):
- Coding style, architecture decisions
- Should be in .mdc or Notepads

Dynamic context (Layer 3-5):
- Specific to current task
- Add as needed, remove when done
```

---

## Troubleshooting Context Issues

### Problem: AI Ignores Recent Files

```
Cause: Index out of sync

Fix:
1. Cursor Settings → "Reindex Codebase"
2. Or: Remove and re-add project folder
```

### Problem: AI Hallucinates Functions

```
Cause: @Codebase returned wrong matches

Fix:
1. Use explicit @Files for the correct file
2. State the actual function name in prompt
```

### Problem: AI Uses Outdated Patterns

```
Cause: Training data overriding @Docs

Fix:
1. Add explicit constraint in prompt
2. Reference specific doc section
3. Add rule to .cursorrules
```

---

## Best Practices Summary

### Do

```
✅ Use @Files for known, critical files
✅ Add documentation via @Docs before coding
✅ Create Notepads for persistent requirements
✅ Start fresh chats when context gets polluted
✅ Be specific with @Codebase queries
```

### Don't

```
❌ Add @Codebase for simple, single-file tasks
❌ Let conversations grow beyond ~20 messages
❌ Expect @Codebase to find renamed/refactored code
❌ Ignore the "Lost in the middle" problem
❌ Mix multiple unrelated tasks in one chat
```

---

## Quick Reference

```
Simple edit        → @Files specific.ts
Find usage         → @Codebase "function name"
Learn API          → @Docs library-name
Architecture       → @Folders src/
History context    → @Git
Current info       → @Web
Persistent specs   → @Notepad name
```

---

[← Back to Main](../README.md)
