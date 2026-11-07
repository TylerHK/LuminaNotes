# Agent instructions

Read README.md and the README/instructions in all affected ancestor and subdirectories before editing. Discover nested AGENTS.md and CLAUDE.md first. Respect docs/governance_charter.md for core-scope changes.

For record/schema changes inspect the actual producer and existing records, then run `python scripts/validate_records.py` and `pytest -q tests/test_validate_records.py`. SwarmSync packets and the generated keyword index have different shapes; legacy minute timestamps and producer second timestamps both exist. Do not invent evidence or rewrite historical packets.

The record validator and its regression tests block CI. Legacy lint and broad test steps remain advisory; a green workflow is not proof those pass. Report them separately.

Use draft branches with one writer each. No main writes, merge, deployment, purchase, email, or external publication without explicit authorization. In particular tools/swarm_sync.py posts to main: do not invoke its post command for a handoff. Stage handoff documentation through a draft PR instead.

OmniIntent Council first-minute UX work belongs in the canonical TylerHK/IAmTheDrop runtime after its own instructions are read; this repository supplies notebook and SwarmSync context, not runtime proof.
