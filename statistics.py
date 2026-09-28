import math
from collections import Counter
def statistics_calculator():
    print("\n--- Statistics Calculator ---")
    data = list(map(float, input("Enter numbers separated by spaces: ").split()))
    if not data:
        print("No data entered.")
        return
    n = len(data)
    mean = sum(data) / n
    sorted_data = sorted(data)
    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]
    counts = Counter(data)
    max_count = max(counts.values())
    if max_count == 1:
        mode = "No mode"
    else:
        mode = [x for x, count in counts.items() if count == max_count]
    variance = sum((x - mean) ** 2 for x in data) / n
    standard_deviation = math.sqrt(variance)
    print("\nResults:")
    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)
    print("Variance:", variance)
    print("Standard Deviation:", standard_deviation)