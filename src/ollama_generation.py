import ollama # type: ignore

def Generate(subject, model_name = 'qwen2.5-coder'):

  prompt = (
    "Write a typescript programming course, format with Markdown. Be modern and concise. "
    f"Your course subject will be on '{subject}'. Do not include a footer message, just the course. "
    "Nothing more, nothing less. Don't include setting up Typescript, assume the user already has TypeScript set up, "
    "a development env set up, and just focus on the Subject at hand."
  )

  response = ollama.chat(model=model_name, messages=[
    {
      'role': 'user',
      'content': prompt,
    },
  ])
  return (response['message']['content'])
