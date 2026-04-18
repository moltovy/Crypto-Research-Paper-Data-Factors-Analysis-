# Keyboard Shortcuts Guide

[← Back to Main](../README.md)

> Master the shortcuts to achieve "flow state" with Cursor.

---

## The Command Hierarchy

Understanding when to use each command is more important than memorizing shortcuts.

| Command | Mac | Windows/Linux | Scope | When to Use |
|---------|-----|---------------|-------|-------------|
| **Inline Edit** | `Cmd + K` | `Ctrl + K` | Single file | Quick fixes, rename, split function |
| **Chat** | `Cmd + L` | `Ctrl + L` | Conversational | Explain code, debug, explore |
| **Composer** | `Cmd + I` | `Ctrl + I` | Multi-file | Refactoring, new features |
| **Composer Full** | `Cmd + Shift + I` | `Ctrl + Shift + I` | Multi-file | Large refactors, review diffs |
| **Add to Context** | `Cmd + Shift + L` | `Ctrl + Shift + L` | Selection | Add selected code to chat |
| **Terminal AI** | `Cmd + K` (in terminal) | `Ctrl + K` | Shell | Generate shell commands |

---

## Inline Edit (Cmd + K)

### The "Surgical Knife"

```
Scope: Current selection or cursor position
Best for: Precise, localized changes
```

### Use Cases

```
✅ Fix a type error on this line
✅ Rename this variable throughout the file
✅ Split this function into two
✅ Add error handling here
✅ Convert this to async/await
```

### How to Use

1. Select code (or place cursor)
2. Press `Cmd + K`
3. Type instruction
4. Review and accept/reject

### Example

```typescript
// Select this line:
const result = fetchData();

// Cmd + K: "Add try-catch and error handling"
// Result:
try {
  const result = await fetchData();
} catch (error) {
  console.error('Failed to fetch data:', error);
  throw error;
}
```

---

## Chat (Cmd + L)

### The "Librarian"

```
Scope: Conversational, Q&A
Best for: Understanding, debugging, exploration
```

### Use Cases

```
✅ Explain how this function works
✅ Why is this test failing?
✅ What's the best pattern for X?
✅ Debug this error message
✅ Review this code for issues
```

### How to Use

1. Press `Cmd + L` to open chat
2. Add context with @ symbols
3. Ask your question
4. Optionally apply code with `Ctrl + Enter`

### Example

```
@Files auth.ts "Why is the session expiring early?"
```

---

## Composer (Cmd + I)

### The "General Manager"

```
Scope: Multi-file, project-wide
Best for: Features, refactoring, orchestration
```

### Use Cases

```
✅ Create a new API endpoint with tests
✅ Refactor from REST to GraphQL
✅ Add authentication to all routes
✅ Create a new React component with styles
✅ Migrate from JavaScript to TypeScript
```

### How to Use

1. Press `Cmd + I` to open Composer
2. Provide context with @ symbols
3. Describe the change
4. Review diffs across all files
5. Accept or reject per-file

### Normal vs Agent Mode

| Mode | Description | Risk |
|------|-------------|------|
| Normal | Proposes edits, you review | Safe |
| Agent | Executes autonomously, runs terminal | ⚠️ Careful |

### Example

```
@Folders src/api "Add rate limiting to all POST endpoints using express-rate-limit"
```

---

## Full Composer (Cmd + Shift + I)

### The "War Room"

```
Scope: Large-scale multi-file operations
Best for: Major refactors, full review mode
```

### Use Cases

```
✅ Massive codebase refactoring
✅ Reviewing complex multi-file changes
✅ When you need full diff visibility
✅ Architectural migrations
```

### Difference from Cmd + I

```
Cmd + I: Floating panel, inline workflow
Cmd + Shift + I: Full-screen, dedicated review mode
```

---

## Context Addition (Cmd + Shift + L)

### Quick Context Injection

```
Scope: Add selection to current chat
Best for: Building context incrementally
```

### How to Use

1. Select code in editor
2. Press `Cmd + Shift + L`
3. Selection added to chat context
4. Continue conversation with context

### Example

```
1. Select error stack trace
2. Cmd + Shift + L
3. "What's causing this error?"
```

---

## Terminal AI (Cmd + K in Terminal)

### Shell Command Generation

```
Scope: Terminal commands
Best for: Complex CLI operations
```

### Use Cases

```
✅ Find all files containing X
✅ Git operations
✅ Docker commands
✅ System administration
```

### Example

```
Press Cmd + K in terminal:
"Find all TypeScript files modified in the last week"

Output:
find . -name "*.ts" -mtime -7
```

---

## Tab Prediction

### The "Mind Reader"

```
Not a shortcut you press - it's always active.
Tab accepts the prediction.
```

### How It Works

```
1. Cursor predicts your next edit
2. Ghost text appears
3. Press Tab to accept
4. Or keep typing to ignore
```

### Pro Tips

```
✅ Trust Tab more - it's often right
✅ Accept and edit > type from scratch
✅ Tab predicts based on recent edits
✅ It understands multi-line patterns
```

---

## Navigation Shortcuts

| Action | Mac | Windows/Linux |
|--------|-----|---------------|
| Go to File | `Cmd + P` | `Ctrl + P` |
| Go to Symbol | `Cmd + Shift + O` | `Ctrl + Shift + O` |
| Go to Definition | `F12` | `F12` |
| Find References | `Shift + F12` | `Shift + F12` |
| Search in Files | `Cmd + Shift + F` | `Ctrl + Shift + F` |
| Toggle Sidebar | `Cmd + B` | `Ctrl + B` |

---

## Chat/Composer Shortcuts

| Action | Mac | Windows/Linux |
|--------|-----|---------------|
| New Chat | `Cmd + N` | `Ctrl + N` |
| Apply Code Block | `Ctrl + Enter` | `Ctrl + Enter` |
| Accept Change | `Cmd + Y` | `Ctrl + Y` |
| Reject Change | `Cmd + N` | `Ctrl + N` |
| Previous Checkpoint | Click in Composer | Click in Composer |

---

## Model Switching

```
In Chat or Composer:
- Click model name dropdown
- Select different model
- Or use @model-name prefix (if configured)
```

---

## The Decision Matrix

```
"Fix this line"
→ Cmd + K (Inline)

"Explain this code"
→ Cmd + L (Chat)

"Build this feature"
→ Cmd + I (Composer)

"Refactor entire module"
→ Cmd + Shift + I (Full Composer)

"Generate terminal command"
→ Cmd + K (in Terminal)
```

---

## Power User Tips

### 1. Don't Mix Scopes

```
❌ Using Cmd + K for multi-file changes
❌ Using Cmd + I for single-line fixes

✅ Use the right tool for the scope
```

### 2. Keyboard-First Workflow

```
1. Cmd + P → Open file
2. Cmd + Shift + O → Jump to symbol
3. Select code
4. Cmd + K → Make edit
5. Tab → Accept prediction
6. Cmd + S → Save
```

### 3. Build Context Before Acting

```
1. Cmd + Shift + L → Add relevant code
2. Cmd + Shift + L → Add more context
3. Then ask for the change
```

### 4. Fresh Start Rule

```
If stuck after ~20 messages:
Cmd + N → New chat with summary
```

---

## Quick Reference Card

```
Cmd + K     → Edit selection (surgical)
Cmd + L     → Chat (conversational)
Cmd + I     → Composer (multi-file)
Cmd + Shift + I → Full Composer (review)
Cmd + Shift + L → Add to context
Cmd + K (terminal) → Generate command
Tab         → Accept prediction
Cmd + Y     → Accept change
Cmd + N     → New chat / Reject change
```

---

[← Back to Main](../README.md)
