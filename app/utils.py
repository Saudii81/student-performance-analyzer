import json


def load_students_from_json(file_path: str) -> dict:
    """Load student scores from a JSON file. Returns a dict of {name: score}."""
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("JSON must be an object mapping student names to scores.")
        return {k: float(v) for k, v in data.items()}
    except FileNotFoundError:
        raise FileNotFoundError(f"Student data file not found: {file_path}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {file_path}: {e}")