#!/usr/bin/env python
"""
sync_helper.py
--------------
Usage:
  python scripts/sync_helper.py <chat_log.txt> <keyword> <source>

Reads the last 20 lines of the chat log, generates a naive
summary (first + last line fallback), and posts via SwarmSync.
"""
import sys, os, pathlib, tools.swarm_sync as hive

log, keyword, source = sys.argv[1:4]
lines = pathlib.Path(log).read_text().splitlines()[-20:]
summary = lines[0][:120] + " … " + lines[-1][:120]
raw = "\n".join(lines)

hive.post(keyword, summary, raw, source)
print("🪽  Synced", keyword, "from", source)
