import re
from collections import Counter
from matplotlib import pyplot
import argparse


# List of words that do not need to be count
STOPWORDS = {
    "the","a","an","and","or","but","in","on",
    "at","to","of","for","is","was","it","that",
    "this","with","he","she","i","you","we","they"
}


# Helper functions
def tokenize(text):
    return text.split()

def clean(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text

def wordsAndFreqs(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()
    tokens = tokenize(clean(raw))
    filtered = [w for w in tokens if w not in STOPWORDS]
    counts = Counter(filtered)

    return counts, len(filtered)

def bigramsAndFreqs(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        raw = f.read()
    tokens = tokenize(clean(raw))
    filtered = [w for w in tokens if w not in STOPWORDS]
    bigrams = list(zip(filtered, filtered[1:]))
    counts = Counter(bigrams)

    return counts, len(bigrams)


# Function for analyzing a books monograms
def analyzeWords(filepath, top_n=20):
    counter, total = wordsAndFreqs(filepath)
    words, freqs = zip(*counter.most_common(top_n))

    plt = pyplot
    plt.figure(figsize=(10, 5))
    plt.title(f"Top {top_n} Words in {filepath}")
    plt.bar(words, freqs, color="steelblue")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# Function for analyzing a books bigrams
def analyzeBigrams(filepath, top_n=20):
    counts, total = bigramsAndFreqs(filepath)
    words, freqs = zip(*counts.most_common(top_n))
    pairs = [" ".join(w) for w in words]

    plt = pyplot
    plt.figure(figsize=(10, 5))
    plt.title(f"Top {top_n} Bigrams (word pairs) in {filepath}")
    plt.bar(pairs, freqs, color="steelblue")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()


# Function for comparing two books top unique words
def compareTopUniqueWords(filepathA, filepathB, top_n=10):
    counter_a, total_a = wordsAndFreqs(filepathA)
    counter_b, total_b = wordsAndFreqs(filepathB)
    
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

    plt = pyplot
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
def compareTopCommonWords(filepathA, filepathB, top_n=10):
    counter_a, total_a = wordsAndFreqs(filepathA)
    counter_b, total_b = wordsAndFreqs(filepathB)
    
    words_set_a = set(counter_a.keys())
    words_set_b = set(counter_b.keys())
    
    common_for_a_and_b = words_set_a & words_set_b
    
    common_counter_a = {word: counter_a[word] for word in common_for_a_and_b}
    top_common_a = sorted(common_counter_a.items(), key=lambda x: x[1], reverse=True)[:top_n]
    common_counter_b = {word: counter_b[word] for word in common_for_a_and_b}
    top_common_b = sorted(common_counter_b.items(), key=lambda x: x[1], reverse=True)[:top_n]

    words_a, freqs_a = zip(*top_common_a)
    words_b, freqs_b = zip(*top_common_b)

    plt = pyplot
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
def compareTopUniqueBigrams(filepathA, filepathB, top_n=10):
    counter_a, total_a = bigramsAndFreqs(filepathA)
    counter_b, total_b = bigramsAndFreqs(filepathB)

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

    plt = pyplot
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
def compareTopCommonBigrams(filepathA, filepathB, top_n=10):
    counter_a, total_a = bigramsAndFreqs(filepathA)
    counter_b, total_b = bigramsAndFreqs(filepathB)
    
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

    plt = pyplot
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
        analyzeWords(args.filepath, top_n=args.number)
    elif args.function == "bigrams":
        analyzeBigrams(args.filepath, top_n=args.number)
    elif args.function == "compare-unique-words":
        compareTopUniqueWords(args.filepath, args.filepath2, top_n=args.number)
    elif args.function == "compare-common-words":
        compareTopCommonWords(args.filepath, args.filepath2, top_n=args.number)
    elif args.function == "compare-unique-bigrams":
        compareTopUniqueBigrams(args.filepath, args.filepath2, top_n=args.number)
    elif args.function == "compare-common-bigrams":
        compareTopCommonBigrams(args.filepath, args.filepath2, top_n=args.number)