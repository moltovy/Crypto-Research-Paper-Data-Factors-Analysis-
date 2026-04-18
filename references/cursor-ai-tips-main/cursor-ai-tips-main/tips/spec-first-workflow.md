# Spec-First Development Workflow

> Stop prompting "Build a Todo App." Start with specifications.

---

## The Problem

Vague prompts lead to:
- AI guessing your requirements
- Wrong architecture choices
- Constant corrections and rewrites
- Wasted tokens and time

---

## The Solution: Document-Driven Development

Create specification documents that the AI **must read** before writing code.

### File Structure

```
project/
├── product_spec.md      # What the app does
├── tech_spec.md         # How it's built
├── .cursor/
│   └── rules/
│       └── architect.mdc  # Enforces reading specs
└── src/
```

---

## 1. Product Specification

**File**: `product_spec.md`

```markdown
# Product Specification: TaskFlow

## Overview
TaskFlow is a team task management app with real-time collaboration.

## User Roles
- **Admin**: Full access, user management
- **Member**: Create/edit own tasks, view team tasks
- **Guest**: View-only access

## Core Features

### Task Management
- Create tasks with title, description, due date
- Assign tasks to team members
- Priority levels: Low, Medium, High, Urgent
- Status: Todo, In Progress, Review, Done

### Real-time Updates
- Live task status changes
- Presence indicators (who's online)
- Activity feed

### Notifications
- Email on task assignment
- In-app notifications
- Daily digest option

## Non-Goals (Out of Scope)
- Time tracking
- Invoicing
- File attachments (v2)

## Success Metrics
- Task completion rate > 80%
- Average response time < 200ms
- User retention > 60% at 30 days
```

---

## 2. Technical Specification

**File**: `tech_spec.md`

```markdown
# Technical Specification: TaskFlow

## Stack
- **Frontend**: Next.js 15 (App Router), TypeScript, Tailwind CSS
- **Backend**: Next.js API Routes + Server Actions
- **Database**: Supabase (PostgreSQL)
- **Auth**: Supabase Auth (magic link + OAuth)
- **Real-time**: Supabase Realtime
- **Deployment**: Vercel

## Architecture Decisions

### Why Supabase over Firebase?
- PostgreSQL > NoSQL for relational task data
- Row Level Security for multi-tenant
- Better TypeScript support

### State Management
- Server state: React Query (TanStack Query)
- Client state: Zustand (minimal, only for UI state)
- No Redux - overkill for this app

### File Structure
```
src/
├── app/              # Next.js routes
├── components/       # React components
│   ├── ui/          # Primitives (Button, Input)
│   └── features/    # Feature components (TaskCard)
├── lib/             # Utilities, Supabase client
├── hooks/           # Custom React hooks
├── types/           # TypeScript types
└── services/        # Business logic
```

## API Design
- RESTful for CRUD operations
- Server Actions for mutations
- Supabase client for real-time subscriptions

## Error Handling
- Zod for input validation
- Custom error classes
- Sentry for production monitoring

## Testing Strategy
- Unit: Vitest for utilities and hooks
- Integration: Playwright for E2E
- No snapshot tests (maintenance burden)
```

---

## 3. The Architect Rule

**File**: `.cursor/rules/architect.mdc`

```yaml
---
description: "Enforces specification compliance"
globs: ["**/*"]
alwaysApply: true
---

# Architectural Compliance

## Before Writing ANY Code

YOU MUST:
1. Read `@product_spec.md` to understand user requirements
2. Read `@tech_spec.md` to ensure stack compatibility
3. If a request conflicts with specs, STOP and ask for clarification

## Enforcement Rules

### Stack Compliance
- Only use libraries listed in tech_spec.md
- If a new library is needed, propose it first
- Follow the file structure defined in tech_spec.md

### Feature Compliance
- Check if feature is in product_spec.md scope
- If feature is in "Non-Goals", reject it
- Reference specific sections when implementing

### Code Standards
- TypeScript strict mode (no `any`)
- All components must have props interface
- Server Components by default

## Example Workflow

When asked to "Add a feature":
1. Check product_spec.md - is it in scope?
2. Check tech_spec.md - how should it be built?
3. If unclear, ask: "This isn't in the spec. Should I add it?"
```

---

## Workflow in Practice

### Starting a New Feature

```
You: "Add the task assignment feature"

Agent thinks:
1. Reads product_spec.md → Task assignment is in scope
2. Reads tech_spec.md → Use Server Actions, Supabase
3. Implements according to specs
```

### When Specs Conflict

```
You: "Use Redux for state management"

Agent (with architect.mdc):
"The tech_spec.md specifies Zustand for client state 
and React Query for server state. Redux is not in 
the approved stack. Should I:
1. Update tech_spec.md to include Redux?
2. Proceed with Zustand as specified?"
```

### Adding New Requirements

```
You: "Add time tracking to tasks"

Agent:
"Time tracking is listed under 'Non-Goals (Out of Scope)' 
in product_spec.md as a v2 feature. Should I:
1. Add it anyway and update the spec?
2. Create a separate feature flag for v2?
3. Skip this for now?"
```

---

## Benefits

| Without Specs | With Specs |
|--------------|------------|
| AI guesses stack | AI follows defined stack |
| Random file structure | Consistent organization |
| Scope creep | Clear boundaries |
| Constant corrections | First-try accuracy |
| Wasted tokens | Efficient prompts |

---

## Quick Start Template

### Minimal product_spec.md
```markdown
# [App Name]

## What it does
[One paragraph]

## Core Features
- Feature 1
- Feature 2
- Feature 3

## Out of Scope
- Not this
- Not that
```

### Minimal tech_spec.md
```markdown
# Tech Stack

## Frontend
- Framework: [Next.js/React/Vue]
- Styling: [Tailwind/CSS Modules]

## Backend
- API: [Next.js API/Express/FastAPI]
- Database: [Supabase/Prisma/MongoDB]

## Key Libraries
- [Library 1]: [Why]
- [Library 2]: [Why]
```

---

## Pro Tips

1. **Version your specs** - Update when requirements change
2. **Keep specs concise** - AI context window is limited
3. **Reference in prompts** - "Per tech_spec.md, use Supabase for..."
4. **Review AI proposals** - If it suggests something off-spec, question it

---

*Source: r/cursor power users workflow*
