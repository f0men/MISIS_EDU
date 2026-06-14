import json
import sys

import yaml


def load_params():
    with open("params.yaml", "r") as f:
        return yaml.safe_load(f)


def validate_model():
    params = load_params()
    accuracy_min = params["accuracy_min"]

    with open("metrics/metrics.json", "r") as f:
        metrics = json.load(f)

    accuracy = metrics["accuracy"]

    print(f"Accuracy: {accuracy:.4f}, threshold: {accuracy_min}")

    if accuracy < accuracy_min:
        print("Model validation failed: accuracy below threshold!")
        sys.exit(1)

    print("Model validation passed!")


if __name__ == "__main__":
    validate_model()
