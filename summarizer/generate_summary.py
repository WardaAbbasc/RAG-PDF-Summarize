import subprocess

def summarize_with_mistral(prompt):
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt,
        capture_output=True,
        text=True,
        encoding='utf-8'  # 🔥 Fix here!
    )
    return result.stdout
