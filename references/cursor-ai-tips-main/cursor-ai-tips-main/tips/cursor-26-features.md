# 🤖 What's New in Cursor 2.6 (March 2026)

> **"The Automation Release"** — Cursor 2.6 introduces always-on, event-driven agents and a controversial shift to token-based pricing for frontier models.

---

## 🆕 Cursor Automations (GA)

**Released:** March 5, 2026 | **Status:** Generally Available

The biggest feature in Cursor 2.6 is **Automations** — agents that work autonomously, triggered by external events, even when you're away from your computer.

### How It Works

```
External Event → Trigger → Agent Task → Output
```

### Supported Triggers

| Trigger | Source | Example |
|---------|--------|---------|
| **GitHub PR** | Push, Open, Review | Auto code review on new PRs |
| **Slack Webhook** | Message, Thread | Create JIRA task from Slack message |
| **Linear Issue** | Created, Updated | Auto-implement when issue assigned |
| **PagerDuty** | Incident Alert | Read logs, open fix PR automatically |
| **Cron** | Scheduled | Run daily test suite at 6 AM |

### Configuration

Automations are configured via the **Cursor Dashboard** (not in-editor):

1. Navigate to **Dashboard → Automations**
2. Select a **Trigger** type
3. Define the **Task** via `.cursorrules` or a custom command

### Example Automation

```
Trigger: GitHub PR (push to main)
Task: Run all tests. If any fail, create a Linear ticket with the error details
      and post a summary to #dev-alerts on Slack.
```

### Security Considerations

- Automations run with your configured API keys and permissions
- Consider using separate service accounts for sensitive operations
- Review automation logs regularly in the Dashboard
- Start with read-only triggers before allowing write operations

---

## 🏪 Team Marketplaces for Plugins

**Released:** March 3-4, 2026 | **Available for:** Teams & Enterprise Plans

Create private, internal plugin marketplaces for your organization:

- Connect a **private GitHub repo** as your plugin source
- Distribute team-specific **MCP servers** securely
- Control which internal tools are available to team members
- Centralized management via admin dashboard

### Use Cases

- Distribute proprietary code generation templates
- Share internal API MCP servers (database, auth, etc.)
- Enforce team-wide coding standards via plugins
- Manage internal tool access per role/team

---

## 💰 Max Mode Pricing (Effective March 16, 2026)

> ⚠️ **BREAKING CHANGE**: Frontier models move to dynamic token-based billing

### What Changed

| Before (Request-Based) | After (Max Mode) |
|:-----------------------|:-----------------|
| 1 query = 1 request | Charged per token consumed |
| Fixed cost per interaction | Dynamic, API-style billing |
| Predictable monthly spend | Variable based on usage patterns |

### Models Moving to Max Mode

| Model | Previous Access | After March 16 |
|-------|----------------|-----------------|
| GPT-5.4 | Pro Plan | Max Mode Only |
| GPT-5.3 Codex | Pro Plan | Max Mode Only |
| Claude Opus 4.6 | Pro Plan | Max Mode Only |
| Claude Sonnet 4.6 ⚠️ | Pro Plan | Max Mode Only |
| Claude Opus 4.5 | Pro Plan | Max Mode Only |

> ⚠️ **Claude Sonnet 4.6** being moved to Max Mode is the most controversial change. As the community's "workhorse" model, this effectively makes the Pro plan significantly more expensive for heavy users.

### Budget Recommendations

1. **Switch to DeepSeek V4 Lite** via OpenRouter for routine tasks
2. **Use Composer 1.5** (still included in Pro plan) for code synthesis
3. **Reserve Max Mode** for complex refactoring that truly needs frontier models
4. **Monitor token usage** carefully — set spending alerts in Dashboard

---

## 🧠 March 2026 Model Landscape

| Model | Quality | Speed | Cost | Context | Best For |
|-------|---------|-------|------|---------|----------|
| Claude Opus 4.6 | 9.8/10 | 🐌 | $$$ | 1M | Complex refactoring, multi-file planning |
| GPT-5.4 | 9.5/10 | ⚡⚡ | $$$ | 1M+ | General use, high reasoning |
| GPT-5.3 Codex | 9.2/10 | ⚡⚡⚡ | $$ | ~1M | Terminal commands, one-shot tasks |
| DeepSeek V4 Lite | 9.0/10 | ⚡⚡⚡ | ¢ | 1M | Open-source, budget local tasks |
| Gemini 3.1 Pro | 8.5/10 | ⚡⚡ | $ | 2M | Massive codebase reading |

### DeepSeek V4 Lite (New!)

- **Codename:** "0302" / "Healer Alpha"
- **Parameters:** ~200B
- **Context:** 1M tokens (up from 128K)
- **Cost:** 1/10 to 1/50 of GPT models
- **Setup:** Use OpenRouter as custom API endpoint in Cursor settings

---

## ⚔️ Competitor Landscape (March 2026)

| | Cursor (v2.6) | Windsurf (Wave 14) | Google Antigravity | Amazon Kiro |
|---|---|---|---|---|
| **Philosophy** | Advanced Editor | Parallel Agent Flow | Task Control (Agent-First) | Spec-Driven Dev |
| **Price** | $20/mo | $15/mo | Free (quota-limited) | AWS Ecosystem |
| **Killer Feature** | Automations | Arena Mode (A/B) | Artifact Generation | Requirements.md |
| **Biggest Issue** | Revert Bug | Rate Limits | Quota Crisis | Poor code quality |

### Amazon Kiro (New!)

A spec-driven IDE from Amazon — the anti-"Vibe Coding" approach:

```
1. You write: requirements.md (EARS format)
2. Kiro generates: design.md (with Mermaid diagrams)
3. Kiro generates: tasks.md
4. Agents write code following the "contract"
```

**Current verdict:** Great philosophy, beautiful UI, but Amazon's model (Kira) doesn't follow specs reliably. Best used as a code reviewer, not a code writer.

---

## 🔥 New Workflows to Adopt

### Context7 MCP Server

The most popular new MCP server — pulls real-time documentation for 2000+ libraries:

```json
// .cursor/mcp.json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"]
    }
  }
}
```

### "Linear vs Looped" Agentic Engineering

| Workflow | When | How |
|----------|------|-----|
| **Linear** | Quick fixes, MVP | `Cmd+K` → Prompt → Code |
| **Looped** | Complex features | Plan → Test → Code → Run → Fix → Repeat |

### New .cursorrules for Agent Control

```markdown
# Anti-Hallucination
If importing an npm package, first run `npm list` via terminal agent
to verify it's installed with 100% certainty.

# Interface Freeze
When adding features, NEVER write implementation directly.
First define types/interfaces, get approval, then implement.
```

---

*Last updated: March 12, 2026*
