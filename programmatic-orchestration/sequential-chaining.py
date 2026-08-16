import boto3
import json

from mypy_boto3_bedrock_runtime.type_defs import BlobTypeDef

QUESTIONS = [
    """I'm experiencing problems with json library in Python. 
    How do I convert a str to json?""",
    """
    How can I demonstrate that the derivative of e^x is e^x?
    """,
    """
    Improve this sentence: 
    "The cat's mother was unalived by a pedestrian with a banana."
    """,
]

PROMPTS = {
    "MATH": """
    You're a professional math teacher that emphasizes understanding and rigor.
    Answer the user's question step by step and add a small summary at the end of your answer.
    
    Question:
    {question}
    """,
    "CODE": """
    You're a senior SWE and patient socratic teacher. 
    Do not answer the user's question directly with code or just provide snippets if needed.
    Question:
    {question}
    """,
    "WRITING": """
    You're a professional copywriter and drafter.
    Check for any grammatical mistakes in the user's draft and help him structure his ideas.

    Question:
    {question}
    """,
}


def invoke(prompt: str, temperature: float = 0.0) -> str:
    bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")
    MODEL_ID = "amazon.nova-lite-v1:0"

    body = {
        "messages": [{"role": "user", "content": [{"text": prompt}]}],
        "inferenceConfig": {"maxTokens": 512, "temperature": 0.0},
    }
    response = bedrock.invoke_model(
        modelId=MODEL_ID,
        body=json.dumps(body),
        contentType="application/json",
        accept="application/json",
    )

    result = json.loads(response["body"].read())
    return result["output"]["message"]["content"][0]["text"]


def classify(question: str) -> str:
    prompt = f"""\
    Classify the following question into one of these categories: MATH, CODE, WRITING.
    Answer only with one word and do not create other categories.
    
    Question:
    {question}
    """
    return invoke(prompt).strip().upper()


def main() -> None:
    for question in QUESTIONS:
        print(classify(question))


if __name__ == "__main__":
    main()
