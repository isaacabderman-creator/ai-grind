import json
import boto3
import sys

from typing import Dict
from pathlib import Path

model_path = Path("./foundational_models_list.json")
output_path = Path("./models.json")


def write_foundational_models_list(region_name: str) -> None:
    bedrock = boto3.client("bedrock", region_name=region_name)
    response = bedrock.list_foundation_models()
    models = [model["modelId"] for model in response["modelSummaries"]]
    content = json.dumps(models, indent=2, default=str)
    output_path.write_text(content)


def main() -> None:
    write_foundational_models_list(sys.argv[1])


if __name__ == "__main__":
    main()
