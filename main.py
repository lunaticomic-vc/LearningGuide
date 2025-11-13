import os

# Base path for your learning repository
BASE_DIR = "/Users/I742773/LearningGuide/Data Science & AI/LLMs & Foundation models"

structure = {
    "Transformer Architecture": [
        "Attention mechanism",
        "Positional encoding",
        "Encoder-decoder vs decoder-only",
        "Scaling laws"
    ],
    "Pretraining Foundations": [
        "Tokenization",
        "Pretraining objectives",
        "Data curation",
        "Transfer learning"
    ],
    "Fine-tuning and Adaptation Methods": [
        "Supervised fine-tuning SFT",
        "RLHF",
        "DPO and preference optimization",
        "LoRA and PEFT"
    ],
    "Embedding Models": [
        "Semantic embeddings",
        "Vector databases",
        "Similarity search applications"
    ],
    "Prompt Engineering and Conditioning": [
        "Instruction prompts",
        "Chain-of-thought",
        "Few-shot and zero-shot",
        "Context windows"
    ],
    "Evaluation and Metrics": [
        "Perplexity and text metrics",
        "Bias and robustness testing",
        "Hallucination evaluation"
    ],
    "Model Compression and Deployment": [
        "Quantization",
        "Pruning",
        "Distillation",
        "Inference optimization"
    ],
    "Interpretability and Safety": [
        "Attention visualization",
        "Attribution methods",
        "Red-teaming",
        "Safety mitigations"
    ],
    "Multimodal Foundation Models": [
        "Vision-language models",
        "Audio-language models",
        "Diffusion models"
    ],
    "Open-Source Ecosystem and Tools": [
        "Hugging Face",
        "LangChain and LlamaIndex",
        "Weights and Biases",
        "Licensing considerations"
    ]
}

# Create directories and markdown files
for topic, subtopics in structure.items():
    topic_dir = os.path.join(BASE_DIR, topic.replace(" ", "_"))
    os.makedirs(topic_dir, exist_ok=True)
    
    for subtopic in subtopics:
        sanitized = (
            subtopic.replace(" ", "_")
                    .replace("/", "_")
                    .replace("-", "_")
        )
        file_path = os.path.join(topic_dir, f"{sanitized}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(f"# {subtopic}\n\nNotes coming soon...\n")

print("Done.")
