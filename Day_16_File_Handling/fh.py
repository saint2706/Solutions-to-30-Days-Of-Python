"""Day 16: File Handling for Business Analytics

This module demonstrates various file handling operations commonly used in business:
- Text analysis and word counting
- JSON data processing for country/language analysis
- Email extraction from text files
- Document similarity analysis
- CSV data processing
- Text cleaning and preprocessing

Author: 30 Days of Python Course
Purpose: Educational examples for MBA students learning Python file operations
"""

import os
import json
import re
import csv
import math
import string
from collections import Counter
from typing import List, Dict, Tuple, Any, Optional, Union

# Import stop words with error handling
try:
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), "..", "data"))
    from stop_words import stop_words as sw
except ImportError:
    # Fallback if stop_words module is not available
    sw = [
        "the",
        "and",
        "or",
        "but",
        "in",
        "on",
        "at",
        "to",
        "for",
        "of",
        "with",
        "by",
        "is",
        "are",
        "was",
        "were",
    ]


def counter(fname: str) -> Tuple[int, int]:
    """Count words and lines in a text file.

    This function is useful for basic document analysis in business contexts,
    such as analyzing report lengths, email content volume, or document complexity.

    Args:
        fname (str): Path to the text file to analyze

    Returns:
        Tuple[int, int]: Number of words and number of lines

    Raises:
        FileNotFoundError: If the specified file doesn't exist
        IOError: If there's an error reading the file

    Example:
        >>> words, lines = counter("../data/obama_speech.txt")
        >>> print(f"Document contains {words} words in {lines} lines")
    """
    num_words = 0
    num_lines = 0

    try:
        with open(fname, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip(os.linesep)
                wordslist = line.split()
                num_lines += 1
                num_words += len(wordslist)

        print(f"Number of words in text file: {num_words}")
        print(f"Number of lines in text file: {num_lines}")
        return num_words, num_lines

    except FileNotFoundError:
        print(f"❌ Error: File '{fname}' not found")
        return 0, 0
    except IOError as e:
        print(f"❌ Error reading file '{fname}': {e}")
        return 0, 0


"""
# Example usage - uncomment to test:
print("Obama:")
counter(os.path.join("..", "data", "obama_speech.txt"))
print()
print("Michelle Obama:")
counter(os.path.join("..", "data", "michelle_obama_speech.txt"))
print()
print("Trump:")
counter(os.path.join("..", "data", "donald_speech.txt"))
print()
print("Melania Trump:")
counter(os.path.join("..", "data", "melina_trump_speech.txt"))
"""


def sort_dict_by_value(
    d: Dict[Any, Union[int, float]], reverse: bool = False
) -> Dict[Any, Union[int, float]]:
    """Sort a dictionary by its values.

    Useful for ranking business metrics, sorting sales data, or organizing
    any key-value data by importance/magnitude.

    Args:
        d (Dict): Dictionary to sort
        reverse (bool): If True, sort in descending order

    Returns:
        Dict: New dictionary sorted by values

    Example:
        >>> sales = {'Q1': 100000, 'Q2': 150000, 'Q3': 120000}
        >>> sorted_sales = sort_dict_by_value(sales, reverse=True)
        >>> # Returns {'Q2': 150000, 'Q3': 120000, 'Q1': 100000}
    """
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


def most_spoken_languages(fname: str, value: int) -> List[Tuple[int, str]]:
    """Analyze language frequency from country data JSON file.

    This function helps businesses understand language markets for
    internationalization and localization strategies.

    Args:
        fname (str): Path to JSON file containing country data
        value (int): Number of top languages to return

    Returns:
        List[Tuple[int, str]]: List of (count, language) tuples

    Example:
        >>> top_langs = most_spoken_languages("../data/countries_data.json", 5)
        >>> print(f"Top language: {top_langs[0][1]} spoken in {top_langs[0][0]} countries")
    """
    try:
        with open(fname, encoding="utf-8") as f:
            to_analyse = json.load(f)

        total_languages_initial = []
        counts = {}
        output_list = []

        # Extract all languages from all countries
        for country in to_analyse:
            if "languages" in country and isinstance(country["languages"], list):
                total_languages_initial.extend(country["languages"])

        # Count language frequencies
        for language in total_languages_initial:
            counts[language] = counts.get(language, 0) + 1

        # Sort by frequency (descending)
        counts = sort_dict_by_value(counts, True)

        # Get top N languages
        for item in list(counts.items())[:value]:
            output_list.append(item)

        # Return as (count, language) tuples for better readability
        return [(count, language) for language, count in output_list]

    except FileNotFoundError:
        print(f"❌ Error: File '{fname}' not found")
        return []
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON file '{fname}': {e}")
        return []
    except Exception as e:
        print(f"❌ Error processing language data: {e}")
        return []


def most_populated_countries(
    fname: str, value: int
) -> List[Dict[str, Union[str, int]]]:
    """Find the most populated countries from JSON data.

    Valuable for market sizing, demographic analysis, and identifying
    large consumer markets for business expansion planning.

    Args:
        fname (str): Path to JSON file containing country data
        value (int): Number of top countries to return

    Returns:
        List[Dict[str, Union[str, int]]]: List of country dictionaries with name and population

    Example:
        >>> top_countries = most_populated_countries("../data/countries_data.json", 3)
        >>> for country in top_countries:
        ...     print(f"{country['Country']}: {country['Population']:,} people")
    """
    try:
        with open(fname, encoding="utf-8") as f:
            list_data = json.load(f)

        populations = {}
        final = []

        # Extract population data
        for country in list_data:
            if "name" in country and "population" in country:
                populations[country["name"]] = country["population"]

        # Sort by population (descending)
        populations = sort_dict_by_value(populations, True)

        # Format results
        for country_name, population in list(populations.items())[:value]:
            final.append({"Country": country_name, "Population": population})

        return final

    except FileNotFoundError:
        print(f"❌ Error: File '{fname}' not found")
        return []
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON file '{fname}': {e}")
        return []
    except Exception as e:
        print(f"❌ Error processing population data: {e}")
        return []


# Example usage:
# print(most_spoken_languages(fname=os.path.join("..", "data", "countries_data.json"), value=3))
# print(most_populated_countries(fname=os.path.join("..", "data", "countries_data.json"), value=3))


def list_of_words(fname: str) -> List[str]:
    """Extract unique words from a text file.

    Useful for vocabulary analysis, content auditing, or preparing
    word lists for text processing tasks in business applications.

    Args:
        fname (str): Path to the text file

    Returns:
        List[str]: List of unique words found in the file

    Example:
        >>> unique_words = list_of_words("../data/email_exchanges.txt")
        >>> print(f"Document contains {len(unique_words)} unique words")
    """
    output = []
    try:
        with open(fname, "r", encoding="utf-8") as file:
            for line in file:
                for word in line.split():
                    output.append(word)
        return list(set(output))
    except FileNotFoundError:
        print(f"❌ Error: File '{fname}' not found")
        return []
    except IOError as e:
        print(f"❌ Error reading file '{fname}': {e}")
        return []


def check_email(word: str) -> bool:
    """Validate if a word is a valid email address.

    Essential for customer data validation, lead qualification,
    and contact information verification in business processes.

    Args:
        word (str): String to check for email format

    Returns:
        bool: True if valid email format, False otherwise

    Example:
        >>> check_email("user@company.com")
        True
        >>> check_email("invalid-email")
        False
    """
    email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    return bool(re.fullmatch(email_pattern, word))


def extract_emails(fname: str) -> List[str]:
    """Extract all email addresses from a text file.

    Critical for business applications like customer data mining,
    contact list building, and lead generation from documents.

    Args:
        fname (str): Path to the text file to scan for emails

    Returns:
        List[str]: List of valid email addresses found

    Example:
        >>> emails = extract_emails("../data/email_exchanges_big.txt")
        >>> print(f"Found {len(emails)} email addresses")
    """
    words = list_of_words(fname)
    email_list = []

    for word in words:
        if check_email(word):
            email_list.append(word)

    return email_list


# Example usage:
# print(extract_emails(os.path.join("..", "data", "email_exchanges_big.txt")))


def find_most_common_words(fname: str, value: int) -> List[Tuple[int, str]]:
    """Find the most frequently used words in a text file.

    Useful for content analysis, keyword extraction, brand mention tracking,
    and understanding communication patterns in business documents.

    Args:
        fname (str): Path to the text file to analyze
        value (int): Number of top words to return

    Returns:
        List[Tuple[int, str]]: List of (frequency, word) tuples

    Example:
        >>> common_words = find_most_common_words("../data/romeo_and_juliet.txt", 5)
        >>> for freq, word in common_words:
        ...     print(f"'{word}' appears {freq} times")
    """
    try:
        with open(fname, "r", encoding="utf-8") as file:
            text = file.read()

        split_words = text.split()
        word_counts = Counter(split_words)

        # Return as (frequency, word) tuples for better readability
        return [(count, word) for word, count in word_counts.most_common(value)]

    except FileNotFoundError:
        print(f"❌ Error: File '{fname}' not found")
        return []
    except IOError as e:
        print(f"❌ Error reading file '{fname}': {e}")
        return []


"""
# Example usage:
print(find_most_common_words(os.path.join("..", "data", "romeo_and_juliet.txt"), 10))
print(find_most_common_words(os.path.join("..", "data", "donald_speech.txt"), 10))
print(find_most_common_words(os.path.join("..", "data", "melina_trump_speech.txt"), 10))
print(find_most_common_words(os.path.join("..", "data", "michelle_obama_speech.txt"), 10))
print(find_most_common_words(os.path.join("..", "data", "obama_speech.txt"), 10))
"""


def clean_text(text: str) -> str:
    """Clean and normalize text for analysis.

    Essential preprocessing step for business text analytics, removing
    noise and standardizing format for consistent analysis results.

    Args:
        text (str): Raw text to clean

    Returns:
        str: Cleaned and normalized text

    Example:
        >>> raw_text = "Check out https://example.com! Contact us at info@company.com."
        >>> clean_text = clean_text(raw_text)
        >>> # Returns cleaned version without URLs and punctuation
    """
    # Convert to lowercase for consistency
    text = text.lower()

    # Remove content in square brackets (often metadata)
    text = re.sub(r"\[.*?\]", "", text)

    # Remove URLs and web addresses
    text = re.sub(r"https?://\S+|www\.\S+", "", text)

    # Remove HTML tags
    text = re.sub(r"<.*?>+", "", text)

    # Remove punctuation
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)

    # Remove newlines
    text = re.sub(r"\n", "", text)

    # Remove words containing digits
    text = re.sub(r"\w*\d\w*", "", text)

    return text


def remove_support_words(text: str) -> List[str]:
    """Remove stop words from text for better content analysis.

    Stop word removal focuses analysis on meaningful business terms
    rather than common language words like 'the', 'and', 'is'.

    Args:
        text (str): Text to process

    Returns:
        List[str]: List of words with stop words removed

    Example:
        >>> text = "The company is growing and expanding rapidly"
        >>> meaningful_words = remove_support_words(text)
        >>> # Returns ['company', 'growing', 'expanding', 'rapidly']
    """
    return [word for word in text.split() if word not in sw]


def read_file(fname: str) -> List[str]:
    """Read and preprocess a text file for analysis.

    Combines file reading, text cleaning, and stop word removal
    for streamlined text preprocessing in business analytics.

    Args:
        fname (str): Path to the text file

    Returns:
        List[str]: List of processed words ready for analysis

    Example:
        >>> processed_words = read_file("../data/business_report.txt")
        >>> print(f"Processed {len(processed_words)} meaningful words")
    """
    try:
        with open(fname, "r", encoding="utf-8") as f:
            data = remove_support_words(clean_text(f.read()))
        return data
    except FileNotFoundError:
        print(f"❌ Error: File '{fname}' not found")
        return []
    except IOError as e:
        print(f"❌ Error opening or reading input file '{fname}': {e}")
        return []


def count_frequency(word_list: List[str]) -> Dict[str, int]:
    """Count frequency of words in a list.

    Essential for text analytics, helping identify key themes,
    brand mentions, and communication patterns in business documents.

    Args:
        word_list (List[str]): List of words to count

    Returns:
        Dict[str, int]: Dictionary mapping words to their frequencies

    Example:
        >>> words = ['sales', 'revenue', 'sales', 'profit', 'sales']
        >>> frequencies = count_frequency(words)
        >>> # Returns {'sales': 3, 'revenue': 1, 'profit': 1}
    """
    frequency_dict = {}

    for word in word_list:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict


def word_frequencies_for_file(filename: str) -> Dict[str, int]:
    """Calculate word frequencies for a file after preprocessing.

    Combines reading, cleaning, and frequency analysis for comprehensive
    text analytics suitable for business document analysis.

    Args:
        filename (str): Path to the text file

    Returns:
        Dict[str, int]: Word frequency mapping

    Example:
        >>> freq_map = word_frequencies_for_file("../data/business_plan.txt")
        >>> print(f"File contains {len(freq_map)} distinct meaningful words")
    """
    word_list = read_file(filename)
    if not word_list:
        return {}

    freq_mapping = count_frequency(word_list)

    print(f"File {filename}:")
    print(f"{len(freq_mapping)} distinct words")

    return freq_mapping


def dot_product(d1: Dict[str, int], d2: Dict[str, int]) -> float:
    """Calculate dot product of two word frequency dictionaries.

    Mathematical foundation for document similarity analysis,
    used in business applications like document clustering,
    plagiarism detection, and content similarity scoring.

    Args:
        d1 (Dict[str, int]): First word frequency dictionary
        d2 (Dict[str, int]): Second word frequency dictionary

    Returns:
        float: Dot product value
    """
    total = 0.0

    for key in d1:
        if key in d2:
            total += d1[key] * d2[key]

    return total


def vector_angle(d1: Dict[str, int], d2: Dict[str, int]) -> float:
    """Calculate angle between two word frequency vectors.

    Measures document similarity using cosine similarity principles.
    Smaller angles indicate more similar documents, useful for
    content classification and duplicate detection in business.

    Args:
        d1 (Dict[str, int]): First word frequency dictionary
        d2 (Dict[str, int]): Second word frequency dictionary

    Returns:
        float: Angle in radians between the two vectors

    Raises:
        ValueError: If vectors have zero magnitude
    """
    numerator = dot_product(d1, d2)
    denominator = math.sqrt(dot_product(d1, d1) * dot_product(d2, d2))

    if denominator == 0:
        raise ValueError(
            "Cannot calculate angle: one or both documents have no valid words"
        )

    return math.acos(numerator / denominator)


def document_similarity(filename_1: str, filename_2: str) -> Optional[float]:
    """Calculate similarity between two text documents.

    Critical for business applications like:
    - Contract comparison and analysis
    - Plagiarism detection in reports
    - Content deduplication
    - Document clustering and organization

    Args:
        filename_1 (str): Path to first document
        filename_2 (str): Path to second document

    Returns:
        Optional[float]: Similarity angle in degrees (0-90), or None if error

    Example:
        >>> similarity = document_similarity("doc1.txt", "doc2.txt")
        >>> if similarity is not None:
        ...     print(f"Documents are {90-similarity:.1f}% similar")
    """
    try:
        word_freq_1 = word_frequencies_for_file(filename_1)
        word_freq_2 = word_frequencies_for_file(filename_2)

        if not word_freq_1 or not word_freq_2:
            print("❌ Error: One or both files could not be processed")
            return None

        angle_radians = vector_angle(word_freq_1, word_freq_2)
        distance_degrees = (angle_radians * 180) / math.pi

        print(f"📊 Document similarity analysis:")
        print(f"   Angle between documents: {distance_degrees:.2f} degrees")
        print(
            f"   Similarity score: {90 - distance_degrees:.1f}% (higher = more similar)"
        )

        return distance_degrees

    except ValueError as e:
        print(f"❌ Error calculating similarity: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error in similarity calculation: {e}")
        return None


# Example usage:
# document_similarity(
#     os.path.join("..", "data", "michelle_obama_speech.txt"),
#     os.path.join("..", "data", "melina_trump_speech.txt")
# )


def analyze_technology_mentions(fname: str) -> Dict[str, int]:
    """Analyze technology mentions in CSV data.

    Useful for market research, trend analysis, and understanding
    technology adoption patterns in business datasets.

    Args:
        fname (str): Path to CSV file to analyze

    Returns:
        Dict[str, int]: Dictionary with counts for different technologies

    Example:
        >>> tech_counts = analyze_technology_mentions("../data/hacker_news.csv")
        >>> print(f"Python mentioned {tech_counts['Python']} times")
    """
    try:
        counts = {"Python": 0, "JavaScript": 0, "Java": 0}

        with open(fname, mode="r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)

            for line in csv_reader:
                line_text = " ".join(
                    line
                ).lower()  # Convert to lowercase for consistent matching

                # Count Python mentions
                if "python" in line_text:
                    counts["Python"] += 1

                # Count JavaScript mentions (various spellings)
                if any(
                    js_variant in line_text
                    for js_variant in ["javascript", "java script"]
                ):
                    counts["JavaScript"] += 1

                # Count Java mentions (but not JavaScript)
                if (
                    "java" in line_text
                    and "javascript" not in line_text
                    and "java script" not in line_text
                ):
                    counts["Java"] += 1

        print(f"📊 Technology Mention Analysis:")
        print(f"   Python: {counts['Python']} mentions")
        print(f"   JavaScript: {counts['JavaScript']} mentions")
        print(f"   Java: {counts['Java']} mentions")

        return counts

    except FileNotFoundError:
        print(f"❌ Error: File '{fname}' not found")
        return {"Python": 0, "JavaScript": 0, "Java": 0}
    except Exception as e:
        print(f"❌ Error analyzing technology mentions: {e}")
        return {"Python": 0, "JavaScript": 0, "Java": 0}


# Example usage:
# analyze_technology_mentions(os.path.join("..", "data", "hacker_news.csv"))


def main():
    """Main function to demonstrate file handling capabilities."""
    print("🗂️  Day 16: File Handling for Business Analytics")
    print("📊 Demonstration of various file processing techniques")
    print("=" * 60)

    # Example: Analyze document word counts
    print("\n📄 Document Analysis Example:")
    try:
        data_dir = os.path.join("..", "data")
        speech_file = os.path.join(data_dir, "obama_speech.txt")
        if os.path.exists(speech_file):
            words, lines = counter(speech_file)
            print(f"✅ Successfully analyzed document: {words} words, {lines} lines")
        else:
            print("ℹ️  Sample speech file not found - skipping word count demo")
    except Exception as e:
        print(f"❌ Error in document analysis: {e}")

    print("\n✨ All file handling functions are ready for use!")
    print("💡 Tip: Uncomment example calls throughout the file to test functionality")


if __name__ == "__main__":
    main()
