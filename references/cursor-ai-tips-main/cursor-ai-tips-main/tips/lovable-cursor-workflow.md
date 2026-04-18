# Lovable + Cursor Hybrid Workflow

[← Back to Main](../README.md)

> The most popular "vibe coding" pattern for rapid SaaS development in 2025.

---

## Why This Workflow?

| Tool | Strength | Weakness |
|------|----------|----------|
| **Lovable** | Fast UI generation, visual feedback | Limited backend logic |
| **Cursor** | Complex engineering, full control | Slower for basic UI |

**Combined**: Build full SaaS products in days, not weeks.

---

## The 5-Step Pipeline

### Step 1: Velocity (Lovable)

Use Lovable for initial frontend scaffolding:

```
✅ Generate UI components
✅ Tailwind styling
✅ Basic component structure
✅ Visual feedback loop (faster than code)
```

**Example prompt in Lovable**:
```
"Create a dashboard with:
- Sidebar navigation
- Stats cards at top
- Data table with pagination
- User avatar dropdown"
```

### Step 2: Sync to GitHub

Push the Lovable project to a GitHub repository:

```
Lovable → Settings → GitHub Integration → Connect
```

This creates a repo with your generated code.

### Step 3: Clone in Cursor

```bash
git clone https://github.com/yourname/project
cd project
cursor .
```

### Step 4: Engineering (Cursor)

Use Cursor Composer for complex features Lovable can't handle:

```
✅ Supabase Authentication
✅ Database schema & migrations
✅ Stripe payment webhooks
✅ Complex business logic
✅ API integrations
✅ Real-time features
```

**Example Cursor workflow**:
```
"Implement Stripe subscription flow:
- @tech_spec.md for stack requirements
- Create checkout session endpoint
- Handle webhook events
- Store subscription status in Supabase
- Update UI based on plan tier"
```

### Step 5: Sync Back

Push changes to GitHub. Lovable pulls the logic updates:

```bash
git add -A
git commit -m "feat: add Stripe integration"
git push
```

Lovable stays in sync with your engineering changes.

---

## When to Use Each Tool

### Use Lovable For

```
🎨 UI Design & Layout
├── Landing pages
├── Dashboard layouts
├── Component styling
├── Responsive design
└── Visual iterations
```

### Use Cursor For

```
⚙️ Backend Engineering
├── Authentication flows
├── Database operations
├── Payment processing
├── API integrations
├── Complex state management
├── Testing & debugging
└── Performance optimization
```

---

## Why This Wins

| Problem | Solution |
|---------|----------|
| Developers waste time on CSS/layout | Lovable handles it |
| No-coders hit walls with complex logic | Cursor handles it |
| Context switching between tools | GitHub keeps them in sync |
| Slow iteration on visual changes | Lovable's instant preview |

---

## Real-World Success Stories

From Reddit and Twitter:

> "Built a complete SaaS with auth, payments, and dashboard in 4 days using Lovable + Cursor."

> "Lovable got me 80% there in 2 hours. Cursor handled the Stripe webhooks and complex queries."

> "Stop centering divs manually. Let Lovable do that. Use Cursor for the hard stuff."

---

## Best Practices

### 1. Define Boundaries

Create a mental model of what goes where:

```
Lovable owns:
├── src/components/ui/
├── src/pages/ (layout only)
└── Tailwind config

Cursor owns:
├── src/lib/
├── src/services/
├── API routes
└── Database schema
```

### 2. Use Spec Files

Before Cursor work, create specifications:

```
product_spec.md → What features to build
tech_spec.md    → What stack to use
```

This prevents Cursor from conflicting with Lovable's patterns.

### 3. Commit Frequently

```bash
# After Lovable changes
git commit -m "feat(ui): dashboard layout from Lovable"

# After Cursor changes
git commit -m "feat(api): Stripe webhook handler"
```

Clean git history makes debugging easier.

### 4. Handle Conflicts

If Lovable regenerates a file Cursor modified:

```bash
git diff                    # See what changed
git checkout --ours file    # Keep Cursor's version
# OR
git checkout --theirs file  # Keep Lovable's version
```

---

## Example Project Structure

```
project/
├── src/
│   ├── components/
│   │   └── ui/          # Lovable-generated
│   ├── pages/           # Lovable layout + Cursor logic
│   ├── lib/             # Cursor-owned
│   │   ├── supabase.ts
│   │   └── stripe.ts
│   └── services/        # Cursor-owned
│       ├── auth.ts
│       └── payments.ts
├── supabase/
│   └── migrations/      # Cursor-owned
├── product_spec.md
├── tech_spec.md
└── .cursorrules
```

---

## Quick Start Checklist

```
□ Create project in Lovable
□ Generate initial UI/components
□ Connect to GitHub
□ Clone locally
□ Open in Cursor
□ Create spec files (optional but recommended)
□ Implement backend logic
□ Push changes
□ Verify sync in Lovable
```

---

## References

- [Lovable Documentation](https://docs.lovable.dev)
- [Cursor + Supabase Guide](tips/mcp-integration.md)
- [Spec-First Workflow](tips/spec-first-workflow.md)

---

*Source: Viral workflow on Twitter/X & r/cursor*

[← Back to Main](../README.md)
