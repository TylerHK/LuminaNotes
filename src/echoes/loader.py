import json
from jsonschema import validate, ValidationError

# Placeholder schema for morphology maps
MORPHOLOGY_SCHEMA = {
    "type": "object",
    "properties": {
        "version": {"type": "string"},
        "nodes": {"type": "array"},
    },
    "required": ["version", "nodes"],
}

def load_morphology_map(path):
    """Load a morphology map from ``path`` and validate it."""
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    validate_morphology_map(data)
    return data


def validate_morphology_map(data):
    """Validate a morphology map structure."""
    try:
        validate(instance=data, schema=MORPHOLOGY_SCHEMA)
    except ValidationError as e:
        raise

