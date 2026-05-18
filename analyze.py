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

def analyze(filepath, top_n=20):
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()
    tokens = tokenize(clean(raw))
    filtered = [w for w in tokens if w not in STOPWORDS]
    counts = Counter(filtered)

    plt = pyplot
    words, freqs = zip(*counts.most_common(top_n))

    plt.bar(words, freqs)
    plt.show()

analyze("frankenstein.txt")