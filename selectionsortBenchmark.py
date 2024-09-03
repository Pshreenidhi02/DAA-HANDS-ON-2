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

# Step 2: Implement Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Step 3: Benchmarking Selection Sort
def benchmark_selection_sort(sizes):
    times = []
    for size in sizes:
        arr = np.random.randint(0, 10000, size).tolist()  # Generate random list of integers
        start_time = time.time()                          # Start timing
        selection_sort(arr)                               # Sort using selection sort
        times.append(time.time() - start_time)            # Record elapsed time
    return times

# Step 4: Define Input Sizes and Run Benchmarks
sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 15000]

# Gather system information
get_system_info()

# Benchmark selection sort
selection_sort_times = benchmark_selection_sort(sizes)

# Step 5: Plot the Results
plt.figure(figsize=(12, 6))
plt.plot(sizes, selection_sort_times, marker='o', color='g', label='Selection Sort')
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Input Size (n)')
plt.ylabel('Time (seconds)')
plt.title('Selection Sort Benchmark: Time vs Input Size')
plt.legend()
plt.grid(True)
plt.show()
