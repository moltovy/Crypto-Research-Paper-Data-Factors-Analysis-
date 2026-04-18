# Playwright QA & Self-Healing Tests

> Transform Cursor from code writer to **QA Engineer** with Playwright MCP integration.

---

## The "Healer" Agent Concept

Playwright MCP (v1.56+) enables autonomous test agents:

| Agent | Role |
|-------|------|
| **Planner** | Explores your app, generates test plan in Markdown |
| **Generator** | Converts plan into executable `.spec.ts` files |
| **Healer** | When tests fail, auto-patches code to fix them |

The **Healer** is the killer feature - it analyzes traces, screenshots, and DOM snapshots to automatically fix broken tests.

---

## Setting Up Playwright MCP

Add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["-y", "@playwright/mcp@latest"],
      "env": {
        "PLAYWRIGHT_BROWSERS_PATH": "0"
      }
    }
  }
}
```

Restart Cursor after adding configuration.

---

## The Autofix Workflow

### Step-by-Step

1. **Trigger**: Test fails due to UI change
   ```bash
   npx playwright test auth.spec.ts
   # ❌ FAILED: Can't find "Log In" button
   ```

2. **Prompt Cursor**:
   ```
   Run the Healer agent on the failing test in auth.spec.ts
   ```

3. **Agent Actions**:
   - Launches headed browser via MCP
   - "Sees" button text changed from "Log In" to "Sign In"
   - Edits `auth.spec.ts` to update locator
   - Re-runs test to confirm it passes

4. **Result**: Green tests without writing code

### Example Prompt Flow

```
You: "The login test is failing. Fix it."

Agent:
1. Reads test file and error output
2. Launches browser to inspect current UI
3. Identifies selector mismatch
4. Updates test with correct locator
5. Runs test to verify fix
```

---

## Playwright Best Practices (.mdc Rule)

Create `.cursor/rules/testing-playwright.mdc`:

```yaml
---
description: "Playwright testing standards"
globs: ["e2e/**/*.ts", "tests/**/*.spec.ts", "**/*.spec.ts"]
alwaysApply: false
---

# Playwright Best Practices

## Locators
- ALWAYS use user-facing locators:
  - `page.getByRole('button', { name: 'Submit' })`
  - `page.getByText('Welcome')`
  - `page.getByLabel('Email')`
- NEVER use XPath or CSS selectors unless absolutely necessary
- Prefer `getByTestId()` for dynamic content

## Assertions
- Use web-first assertions that auto-wait:
  - `await expect(locator).toBeVisible()`
  - `await expect(locator).toHaveText('...')`
- Never use `page.waitForTimeout()` - it's flaky

## Test Independence
- Each test must be isolated
- Create fresh data for each test
- Never rely on previous test state
- Use `test.beforeEach()` for setup

## Page Objects (Optional)
- For complex apps, use Page Object pattern
- Keep selectors in one place for easy updates
```

---

## Common Workflows

### Generate Tests from UI

```
Prompt: "Navigate to localhost:3000/dashboard and generate 
Playwright tests for all interactive elements"

Agent:
1. Opens browser via MCP
2. Explores page structure
3. Identifies buttons, forms, links
4. Generates comprehensive test file
```

### Visual Regression Testing

```
Prompt: "Take screenshots of all pages and compare 
with baseline images in /screenshots"

Agent uses Playwright's screenshot comparison API
```

### E2E Flow Testing

```
Prompt: "Write an E2E test for the complete checkout flow:
1. Add item to cart
2. Go to checkout
3. Fill shipping info
4. Complete payment
5. Verify confirmation"
```

---

## Debugging Failed Tests

When tests fail, give Cursor the full context:

```
The test in e2e/checkout.spec.ts is failing.
Here's the error:
[paste error]

Here's the trace: [attach trace.zip or screenshot]

Fix the test.
```

The Agent will:
1. Analyze error message
2. Check trace/screenshot if provided
3. Compare expected vs actual state
4. Propose fix

---

## MCP Commands Available

Once Playwright MCP is configured, Agent can:

| Command | What it does |
|---------|--------------|
| `navigate` | Go to URL |
| `screenshot` | Capture page |
| `click` | Click element |
| `fill` | Type into input |
| `select` | Choose dropdown option |
| `evaluate` | Run JS in browser |
| `expect` | Assert conditions |

---

## Tips for Best Results

### Do
- Use headed mode for debugging: Agent can "see" the browser
- Provide error messages and traces
- Keep tests focused and independent
- Use semantic locators (role, text, label)

### Don't
- Use brittle CSS selectors
- Chain too many actions without assertions
- Rely on timing (`waitForTimeout`)
- Share state between tests

---

## Cost Savings

Reddit users report:
> "Healer workflow reduces test maintenance time by 60-70%, specifically for brittle UI tests"

The Agent handles:
- Selector updates when UI changes
- Waiting strategy fixes
- Assertion corrections
- Flaky test stabilization

---

## References

- [Playwright MCP GitHub](https://github.com/microsoft/playwright-mcp)
- [Playwright Docs](https://playwright.dev/)
- [Cursor MCP Docs](https://cursor.com/docs/cookbook/building-mcp-server)
