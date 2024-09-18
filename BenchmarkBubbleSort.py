import time
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import numpy as np

# Implementing the sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Function to benchmark the sorting algorithms
def benchmark_sorting_algorithm(sort_func, sizes):
    times = []
    for size in sizes:
        arr = np.random.randint(0, 10000, size).tolist()
        start_time = time.time()
        sort_func(arr)
        times.append(time.time() - start_time)
    return times

# Array sizes for benchmarking
sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]

# Benchmarking the algorithms
bubble_times = benchmark_sorting_algorithm(bubble_sort, sizes)
insertion_times = benchmark_sorting_algorithm(insertion_sort, sizes)
selection_times = benchmark_sorting_algorithm(selection_sort, sizes)

# Plotting the results
plt.figure(figsize=(12, 6))
plt.plot(sizes, bubble_times, marker='o', label='Bubble Sort')
plt.plot(sizes, insertion_times, marker='o', label='Insertion Sort')
plt.plot(sizes, selection_times, marker='o', label='Selection Sort')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Sorting Algorithm Benchmark: Time vs Input Size')
plt.legend()
plt.grid(True)
plt.show()
