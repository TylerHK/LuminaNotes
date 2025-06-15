import json
import os


def test_spec_schema_keys():
    path = os.path.join(os.path.dirname(__file__), "tokenizer_spec.json")
    with open(path, "r", encoding="utf-8") as f:
        spec = json.load(f)
    required = {"tokenizer", "vocab_size", "special_tokens"}
    assert required.issubset(spec.keys())
