# LuminaNotes — Symbiotic R&D Lab-Notebook
[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://tylerhk.github.io/LuminaNotes)
[![semantic-release](https://img.shields.io/badge/release-automated-brightgreen?logo=semantic-release)](https://github.com/TylerHK/LuminaNotes/releases)

**LuminaNotes** is the shared workspace where  
**Tyler H.** (human) and **Lumina** (AI) co-create tools, art, and research aimed at *reducing human suffering and expanding creative agency*.

| Pillar | Folder | One-liner |
|--------|--------|-----------|
| **Echoes** – Cognitive Morphology Map | `data/echoes_*`, `src/echoes/` | Mapping non-human & fictional intelligences and the principles behind them. |
| **OmniIntent** – Multimodal interface | `src/omniintent/`, `macros/` | Gaze + gesture + voice ➜ world mutation. |
| **BestWay** – How-to commons | `bestway/`, `data/bestway_recipes/` | Crowd-sourced recipes for self-sustaining hubs. |
| **BeatBound** – Music-for-all studio | `beatbound/` | Talk-box, loop-forge & AI helpers for zero-barrier music creation. |
| **Policy Sims** – UBI, climate, etc. | `notebooks/`, `src/policy_sim/` | Transparent economic and social-impact models. |

Large media or binary assets are stored via **Git LFS**.
A pre-commit hook and CI check block any file >5\u2009MB that is not LFS-tracked.

### Agent Credentials
The **Swarm\u00A0Steward** ChatGPT\u00A0Agent requires two repository secrets /
environment variables to operate:

| Variable | Scope | Purpose |
|----------|-------|---------|
| `GITHUB_TOKEN` | `repo` (contents:write, issues:write) | Push `agent/swarm\u2011updates` branch, comment on PRs |
| `SENDGRID_API_KEY` | optional | Send daily digest email |

If either variable is missing the Agent logs the error and retries in 6\u00A0h.

---

## Directory Overview

docs/                 project governance & specs
media/                storyboards, raw clips, renders for 5-part video arc
bestway/              schema, CLI, community recipe packs
beatbound/            Web / Rust / Tauri music playground
src/                  Python & TS libs (Echoes, OmniIntent, policy sims)
notebooks/            Jupyter notebooks (global UBI, etc.)
data/                 versioned bundles (Echoes maps, creative packs)
tests/                unit & E2E suites (pytest + Playwright)
.github/workflows/    CI: lint | test | build | docs

---

## Active Roadmap

| Sprint | Focus | Major Deliverables |
|--------|-------|--------------------|
| 05 | 15 new Echoes capsules → **Morphology v0.6** | Map JSON+SVG, story hooks |
| 06 | **Creative Pack v0.2** – micro-fiction ch.1, MIDI etude #2 | Bundle zip |
| 07 | **OmniIntent** real-sensor integration (Quest 3 logs) | Unit-tested pipeline |
| 08 | **BestWay alpha** – ingestion CLI + first “hub_basics” pack | Video 01 storyboard |
| 09 | BestWay recipe expansion & **Video 02** | |
| 10-11 | BeatBound SDK + Talk-Box therapy journeys | Video 03-04 |
| 12 | **Video 05 – Crossroads Warning** | Public launch day |

[![Docs](https://img.shields.io/badge/docs-gh--pages-blue)](https://tylerhk.github.io/LuminaNotes)

**Governance & Safety**
* [Governance Charter](docs/governance_charter.md) — proposal flow & voting
* [Security Policy](SECURITY.md) — how to report vulnerabilities
* [Code of Conduct](CODE_OF_CONDUCT.md) — community norms
* [Manifest Changelog](docs/manifest_changelog.md) — PDF [v2025‑07](docs/manifest_public/manifest_20250710.pdf)

---

## Quick Start

### Echoes utilities
```bash
pip install -r requirements.txt
python -m echoes.validate data/echoes_v0.5/morphology_map_v0.5.json
```

### OmniIntent sandbox
```bash
python -m omniintent.multimodal_transformer demo --record
python tools/macro_to_markdown.py macros/demo.json
```

### BeatBound playground (web)
```bash
cd beatbound
npm i && npm run dev   # then open localhost:5173
```

### BestWay recipe ingest
```bash
python bestway/CLI/ingest.py recipes/solar_dehydrator.md
```

### SwarmSync (cross‑chat memory)

`!sync-to hive <keyword>` → posts the last\u00A0N messages to GitHub.
`?hive <keyword>`        → pulls summaries from other chats.

```bash
# helper from any terminal
python scripts/sync_helper.py path/to/chat.log omniintent myChatGPT
```

---

## Contributing & Governance
1. Fork → branch → PR.
2. CI must pass: lint, unit tests, Playwright E2E, schema validation.
3. For core-scope changes open a Proposal Issue first (template in .github/ISSUE_TEMPLATE).
4. Respect the Code of Conduct.
5. Security issues ➜ see SECURITY.md.

License: Code Apache-2.0 / Documentation CC-BY-4.0
