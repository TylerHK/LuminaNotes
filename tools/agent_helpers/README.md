# Agent Helpers

Shared helper modules (GitHub wrappers, SendGrid mailer, RSS fetch) used by
GrantSeeker, ResearchScout, PRWatch.  Agents import via:

```python
from tools.agent_helpers.github import create_pr
