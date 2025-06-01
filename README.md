# TypeScript Tommy

This is a minimal AI-powered CLI tool that generates concise, modern, markdown-formatted TypeScript programming courses based on a subject you provide.

Powered by [Ollama](https://ollama.com/) and a local model (`qwen2.5-coder`), this tool lets you instantly create technical documentation or lessons for any topic in TypeScript — no fluff, sometimes boilerplate setup instructions.

- Markdown output
- Local model generation using Ollama
- Input any subject and get a tailored course
- Automatically saves to a `.md` file
- Optional `--output` flag for custom filenames

## Installation

Clone this repository and ensure you have [Ollama](https://ollama.com/) installed with a compatible model:

```bash
git clone https://github.com/myferr/typescript-tommy  # Clone repository
cd typescript-tommy                                   # Navigate to directory
pip install -r requirements.txt                       # Install ollama (if needed)
```

## Usage

Generate a TypeScript course on a subject like "React Hooks":

```bash
python3 main.py . . "React Hooks"
```

Specify a custom output file:

```bash
python3 main.py --output hooks-course.md "React Hooks"
```
