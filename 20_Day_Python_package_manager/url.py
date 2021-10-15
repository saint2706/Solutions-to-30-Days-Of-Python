import requests
from collections import Counter
response = requests.get('http://www.gutenberg.org/files/1112/1112.txt')
def most_common_words(text):
    split_it = text.split()
    Cnter = Counter(split_it).most_common()
    # Cnter.sort(reverse=True)
    return Cnter[:10]

print(most_common_words(response.text))