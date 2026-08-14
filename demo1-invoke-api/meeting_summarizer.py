from pathlib import Path

import boto3
import json

notes_path = Path("./demo1-invoke-api/NOTES.md")
if not notes_path.exists():
    raise FileNotFoundError(f"Meeting notes file not found: {notes_path}")
MEETING_NOTES = notes_path.read_text()


def summarize_meeting(notes: str) -> str:
    bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
    model_id = "amazon.nova-pro-v1:0"

    prompt = (
        "Summarize the following meeting notes into:\n"
        "1. Key decisions made \n"
        "2. Action items with owners\n\n"
        "Meeting notes:"
        "<notes>\n"
        f"{notes}\n"
        "<notes/>\n"
    )

    body = {
        "messages": [{"role": "user", "content": [{"text": prompt}]}],
        "inferenceConfig": {"maxTokens": 512, "temperature": 0.0},
    }
    response = bedrock.invoke_model(
        modelId=model_id,
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json",
    )

    result = json.loads(response["body"].read())
    return result["output"]["message"]["content"][0]["text"]


def main():
    output_path = Path("./demo1-invoke-api/meeting_summary.md")
    output_path.write_text(summarize_meeting(MEETING_NOTES))


if __name__ == "__main__":
    main()
