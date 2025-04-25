import numpy as np

def normalize(value, min_val, max_val):
    """Normalize a value between 0 and 1."""
    return (value - min_val) / (max_val - min_val)

def denormalize(value, min_val, max_val):
    """Denormalize a value from 0-1 range to original scale."""
    return value * (max_val - min_val) + min_val

def validate_input(value, min_val, max_val, param_name):
    """Validate if the input is within the expected range."""
    if not (min_val <= value <= max_val):
        raise ValueError(f"{param_name} should be between {min_val} and {max_val}.")
    return value
