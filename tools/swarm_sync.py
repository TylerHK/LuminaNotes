"""
swarm_sync.py
-------------
CLI to post or fetch "sync packets" to GitHub.
Run from any environment where GITHUB_TOKEN is set.
"""
import os, json, datetime, pathlib, sys
from github import Github

REPO = "TylerHK/LuminaNotes"
FOLDER = "swarm_sync"

def post(keyword:str, summary:str, raw:str, source:str):
    gh = Github(os.environ["GITHUB_TOKEN"])
    repo = gh.get_repo(REPO)
    day = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    fname = f"{FOLDER}/{day}_{source}_{keyword}.json"
    body = json.dumps({
        "keyword": keyword,
        "timestamp": day,
        "summary": summary,
        "raw": raw,
        "source_chat": source
    }, indent=2)
    repo.create_file(fname, f"swarm: add {keyword} from {source}", body, branch="main")

def fetch(keyword:str, limit:int=5):
    gh = Github(os.environ["GITHUB_TOKEN"])
    repo = gh.get_repo(REPO)
    contents = repo.get_contents(FOLDER)
    hits=[]
    for c in contents:
        if keyword in c.name:
            hits.append(json.loads(repo.get_contents(c.path).decoded_content))
    # newest first
    hits = sorted(hits, key=lambda x: x["timestamp"], reverse=True)[:limit]
    print(json.dumps(hits, indent=2))

if __name__ == "__main__":
    cmd,*args = sys.argv[1:]
    if cmd=="post":
        post(*args)   # keyword summary raw source_chat
    elif cmd=="fetch":
        fetch(args[0])
