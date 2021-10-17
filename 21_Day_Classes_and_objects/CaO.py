import statistics as stat
from math import floor, ceil

class Statistics:
    def __init__(self, ages):
        self.array = ages
    def getData(self):
        return self.array
    def count(self):
        return len(self.array)
    def sum(self):
        return sum(self.array)
    def min(self):
        return min(self.array)
    def max(self):
        return max(self.array)
    def range(self):
        return max(self.array) - min(self.array)
    def mean(self):
        return stat.mean(self.array)
    def median(self):
        return stat.median(self.array)
    def mode(self):
        mode_value = stat.mode(self.array)
        return {'mode': mode_value, 'count': self.array.count(mode_value)}
    def std(self):
        return stat.stdev(self.array)
    def var(self):
        return stat.variance(self.array)
    def freq_dist(self):
        return sorted([(self.array.count(i)*4.0,i) for i in set(self.array)], reverse=True)
    
data = Statistics(ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26])
print('Count:', data.count())
print('Sum:', data.sum())
print('Min:', data.min())
print('Max:', data.max())
print('Range:', data.range())
print('Mean:', data.mean())
print('Median:', data.median())
print('Mode:', data.mode())
print('Standard Deviation: %.2f' % data.std())
print('Variance: %.2f' % data.var())
print('Frequency Distribution:', data.freq_dist())