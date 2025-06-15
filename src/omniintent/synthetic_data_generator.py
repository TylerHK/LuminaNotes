"""Utility for generating synthetic training data for OmniIntent models."""

import random


def generate_examples(num:int=1):
    """Return a list of simple synthetic text strings."""
    examples = []
    for _ in range(num):
        examples.append(f"sample-{random.randint(0, 9999)}")
    return examples
