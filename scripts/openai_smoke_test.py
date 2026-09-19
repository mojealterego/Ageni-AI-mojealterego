"""Minimal live OpenAI API smoke test for manual GitHub Actions runs."""

import os
import sys


def main() -> int:
    api_key = os.getenv("OPENAI_API_KEY", "").strip()
    if not api_key:
        print("ERROR: OPENAI_API_KEY is not available to this workflow.", file=sys.stderr)
        return 2

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key, timeout=30.0, max_retries=0)
        response = client.responses.create(
            model="gpt-5.0",
            input="Reply with exactly: API connection OK",
            max_output_tokens=32,
        )
        output = (response.output_text or "").strip()
        if not output:
            print("ERROR: API responded but returned no text.", file=sys.stderr)
            return 1
        print("SUCCESS: OpenAI Responses API returned a response.")
        print(f"Model: {response.model}")
        print(f"Response: {output}")
        return 0
    except Exception as exc:  # Report exception type/message, never print credentials.
        print(f"ERROR: OpenAI API smoke test failed ({type(exc).__name__}): {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
