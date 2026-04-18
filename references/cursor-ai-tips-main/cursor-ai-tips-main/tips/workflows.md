# Development Workflows Guide

[← Back to Main](../README.md)

> Proven workflows for different development scenarios.

---

## Research-First Protocol

The most rigorous workflow for complex changes.

### The 5 Phases

```
1. DISCOVERY → Understand the current state
2. PLAN      → Create implementation plan
3. CRITIQUE  → Review and challenge the plan
4. EXECUTE   → Implement with Composer
5. AUDIT     → Review changes carefully
```

### Phase 1: Discovery

```
Goal: Map the current state without making changes

Prompt:
"@Codebase Map all usages of the UserService class.
List files, line numbers, and how it's used.
DO NOT suggest changes yet."
```

### Phase 2: Plan

```
Goal: Create a detailed implementation plan

Prompt:
"Based on the UserService analysis:
1. Create a refactoring plan
2. List all affected files
3. Identify potential regressions
4. Propose a testing strategy

Output to plan.md - don't code yet."
```

### Phase 3: Critique

```
Goal: Challenge assumptions before coding

Switch to a different model (optional):
"Review plan.md for:
- Edge cases we might have missed
- Performance implications
- Security concerns
- Simpler alternatives"
```

### Phase 4: Execute

```
Goal: Implement step by step

Open Composer (Cmd + I):
"Implement Step 1 of plan.md.
@Files plan.md @Files UserService.ts

After implementation:
- Run existing tests
- Wait for my approval before Step 2"
```

### Phase 5: Audit

```
Goal: Verify changes before commit

Commands:
git diff --staged  # Review all changes
npm test           # Run tests
npm run lint       # Check style

Then: Line-by-line review of AI changes
```

---

## TDD with AI

Test-Driven Development enhanced by AI.

### The Pattern

```
1. Write test → AI helps with test structure
2. Review test → Human validates logic
3. Implement → AI writes code to pass test
4. Refactor → AI improves while keeping tests green
```

### Step 1: Generate Test First

```
Prompt:
"Write a Vitest test for a compound interest calculator.

Test cases:
- Principal: $1000, Rate: 5%, Time: 10 years, Monthly compounding
- Edge case: Zero principal
- Edge case: Negative rate

Include edge cases. Don't write the implementation."
```

### Step 2: Review Test Logic

```
Human reviews:
✅ Are the expected values correct?
✅ Are edge cases reasonable?
✅ Is the API design sensible?
```

### Step 3: Implement to Pass

```
Prompt:
"@Files calculator.test.ts
Write the implementation to pass all these tests.
Export from calculator.ts"
```

### Step 4: Refactor

```
Prompt:
"Refactor the implementation for:
- Better performance
- Cleaner code
- More edge case handling

Keep all tests passing."
```

---

## Debug with AI

Systematic debugging workflow.

### Terminal Error Flow

```
1. Command fails in terminal
2. Click "Debug with AI" button (appears automatically)
3. AI receives full error context
4. AI proposes fix
```

### Important: Don't Copy-Paste Errors

```
❌ Bad: Manually copying error and pasting into chat
   - Loses context
   - May truncate important info

✅ Good: Use "Debug with AI" button
   - Full stdout/stderr captured
   - Command context included
   - Environment info preserved
```

### Complex Bug Flow

```
1. Describe the bug behavior
2. Add context:
   @Files affected_file.ts
   @Git "show recent changes to this file"
   
3. Prompt:
   "This function returns null unexpectedly.
    Expected: User object
    Actual: null
    
    The change started after commit abc123.
    Analyze what could cause this."
```

### The "Rubber Duck" Technique

```
When stuck:
1. Open Chat (Cmd + L)
2. Explain the problem in detail
3. Often, writing it out reveals the answer
4. AI provides fresh perspective
```

---

## The Plan-Act Pattern

Strategic approach for complex features.

### Phase 1: PLAN (Thinking Model)

```
Model: Claude 3.5 Sonnet or GPT-5.1 High

Prompt:
"Analyze this feature request: [requirement]

DO NOT write code.
Create a detailed implementation plan:
1. Required files and changes
2. Data flow
3. Edge cases
4. Testing strategy
5. Potential risks

Save to plan.md"
```

### Phase 2: CRITIQUE (Optional)

```
Model: Different model for fresh perspective

Prompt:
"Review plan.md for:
- Efficiency gaps
- Missing requirements
- Alternative approaches
- Security concerns"
```

### Phase 3: EXECUTE (Composer)

```
Model: Composer (optimized for edits)

Prompt:
"Implement Step 1 of plan.md.
@Files plan.md

Run tests after each step.
If tests fail, stop and report.
If tests pass, proceed to next step."
```

---

## Greenfield Accelerator

Building new projects from scratch.

### Setup Phase

```
1. Initialize repo:
   git init
   npm init -y
   
2. Add documentation:
   @Docs for your stack (React, Next.js, etc.)
   
3. Create .cursorrules:
   Define tech stack and conventions
```

### Scaffold Phase

```
Prompt (Composer):
"Create a dashboard application structure:
- Next.js 14 App Router
- Tailwind CSS
- Prisma ORM
- Authentication with NextAuth

Create:
1. Folder structure
2. Base configuration files
3. Database schema
4. Auth setup
5. Basic layout components

Use @Docs for current patterns."
```

### Iterate Phase

```
Use Tab for filling in details:
- Component implementation
- API route handlers
- Database queries

Use Chat for questions:
- "How should I structure this?"
- "What's the best pattern for X?"
```

---

## Legacy Excavator

Modernizing old codebases.

### Analysis Phase

```
Prompt:
"@Codebase Analyze this codebase for:
1. Deprecated patterns
2. Security vulnerabilities
3. Performance issues
4. Missing type safety

Create migration_plan.md with prioritized fixes."
```

### Migration Phase

```
Prompt (Composer):
"Implement high-priority item 1 from migration_plan.md.
@Files migration_plan.md

Rules:
- Maintain backward compatibility
- Add tests for changed code
- Update documentation"
```

### Verification Phase

```
After each migration step:
1. Run full test suite
2. Check for type errors
3. Run linter
4. Manual smoke test
```

---

## The TaskMaster Workflow

For large, structured projects.

### Step 1: Create PRD

```markdown
# Product: [Name]

## Overview
[One paragraph description]

## User Stories
1. As a [user], I want [feature] so that [benefit]

## Technical Requirements
- Stack: [list]
- Architecture: [pattern]
- Integrations: [list]

## Data Models
[Schema definitions]

## API Endpoints
[List of endpoints]

## UI Screens
[List of screens]
```

### Step 2: Parse into Tasks

```
Prompt:
"@Files prd.md
Parse this PRD into discrete implementation tasks.
Each task should be:
- Independently completable
- Testable
- Estimated (S/M/L)

Output to tasks.md"
```

### Step 3: Execute Systematically

```
For each task:
1. Open new Composer
2. Reference task and PRD
3. Implement
4. Test
5. Commit
6. Move to next task
```

---

## Refactor Loop

Safe refactoring with self-verification.

### The Pattern

```
1. Generate → AI writes refactored code
2. Critique → AI reviews for issues
3. Test → Run automated tests
4. Repeat → Until clean
```

### Implementation

```
Step 1 - Generate:
"Refactor this function for better performance"

Step 2 - Critique (same chat):
"Now critique this implementation for:
- Security flaws
- Edge cases
- Error handling"

Step 3 - Test:
Run: npm test

Step 4 - If issues found, iterate:
"Fix the issues you identified"
```

---

## Documentation First

Using docs to prevent hallucinations.

### The Problem

```
AI trained on old library versions
→ Suggests deprecated APIs
→ Code doesn't work
```

### The Solution

```
1. Before coding:
   Add library docs via @Docs
   
2. In prompt:
   "@Docs nextjs Create a Server Component using the App Router"
   
3. AI prioritizes:
   Official docs over training data
```

### Example

```
// Adding Next.js 14 docs
Command Palette → "Cursor: Add Documentation"
URL: https://nextjs.org/docs

// Using in prompt
"@Docs nextjs How do I implement a Server Action for form submission?"
```

---

## Best Practices Summary

### Do

```
✅ Use Research-First for complex changes
✅ Write tests before implementation (TDD)
✅ Use "Debug with AI" button for errors
✅ Add documentation before using new libraries
✅ Create plans before executing
```

### Don't

```
❌ Jump straight to Composer for complex tasks
❌ Copy-paste errors manually
❌ Skip the critique phase
❌ Ignore test failures and proceed
❌ Reuse Composer windows for different tasks
```

---

## Workflow Quick Reference

| Scenario | Workflow |
|----------|----------|
| Complex refactor | Research-First Protocol |
| New feature | Plan-Act Pattern |
| Bug fixing | Debug with AI |
| New project | Greenfield Accelerator |
| Legacy code | Legacy Excavator |
| Large project | TaskMaster |
| Quick improvement | Refactor Loop |
| New library | Documentation First |

---

[← Back to Main](../README.md)
