# WordFrequencyAnalyzer
A Python text analysis tool for extracting and comparing word frequencies, bigrams, and linguistic patterns in text files.


## Features
- **Word Frequency Analysis**: Identify and visualize the most frequent words in a text
- **Bigram Analysis**: Analyze word pair frequencies to identify common phrases
- **Text Comparison**: Compare two texts to find unique and common words/bigrams
- **Stopword Filtering**: Remove common words to focus on meaningful content
- **Visualization**: Generate bar charts for easy pattern identification


## Installation
Requires Python 3.6+ with the following dependencies:

```bash
pip install matplotlib
```

### Quick Start
```bash
# Analyze word frequencies in a text file (top 10 by default)
python analyze.py frankenstein.txt

# Analyze top 15 words
python analyze.py frankenstein.txt -n 15

# Compare two texts
python analyze.py frankenstein.txt romeoAndJuliet.txt --function compare-common-words
```


## Usage
### Command-Line Interface
```bash
python analyze.py <filepath> [filepath2] [--function <function_name>] [-n <number>]
```

### Options
- `filepath`: Path to the first text file to analyze (required)
- `filepath2`: Path to a second file for comparison functions (optional)
- `--number, -n`: Number of top items to display (default: 10)
- `--function, -f`: Analysis function to run (default: words)

### Available Functions
#### Single-File Analysis
**`words`** (default) - Analyze top 10 most frequent words
```bash
python analyze.py frankenstein.txt
```

Analyze top 20 words:
```bash
python analyze.py frankenstein.txt -n 20
```

**`bigrams`** - Analyze top 10 most frequent word pairs
```bash
python analyze.py frankenstein.txt --function bigrams
```

Analyze top 15 bigrams:
```bash
python analyze.py frankenstein.txt -f bigrams -n 15
```

#### Comparison Analysis (requires two files)
**`compare-unique-words`** - Compare unique words between two texts
```bash
python analyze.py frankenstein.txt romeoAndJuliet.txt --function compare-unique-words
```

**`compare-common-words`** - Compare common words between two texts
```bash
python analyze.py frankenstein.txt romeoAndJuliet.txt -f compare-common-words
```

**`compare-unique-bigrams`** - Compare unique bigrams (word pairs) between two texts
```bash
python analyze.py frankenstein.txt romeoAndJuliet.txt --function compare-unique-bigrams -n 15
```

**`compare-common-bigrams`** - Compare common bigrams (word pairs) between two texts
```bash
python analyze.py frankenstein.txt romeoAndJuliet.txt -f compare-common-bigrams -n 20
```


## How It Works
### Text Processing Pipeline
1. **Reading**: Opens and reads the entire text file
2. **Tokenization**: Splits text into individual words
3. **Cleaning**: Converts to lowercase and removes non-alphabetic characters
4. **Filtering**: Removes stopwords (common words like "the", "and", "is")
5. **Counting**: Tallies word/bigram frequencies using `Counter`
6. **Visualization**: Generates bar charts of top frequencies

### Stopwords
The tool filters these words by default:
```python
the, a, an, and, or, but, in, on, at, to, of, for, is, was, it, that, this, with, he, she, i, you, we, they
```

To modify stopwords, edit the `STOPWORDS` set in `analyze.py`.


## Function Reference
### Core Functions
- `tokenize(text)` - Splits text into words
- `clean(text)` - Converts to lowercase and removes punctuation
- `wordsAndFreqs(filepath)` - Returns word frequency counter and total word count
- `bigramsAndFreqs(filepath)` - Returns bigram frequency counter and total bigram count

### Analysis Functions
- `analyze_words(filepath, top_n=20)` - Display word frequency bar chart (default top_n: 20)
- `analyze_bigrams(filepath, top_n=20)` - Display bigram frequency bar chart (default top_n: 20)
- `compare_top_unique_words(filepathA, filepathB, top_n=10)` - Side-by-side unique words comparison (default top_n: 10)
- `compare_top_common_words(filepathA, filepathB, top_n=10)` - Side-by-side common words comparison (default top_n: 10)
- `compare_top_unique_bigrams(filepathA, filepathB, top_n=10)` - Side-by-side unique bigrams comparison (default top_n: 10)
- `compare_top_common_bigrams(filepathA, filepathB, top_n=10)` - Side-by-side common bigrams comparison (default top_n: 10)

**Note**: The `-n` or `--number` command-line flag overrides function defaults.


## Examples
### Analyze Frankenstein (top 10 words, default)
```bash
python analyze.py frankenstein.txt
```

### Analyze top 25 words in Frankenstein
```bash
python analyze.py frankenstein.txt -n 25
```

### Find common words between two texts
```bash
python analyze.py frankenstein.txt romeoAndJuliet.txt --function compare-common-words
```

### Analyze top 20 bigrams
```bash
python analyze.py romeoAndJuliet.txt --function bigrams -n 20
```

### Compare unique bigrams between texts (top 15)
```bash
python analyze.py frankenstein.txt romeoAndJuliet.txt -f compare-unique-bigrams -n 15
```


## Output
- **Word/Bigram Analysis**: Interactive matplotlib bar chart with top frequencies
- **Comparison Analysis**: Two side-by-side bar charts for visual comparison
- Charts are displayed in a window that allows zoom, pan, and save operations


## Notes
- All analysis is case-insensitive
- Non-alphabetic characters (punctuation, numbers) are removed
- The tool processes entire files into memory; very large files may require significant RAM
- Charts can be saved from the matplotlib interface using the Save icon
- Command-line flags can be used in any order after the filepath arguments
- Short forms: `-n` for `--number`, `-f` for `--function`