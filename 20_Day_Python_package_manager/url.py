import requests
from collections import Counter
from pprint import pprint
import numpy
response = requests.get('http://www.gutenberg.org/files/1112/1112.txt')
def most_common_words(text):
    split_it = text.split()
    Cnter = Counter(split_it).most_common()
    # Cnter.sort(reverse=True)
    return Cnter[:10]

# print(most_common_words(response.text))

cat_pi = requests.get('https://api.thecatapi.com/v1/breeds')
data = cat_pi.json()
metric_weights = []

for breed in data:
    metric_weights.append((int(breed['weight']['metric'].split()[0]) + int(breed['weight']['metric'].split()[-1])) / 2)

median = numpy.median(metric_weights)
mean = numpy.mean(metric_weights)
min_metric = min(metric_weights)
max_metric = max(metric_weights)
sd = numpy.std(metric_weights)
print("Standard Deviation: %0.2f" % sd)
print("Minimum:", min_metric)
print("Maximum:", max_metric)
print("Median:", median)
print("Mean: %0.2f" % mean)