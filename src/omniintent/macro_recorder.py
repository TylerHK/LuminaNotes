import json
import time
from pathlib import Path
from typing import Any, Dict, List

_events: List[Dict[str, Any]] = []
_recording = False


def start_record() -> None:
    """Begin recording macro events."""
    global _events, _recording
    _events = []
    _recording = True
    _events.append({"type": "start", "time": time.time()})


def stop_record() -> None:
    """Stop recording events."""
    global _recording
    if _recording:
        _events.append({"type": "stop", "time": time.time()})
        _recording = False


def log_event(prompt: str, response: str) -> None:
    """Record a prompt/response pair."""
    if _recording:
        _events.append(
            {
                "type": "step",
                "time": time.time(),
                "prompt": prompt,
                "response": response,
            }
        )


def save_json(path: Path) -> None:
    """Write recorded events to a JSON file."""
    if _events:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            json.dump(_events, f, indent=2)


def replay(json_path: Path) -> None:
    """Replay events from a saved macro."""
    events = json.loads(Path(json_path).read_text())
    prev_time = None
    for event in events:
        if prev_time is not None:
            delay = event["time"] - prev_time
            time.sleep(min(max(delay, 0), 2))
        if event["type"] == "step":
            print(event["prompt"])
            print(event["response"])
        prev_time = event["time"]
