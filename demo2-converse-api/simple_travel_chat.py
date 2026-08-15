import boto3

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

MODEL_ID = "amazon.nova-lite-v1:0"

SYSTEM_PROMPT = """\
    You are a friendly travel assistant. Help users explore destinations, plan itineraries, \
and answer travel questions. Keep your answers concise and conversational."""


def run_chat() -> None:
    messages = []

    print("Travel assistant: Hello! How can I help you plan your next trip?")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye")
            break
        if not user_input:
            continue

        messages.append({"role": "user", "content": [{"text": user_input}]})

        response = bedrock.converse(
            modelId=MODEL_ID,
            system=[{"text": SYSTEM_PROMPT}],
            messages=messages,
        )

        output_message = response["output"]["message"]
        messages.append(output_message)

        reply = output_message["content"][0]["text"]

        print(f"\nTravel assistant: {reply}\n")


if __name__ == "__main__":
    run_chat()
