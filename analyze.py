import re
from collections import Counter
from matplotlib import pyplot as plt
import argparse


# List of words that do not need to be count
STOPWORDS = {
    'i', 'me', 'my', 'myself', 'we', 'our', 'ours',
    'you', 'your', 'yours', 'he', 'him', 'his', 'she',
    'her', 'it', 'its', 'they', 'them', 'what', 'which',
    'who', 'this', 'that', 'am', 'is', 'are', 'was',
    'were', 'be', 'have', 'has', 'had', 'do', 'does',
    'did', 'a', 'an', 'the', 'and', 'but', 'if', 'or',
    'because', 'as', 'until', 'while', 'of', 'at', 'by',
    'for', 'with', 'about', 'against', 'between', 'into',
    'through', 'during', 'before', 'after', 'above',
    'below', 'to', 'from', 'up', 'down', 'in', 'out',
    'on', 'off', 'over', 'under', 'again', 'further',
    'then', 'once', 'here', 'there', 'when', 'where',
    'why', 'how', 'all', 'any', 'both', 'each', 'few',
    'more', 'most', 'other', 'some', 'such', 'no', 'nor',
    'not', 'only', 'own', 'same', 'so', 'than', 'too',
    'very', 'can', 'will', 'just', 'should', 'now'
}


# Helper functions
def tokenize(text):
    return text.split()

def clean(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text

def words_and_freqs(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()
    tokens = tokenize(clean(raw))
    filtered = [w for w in tokens if w not in STOPWORDS]
    counts = Counter(filtered)

    return counts, len(filtered)

def bigrams_and_freqs(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()
    tokens = tokenize(clean(raw))
    filtered = [w for w in tokens if w not in STOPWORDS]
    bigrams = list(zip(filtered, filtered[1:]))
    counts = Counter(bigrams)

    return counts, len(bigrams)


# Function for analyzing a books monograms
def analyze_words(filepath, top_n=20):
    counter, total = words_and_freqs(filepath)
    words, freqs = zip(*counter.most_common(top_n))

    plt.figure(figsize=(10, 5))
    plt.title(f"Top {top_n} Words in {filepath}")
    plt.bar(words, freqs, color="steelblue")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# Function for analyzing a books bigrams
def analyze_bigrams(filepath, top_n=20):
    counts, total = bigrams_and_freqs(filepath)
    words, freqs = zip(*counts.most_common(top_n))
    pairs = [" ".join(w) for w in words]

    plt.figure(figsize=(10, 5))
    plt.title(f"Top {top_n} Bigrams (word pairs) in {filepath}")
    plt.bar(pairs, freqs, color="steelblue")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# Function for comparing two books top unique words
def compare_top_unique_words(filepathA, filepathB, top_n=10):
    counter_a, total_a = words_and_freqs(filepathA)
    counter_b, total_b = words_and_freqs(filepathB)
    
    words_set_a = set(counter_a.keys())
    words_set_b = set(counter_b.keys())
    
    unique_to_a = words_set_a - words_set_b
    unique_to_b = words_set_b - words_set_a
    
    unique_counter_a = {word: counter_a[word] for word in unique_to_a}
    top_unique_a = sorted(unique_counter_a.items(), key=lambda x: x[1], reverse=True)[:top_n]
    unique_counter_b = {word: counter_b[word] for word in unique_to_b}
    top_unique_b = sorted(unique_counter_b.items(), key=lambda x: x[1], reverse=True)[:top_n]

    words_a, freqs_a = zip(*top_unique_a)
    words_b, freqs_b = zip(*top_unique_b)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.bar(words_a, freqs_a, color="steelblue")
    plt.title(f"Top {top_n} Unique Words in {filepathA}")
    plt.xticks(rotation=45, ha="right")
    
    plt.subplot(1, 2, 2)
    plt.bar(words_b, freqs_b, color="indianred")
    plt.title(f"Top {top_n} Unique Words in {filepathB}")
    plt.xticks(rotation=45, ha="right")
    
    plt.tight_layout()
    plt.show()


# Function for comparing two books top common words
def compare_top_common_words(filepathA, filepathB, top_n=10):
    counter_a, total_a = words_and_freqs(filepathA)
    counter_b, total_b = words_and_freqs(filepathB)
    
    words_set_a = set(counter_a.keys())
    words_set_b = set(counter_b.keys())
    
    common_for_a_and_b = words_set_a & words_set_b
    
    common_counter_a = {word: counter_a[word] for word in common_for_a_and_b}
    top_common_a = sorted(common_counter_a.items(), key=lambda x: x[1], reverse=True)[:top_n]
    common_counter_b = {word: counter_b[word] for word in common_for_a_and_b}
    top_common_b = sorted(common_counter_b.items(), key=lambda x: x[1], reverse=True)[:top_n]

    words_a, freqs_a = zip(*top_common_a)
    words_b, freqs_b = zip(*top_common_b)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.bar(words_a, freqs_a, color="steelblue")
    plt.title(f"Top {top_n} Common Words in {filepathA}")
    plt.xticks(rotation=45, ha="right")
    
    plt.subplot(1, 2, 2)
    plt.bar(words_b, freqs_b, color="indianred")
    plt.title(f"Top {top_n} Common Words in {filepathB}")
    plt.xticks(rotation=45, ha="right")
    
    plt.tight_layout()
    plt.show()


# Function for comparing two books top unique bigrams
def compare_top_unique_bigrams(filepathA, filepathB, top_n=10):
    counter_a, total_a = bigrams_and_freqs(filepathA)
    counter_b, total_b = bigrams_and_freqs(filepathB)

    words_set_a = set(counter_a.keys())
    words_set_b = set(counter_b.keys())

    unique_to_a = words_set_a - words_set_b
    unique_to_b = words_set_b - words_set_a

    unique_counter_a = {word: counter_a[word] for word in unique_to_a}
    top_unique_a = sorted(unique_counter_a.items(), key=lambda x: x[1], reverse=True)[:top_n]
    unique_counter_b = {word: counter_b[word] for word in unique_to_b}
    top_unique_b = sorted(unique_counter_b.items(), key=lambda x: x[1], reverse=True)[:top_n]

    words_a, freqs_a = zip(*top_unique_a)
    words_b, freqs_b = zip(*top_unique_b)

    pairs_a = [" ".join(w) for w in words_a]
    pairs_b = [" ".join(w) for w in words_b]

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.bar(pairs_a, freqs_a, color="steelblue")
    plt.title(f"Top {top_n} Unique Bigrams in {filepathA}")
    plt.xticks(rotation=45, ha="right")
    
    plt.subplot(1, 2, 2)
    plt.bar(pairs_b, freqs_b, color="indianred")
    plt.title(f"Top {top_n} Unique Bigrams in {filepathB}")
    plt.xticks(rotation=45, ha="right")
    
    plt.tight_layout()
    plt.show()


# Function for comparing two books top common words
def compare_top_common_bigrams(filepathA, filepathB, top_n=10):
    counter_a, total_a = bigrams_and_freqs(filepathA)
    counter_b, total_b = bigrams_and_freqs(filepathB)
    
    words_set_a = set(counter_a.keys())
    words_set_b = set(counter_b.keys())
    
    common_for_a_and_b = words_set_a & words_set_b
    
    common_counter_a = {word: counter_a[word] for word in common_for_a_and_b}
    top_common_a = sorted(common_counter_a.items(), key=lambda x: x[1], reverse=True)[:top_n]
    common_counter_b = {word: counter_b[word] for word in common_for_a_and_b}
    top_common_b = sorted(common_counter_b.items(), key=lambda x: x[1], reverse=True)[:top_n]

    words_a, freqs_a = zip(*top_common_a)
    words_b, freqs_b = zip(*top_common_b)

    pairs_a = [" ".join(w) for w in words_a]
    pairs_b = [" ".join(w) for w in words_b]

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.bar(pairs_a, freqs_a, color="steelblue")
    plt.title(f"Top {top_n} Common Bigrams in {filepathA}")
    plt.xticks(rotation=45, ha="right")
    
    plt.subplot(1, 2, 2)
    plt.bar(pairs_b, freqs_b, color="indianred")
    plt.title(f"Top {top_n} Common Bigrams in {filepathB}")
    plt.xticks(rotation=45, ha="right")
    
    plt.tight_layout()
    plt.show()


# Command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze word frequencies in text files")
    parser.add_argument("filepath", help="Path to the text file to analyze")
    parser.add_argument("filepath2", nargs="?", help="Second file for comparison functions")
    parser.add_argument("--number", "-n", type=int, default=10, help="Number of words/bigrams to analyze (default: 10)")
    parser.add_argument("--function", "-f", choices=["words", "bigrams", "compare-unique-words", 
                                                "compare-common-words", "compare-unique-bigrams", 
                                                "compare-common-bigrams"],
                        default="words", help="Analysis function to run")
    
    args = parser.parse_args()
    
    if args.function == "words":
        analyze_words(args.filepath, top_n=args.number)
    elif args.function == "bigrams":
        analyze_bigrams(args.filepath, top_n=args.number)
    elif args.function == "compare-unique-words":
        compare_top_unique_words(args.filepath, args.filepath2, top_n=args.number)
    elif args.function == "compare-common-words":
        compare_top_common_words(args.filepath, args.filepath2, top_n=args.number)
    elif args.function == "compare-unique-bigrams":
        compare_top_unique_bigrams(args.filepath, args.filepath2, top_n=args.number)
    elif args.function == "compare-common-bigrams":
        compare_top_common_bigrams(args.filepath, args.filepath2, top_n=args.number)