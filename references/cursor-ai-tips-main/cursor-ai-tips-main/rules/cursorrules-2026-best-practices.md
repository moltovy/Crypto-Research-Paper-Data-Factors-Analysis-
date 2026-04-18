# 📏 2026 Best Practices for `.cursorrules`

**Updated: March 12, 2026**

With the release of Cursor 2.6 and the rise of **Agentic Engineering** (always-on agents, Automations, Looped workflows), your `.cursorrules` need a major update. Models are no longer just assistants — they are autonomous workers that need strict boundaries.

## 🧠 Meta-Rules (The "Vibe" Shift)

Old rules focused on "don't be lazy". New models aren't lazy, but they can be **over-verbose** or **insecure**.

### 1. The "Concise Architect" Rule
Prevents Opus 4.5 from explaining every single import.

```markdown
# General Behavior
- Be concise. Do not explain standard code patterns unless asked.
- Focus on the "Unique Value" of the change.
- If a solution is effectively identical to the existing code, say "No changes needed".
```

### 2. The "Security First" Rule (Critical for Agents)
Agents now run recursively. You must bound them.

```markdown
# Agent Boundaries
- NEVER commit code without user review strings.
- NEVER delete config files (.env, package.json) without explicit confirmation.
- If you find a security vulnerability, STOP and report it immediately.
```

---

## 🛠️ Fixes for Common 2025 Bugs

### The "Zombie Revert" Fix
Cursor 2.2/2.3 sometimes "hangs" on apply. Add this context to help the model avoid complex diffs.

```markdown
# Diffs & Applies
- When editing large files (>500 lines), prefer `SEARCH/REPLACE` blocks over full file rewrites.
- If you are unsure where a block belongs, ask for the surrounding context first.
```

### Windows/WSL Terminal Fix
If you are on Windows, force the legacy terminal tool to avoid PID -1 errors.

```markdown
# Environment
- Use "Legacy Terminal Tool" behavior: simple command execution, no complex TTY manipulation.
```

---

## ⚡ Framework-Specific Snippets (2026 Editions)

### Next.js 15+ (App Router Strict Mode)

```markdown
# Next.js
- Default to `server components` unless `useState` or `useEffect` is strictly required.
- Use `await params` in dynamic routes (Next.js 15 change).
- Prefer `typed-routes` for all navigation.
```

### Python / FastAPI (Async First)

```markdown
# Python
- All IO-bound operations MUST be `async def`.
- Use Pydantic V2 `model_validate` patterns.
- Type hints are mandatory (Python 3.12+ syntax).
```

---

## 🤖 2026 Agentic Engineering Standards (NEW — March 2026)

With Cursor Automations and always-on agents, these rules prevent autonomous agents from causing damage:

### 3. The "Anti-Hallucination" Rule
Prevents agents from importing non-existent packages or using outdated APIs.

```markdown
# Dependency Verification
- If you are about to import an npm package, FIRST run `npm list <package>` via the terminal
  agent and verify it is installed in the project with 100% certainty.
- If using a Python package, run `pip show <package>` before importing.
- NEVER assume a package exists based on training data — always verify at runtime.
- When using a framework API (React, Next.js, etc.), use Context7 MCP to fetch current docs.
```

### 4. The "Interface Freeze" Rule
Prevents agents from writing sprawling implementations without approval.

```markdown
# Interface-First Development
- When adding a new feature, NEVER write implementation directly.
- First define types/interfaces in a separate block.
- Present the interface for user approval.
- Only after explicit approval, write the implementation.
- This prevents wasted compute on wrong abstractions.
```

### 5. The "No Placeholder" Rule (Zero Placeholder Policy)
Prevents agents from leaving incomplete code.

```markdown
# Zero Placeholders
- NEVER use placeholder comments like "// TODO: implement this" or "// rest of the code".
- Every function must be fully implemented or not included at all.
- If you cannot complete a function, explain WHY and ask for guidance.
- Autonomous agents (Automations) cannot ask follow-ups — they must complete or abort.
```

### 6. The "Defensive Commit" Rule
Prevents data loss during long-running agent sessions.

```markdown
# Defensive Commits
- Before starting any multi-file refactoring, create a git checkpoint:
  `git add -A && git commit -m "checkpoint: before <task>"`
- After every successful test run, commit immediately.
- Never modify more than 3 files without an intermediate commit.
```
