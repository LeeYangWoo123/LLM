import os
from openai import OpenAI
from dotenv import load_dotenv

# .env 파일이 같은 디렉터리에 있을 경우
load_dotenv()

# 환경변수명은 OPENAI_API_KEY로 통일
api_key = os.getenv("OPENAI_API_KEY")
print("API KEY:", api_key)  # 값이 출력되는지 확인

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4.1-2025-04-14",
    messages=[
        {"role": "user", "content": "왜 강남은 강남이라고 할까요?"}
    ],
    temperature=0.0
)
print(response)