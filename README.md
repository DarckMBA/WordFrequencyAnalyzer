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


## Usage
### Command-Line Interface
```bash
python analyze.py <filepath> [filepath2] --function <function_name>
```

### Available Functions
#### Single-File Analysis
**`words`** (default) - Analyze top 20 most frequent words
```bash
python analyze.py frankenstein.txt
```

**`bigrams`** - Analyze top 20 most frequent word pairs
```bash
python analyze.py frankenstein.txt --function bigrams
```

#### Comparison Analysis (requires two files)
**`compare-unique-words`** - Compare unique words between two texts
```bash
python analyze.py frankenstein.txt romeoAndJuliet.txt --function compare-unique-words
```

**`compare-common-words`** - Compare common words between two texts
```bash
python analyze.py frankenstein.txt romeoAndJuliet.txt --function compare-common-words
```

**`compare-unique-bigrams`** - Compare unique bigrams (word pairs) between two texts
```bash
python analyze.py frankenstein.txt romeoAndJuliet.txt --function compare-unique-bigrams
```

**`compare-common-bigrams`** - Compare common bigrams (word pairs) between two texts
```bash
python analyze.py frankenstein.txt romeoAndJuliet.txt --function compare-common-bigrams
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
- `analyzeWords(filepath, top_n=20)` - Display word frequency bar chart
- `analyzeBigrams(filepath, top_n=20)` - Display bigram frequency bar chart
- `compareTopUniqueWords(filepathA, filepathB, top_n=10)` - Side-by-side unique words comparison
- `compareTopCommonWords(filepathA, filepathB, top_n=10)` - Side-by-side common words comparison
- `compareTopUniqueBigrams(filepathA, filepathB, top_n=10)` - Side-by-side unique bigrams comparison
- `compareTopCommonBigrams(filepathA, filepathB, top_n=10)` - Side-by-side common bigrams comparison


## Examples
### Analyze Frankenstein
```bash
python analyze.py frankenstein.txt
```

### Find common words between two texts
```bash
python analyze.py frankenstein.txt romeoAndJuliet.txt --function compare-common-words
```

### Analyze top 20 bigrams
```bash
python analyze.py romeoAndJuliet.txt --function bigrams
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