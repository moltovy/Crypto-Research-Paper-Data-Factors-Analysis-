# .mdc Rule Examples

> Production-ready templates for different tech stacks.

---

## Structure

```yaml
---
description: "Rule description"
globs: ["**/*.tsx"]
alwaysApply: false
---

# Your rules in Markdown
```

---

## Global Rules

**File**: `.cursor/rules/global.mdc`

```yaml
---
description: "Project-wide standards"
globs: ["**/*"]
alwaysApply: true
---

# Project Standards

## Tech Stack
- Next.js 14+ (App Router)
- TypeScript (strict)
- Tailwind CSS
- Prisma + PostgreSQL

## Principles
- Composition over inheritance
- Functions under 50 lines
- No magic numbers
- JSDoc on all exports

## Security
- Never log PII
- Validate inputs with Zod
- Parameterized queries only
```

---

## React/TypeScript

**File**: `.cursor/rules/react-standards.mdc`

```yaml
---
description: "React component standards"
globs: ["src/**/*.tsx", "components/**/*"]
alwaysApply: false
---

# React Standards

## Components
- Functional only (no classes)
- Server Components by default
- Named exports: `export const Button`

## TypeScript
- NO `any` - use `unknown` or generics
- Define props interface for every component:

```typescript
export interface ButtonProps {
  variant: 'primary' | 'secondary';
  children: React.ReactNode;
}
```

## Styling
- Tailwind only
- Use `clsx` for conditionals
- No hardcoded colors

## Forbidden
- ❌ useState for server data
- ❌ useEffect for fetching
- ❌ Prop drilling > 2 levels
```

---

## Python/FastAPI

**File**: `.cursor/rules/python-backend.mdc`

```yaml
---
description: "Python backend standards"
globs: ["**/*.py", "backend/**/*"]
alwaysApply: false
---

# Python Standards

## Modern Python
- Type hints on ALL functions
- Use `str | None` not `Optional[str]`
- f-strings for formatting

## FastAPI
- Pydantic v2 for validation
- ALL I/O must be `async def`
- Use `HTTPException` for errors

## Database
- Separate ORM models from schemas
- Use `selectinload` for N+1

## Forbidden
- ❌ `import *`
- ❌ Bare `except:`
- ❌ Mutable default args
```

---

## Testing

**File**: `.cursor/rules/testing.mdc`

```yaml
---
description: "Testing standards"
globs: ["**/*.test.ts", "**/*.spec.ts", "tests/**/*"]
alwaysApply: false
---

# Testing Standards

## Structure (AAA)
```typescript
it('should create user', async () => {
  // Arrange
  const data = { email: 'test@example.com' };
  
  // Act
  const result = await createUser(data);
  
  // Assert
  expect(result.email).toBe(data.email);
});
```

## Rules
- Test behavior, not implementation
- Mock external services only
- 80%+ coverage on business logic
```

---

## Anti-Lazy Output

**File**: `.cursor/rules/anti-lazy.mdc`

```yaml
---
description: "Prevent AI shortcuts"
globs: ["**/*"]
alwaysApply: true
---

# Output Rules

## NEVER
- ❌ "// ... existing code ..."
- ❌ "// rest remains same"
- ❌ Truncating files
- ❌ Placeholder comments

## ALWAYS
- ✅ Complete file contents
- ✅ All imports
- ✅ Full function bodies
- ✅ Exact formatting

You are an expert who outputs complete, production-ready code.
```

---

## Setup

```bash
mkdir -p .cursor/rules
touch .cursor/rules/global.mdc
touch .cursor/rules/react-standards.mdc
```
