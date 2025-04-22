# pip install portkey_ai
import os
from portkey_ai import Portkey, PORTKEY_GATEWAY_URL

def main():
    # Construct a client with a virtual key
    portkey = Portkey(
        api_key=os.getenv("PORTKEY_API_KEY"),
        virtual_key="google-virtual-005f0a",
        base_url=PORTKEY_GATEWAY_URL
    )

    completion = portkey.chat.completions.create(
        messages = [{ "role": 'user', "content": 'Who is QAware?' }],
        model="gemini-1.5-pro",
        max_tokens=64)
    print(completion)

if __name__ == "__main__":
    main()
