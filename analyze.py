import re
from collections import Counter
from matplotlib import pyplot

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

def analyzeMonograms(filepath, top_n=20):
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()
    tokens = tokenize(clean(raw))
    filtered = [w for w in tokens if w not in STOPWORDS]
    counts = Counter(filtered)
    words, freqs = zip(*counts.most_common(top_n))

    plt = pyplot
    plt.figure(figsize=(10, 5))
    plt.title("Top 20 words")
    plt.bar(words, freqs, color="steelblue")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

def analyzeBigrams(filepath, top_n=20):
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()
    tokens = tokenize(clean(raw))
    filtered = [w for w in tokens if w not in STOPWORDS]
    bigrams = list(zip(filtered, filtered[1:]))
    counts = Counter(bigrams)
    words, freqs = zip(*counts.most_common(top_n))
    pairs = [" ".join(w) for w in words]

    plt = pyplot
    plt.figure(figsize=(10, 5))
    plt.title("Top 20 bigrams (word pairs)")
    plt.bar(pairs, freqs, color="steelblue")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

analyzeMonograms("frankenstein.txt")
analyzeBigrams("frankenstein.txt")