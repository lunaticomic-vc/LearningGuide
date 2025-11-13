import os
from pathlib import Path
from openai import OpenAI

# 1. CONFIGURATION
BASE_DIR = Path("/Users/I742773/LearningGuide")  # change if needed
MODEL_NAME = "gpt-4.1-mini"  # or "gpt-4.1" / "gpt-4.1-pro" if you prefer

PROMPT_TEMPLATE = """
You will create a structured learning document in Markdown for the topic "{title}".
Audience: student professional
Goal: deep, practical understanding using evidence-based learning methods
Language: Bulgarian
Tone: like a Stanford professor teaching advanced undergraduates or early graduate students.

Use exactly the following section headings in English:

# {title}

## 1. Activate Prior Knowledge
Ask 2–3 questions that help the learner recall, connect, or predict what the topic involves, especially in the context of AI systems or software engineering.

## 2. Overview
Write 2–4 short paragraphs that build a clear conceptual model.
Explain the purpose, where it fits in a broader system, and why it matters.

## 3. Key Concepts
List essential terms. Format each bullet as:
Term – 1–3 precise and accessible sentences.
Include simple analogies or mental models when useful.

## 4. Step-by-step Learning Path
Provide a numbered list. Each step must include:
- what to focus on
- a small practical task
- 1–2 retrieval questions
Tasks should reflect real engineering practice when relevant.

## 5. Examples
Give 2–3 concrete examples demonstrating the topic in practice.
If appropriate, include short code snippets inside ```language blocks.

## 6. Common Pitfalls
List typical misunderstandings or implementation mistakes and how to avoid them.

## 7. Short Retrieval Quiz
Provide 5–7 short questions answerable from memory.

## 8. Quick Recap
Summarize the core ideas in 5–7 bullet points.

## 9. Spaced Review Plan
Add a small table with review prompts for:
- 1 day
- 3 days
- 1 week
- 1 month

Do not include meta commentary about being an AI model.
"""

TARGET_SUBSTRING = "Notes coming soon..."

# Uses OPENAI_API_KEY from environment
client = OpenAI()


def extract_title_from_filename(path: Path) -> str:
    # "Persistent_and_immutable_structures.md" -> "Persistent_and_immutable_structures"
    return path.stem


def build_prompt(title: str) -> str:
    return PROMPT_TEMPLATE.format(title=title)


def generate_markdown_for_title(title: str) -> str:
    prompt = build_prompt(title)

    resp = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You write focused, comprehensive, exhaustive student-friendly technical study guides in Markdown.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.3,
    )

    return resp.choices[0].message.content


def process_markdown_file(path: Path, dry_run: bool = False):
    content = path.read_text(encoding="utf-8")

    # Only process files containing the target substring anywhere
    if TARGET_SUBSTRING not in content:
        print(f"Skipping file (substring not found): {path}")
        return

    title = extract_title_from_filename(path)
    print(f"Processing: {path} (title: {title})")

    new_content = generate_markdown_for_title(title)

    if dry_run:
        print(f"[DRY RUN] Would overwrite {path}")
        return

    path.write_text(new_content, encoding="utf-8")
    print(f"Updated: {path}")


def iterate_all_markdown_files(base_dir: Path, dry_run: bool = False):
    for root, _, files in os.walk(base_dir):
        for fname in files:
            if fname.lower().endswith(".md"):
                process_markdown_file(Path(root) / fname, dry_run=dry_run)


if __name__ == "__main__":
    iterate_all_markdown_files(BASE_DIR, dry_run=False)
