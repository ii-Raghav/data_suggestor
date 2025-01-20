import re
from typing import List
import nltk
from nltk.corpus import stopwords

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Define possible constraints
possible_constraints = {
    'O(1) access': ['O(1) access', 'constant time access', 'instant access'],
    'O(1) deletion': ['O(1) deletion', 'constant time deletion', 'quick deletion'],
    'O(log n) access': ['O(log n) access', 'logarithmic access', 'balanced access'],
    'O(log n) deletion': ['O(log n) deletion', 'logarithmic deletion'],
    'O(1) insertion': ['O(1) insertion', 'constant time insertion', 'quick insertion'],
    'O(log n) insertion': ['O(log n) insertion', 'logarithmic insertion', 'balanced insertion'],
    'O(n) insertion': ['O(n) insertion', 'linear insertion'],
    'O(n) deletion': ['O(n) deletion', 'linear deletion'],
    'O(1) search': ['O(1) search', 'constant time search', 'quick search'],
    'O(log n) search': ['O(log n) search', 'logarithmic search', 'binary search'],
    'O(n) search': ['O(n) search', 'linear search'],
    'fast_access': ['fast access', 'quick access', 'efficient access'],
    'fast_insertion': ['fast insertion', 'quick insertion', 'frequent insertion', 'high insertion speed'],
    'fast_deletion': ['fast deletion', 'quick deletion', 'frequent deletion', 'high deletion speed'],
    'balanced_insertion': ['balanced insertion', 'logarithmic insertion', 'O(log n) insertion'],
    'balanced_deletion': ['balanced deletion', 'logarithmic deletion', 'O(log n) deletion'],
    'fast_retrieval': ['fast retrieval', 'quick retrieval', 'efficient retrieval'],
    'fast_sorting': ['fast sorting', 'quick sorting', 'sorting speed'],
    'low_memory_usage': ['low memory', 'memory efficient', 'less memory', 'minimal memory', 'O(1) space'],
    'moderate_memory_usage': ['moderate memory', 'average memory usage'],
    'high_memory_usage': ['high memory', 'large memory', 'memory-intensive', 'high space complexity'],
    'ordered': ['ordered', 'sequence', 'sorted', 'sorted list', 'preserve order'],
    'unordered': ['unordered', 'random order', 'any order'],
    'LIFO': ['last in first out', 'LIFO', 'stack behavior'],
    'FIFO': ['first in first out', 'FIFO', 'queue behavior'],
    'key_value_store': ['key-value pairs', 'key-value store', 'hash map', 'dictionary'],
    'prefix_search': ['prefix search', 'autocomplete', 'prefix-based search'],
}

# Precompile regex for tokenization and load stopwords
TOKENIZER_REGEX = re.compile(r'\b\w+\b')
STOPWORDS = set(stopwords.words('english'))

# Precompiled patterns for constraint extraction
PRECOMPILED_PATTERNS = {
    constraint: [re.compile(r'\b' + re.escape(keyword) + r'\b', re.IGNORECASE) for keyword in keywords]
    for constraint, keywords in possible_constraints.items()
}

def tokenize_problem(problem: str) -> List[str]:
    tokens = TOKENIZER_REGEX.findall(problem.lower())
    return [token for token in tokens if token not in STOPWORDS]

def extract_constraints(tokens: List[str]) -> set:
    constraints = set()
    text = " ".join(tokens)

    # Debugging print statement
    print("Text to analyze for constraints:", text)

    # Iterate through precompiled patterns to find constraints
    for constraint, patterns in PRECOMPILED_PATTERNS.items():
        for pattern in patterns:
            if pattern.search(text):
                constraints.add(constraint)
                break  # Stop after the first matching pattern for efficiency

    # Debugging print to see which constraints are detected
    print("Extracted Constraints:", constraints)

    return constraints
