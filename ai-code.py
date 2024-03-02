import os
import openai
openai.api_key = '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'

messages = [
    {"role": "system", "content": "You're a creating a timetable for students in tabular form to study for certain hours a day"}
]

def chatbot(event):
    content = "Hi"
    messages.append({"role": "user", "content": content})

    completion = openai.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=messages
    )

    chat_response = completion.choices[0].message.content
    print(f'ChatGPT: {chat_response}')
    messages.append({"role": "assistant", "content": chat_response})