import re
import sys
import io
from collections import Counter

# Configure UTF-8 encoding for console output on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

STOPWORDS = {
    "the","a","an","and","or","but","in","on",
    "at","to","of","for","is","was","it","that",
    "this","with","he","she","i","you","we","they"
}

def clean(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text

def tokenize(text):
    return text.split()

def analyze(filepath, top_n=20):
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()
    tokens = tokenize(clean(raw))
    filtered = [w for w in tokens if w not in STOPWORDS]
    counts = Counter(filtered)
    print(f"\nTop {top_n} words:\n")
    for word, freq in counts.most_common(top_n):
        bar = "█" * (freq // 50)
        print(f"  {word:<15} {freq:>5}  {bar}")

analyze("frankenstein.txt")