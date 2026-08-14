import json
import boto3

from pathlib import Path

from urllib3 import response

notes_path = Path("./NOTES.md")
response_schema = Path("./response_stream_schema.json")

if not notes_path.exists():
    raise FileNotFoundError("NOTES.md not found")

MEETING_NOTES = notes_path.read_text()


def summarize_notes_stream(notes: str) -> None:
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
        "inferenceConfig": {"temperature": 0.0, "maxTokens": 512},
    }

    response = bedrock.invoke_model_with_response_stream(
        modelId=model_id,
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json",
    )

    for event in response["body"]:
        chunk = json.loads(event["chunk"]["bytes"])
        if "contentBlockDelta" in chunk:
            print(
                chunk["contentBlockDelta"]["delta"].get("text", ""), end="", flush=True
            )


def main() -> None:
    summarize_notes_stream(MEETING_NOTES)


if __name__ == "__main__":
    main()
