# Contributing

Run the maintained verification suite before proposing changes:

```powershell
uv sync --all-extras
uv run ruff check src/cqresearch scripts tests
uv run ruff format --check src/cqresearch scripts tests
uv run mypy src/cqresearch
uv run pytest -q
uv run python scripts/run_all.py --mode fixture
uv run python scripts/run_all.py --mode artifact
uv run python scripts/check_research_surface.py --module all
```

Run `uv run python scripts/run_all.py --mode local` only when legally obtained local provider inputs are present under `data_local/raw/` or an external `CMD_DATA_ROOT`. Do not commit secrets, raw cache payloads, provider exports, or generated local panels.
