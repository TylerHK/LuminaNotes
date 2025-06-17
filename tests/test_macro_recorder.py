import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from omniintent import macro_recorder as mr


def test_start_stop(tmp_path):
    mr.start_record()
    mr.log_event("hello", "world")
    mr.stop_record()
    out = tmp_path / "macro.json"
    mr.save_json(out)
    assert out.exists()
    mr.replay(out)
