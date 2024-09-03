import platform
import psutil
import time
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Gather System Information
def get_system_info():
    system_info = {
        "Operating System": platform.system() + " " + platform.release(),
        "CPU": platform.processor(),
        "RAM": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB"
    }
    print("System Information:", system_info)

# Step 2: Implement Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Step 3: Benchmarking Insertion Sort
def benchmark_insertion_sort(sizes):
    times = []
    for size in sizes:
        arr = np.random.randint(0, 10000, size).tolist()  # Generate random list of integers
        start_time = time.time()                          # Start timing
        insertion_sort(arr)                               # Sort using insertion sort
        times.append(time.time() - start_time)            # Record elapsed time
    return times

# Step 4: Define Input Sizes and Run Benchmarks
sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 15000]

# Gather system information
get_system_info()

# Benchmark insertion sort
insertion_sort_times = benchmark_insertion_sort(sizes)

# Step 5: Plot the Results
plt.figure(figsize=(12, 6))
plt.plot(sizes, insertion_sort_times, marker='o', color='r', label='Insertion Sort')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Insertion Sort Benchmark: Time vs Input Size')
plt.legend()
plt.grid(True)
plt.show()
