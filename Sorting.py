# Write a Program to implement all Sorting algos. Find the number of comparisons during each pass and display the intermediate result. Use the observed values to plot a graph to analyse the complexity of algorithm.

import matplotlib.pyplot as plt
import random

# Sorting Algorithms Implementation with Comparison Counting

class SortingAlgorithms:
    
    def __init__(self):
        self.comparisons = []
    
    def reset_comparisons(self):
        """Resets the comparisons count for each sorting pass"""
        self.comparisons = []
    
    def bubble_sort(self, arr):
        n = len(arr)
        self.reset_comparisons()
        for i in range(n):
            for j in range(0, n - i - 1):
                self.comparisons.append((arr.copy(), j, j+1))  # Record comparisons
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
        return arr
    
    def selection_sort(self, arr):
        n = len(arr)
        self.reset_comparisons()
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                self.comparisons.append((arr.copy(), min_idx, j))  # Record comparisons
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap
        return arr
    
    def insertion_sort(self, arr):
        n = len(arr)
        self.reset_comparisons()
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                self.comparisons.append((arr.copy(), j, j+1))  # Record comparisons
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
    
    def quick_sort(self, arr):
        self.reset_comparisons()
        self._quick_sort_helper(arr, 0, len(arr) - 1)
        return arr
    
    def _quick_sort_helper(self, arr, low, high):
        if low < high:
            pivot_index = self._partition(arr, low, high)
            self._quick_sort_helper(arr, low, pivot_index - 1)
            self._quick_sort_helper(arr, pivot_index + 1, high)
    
    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            self.comparisons.append((arr.copy(), i, j))  # Record comparisons
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def merge_sort(self, arr):
        self.reset_comparisons()
        return self._merge_sort_helper(arr)
    
    def _merge_sort_helper(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]
            
            left_sorted = self._merge_sort_helper(left_half)
            right_sorted = self._merge_sort_helper(right_half)
            
            return self._merge(left_sorted, right_sorted)
        else:
            return arr
    
    def _merge(self, left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            self.comparisons.append((left + right, i, j))  # Record comparisons
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged
    
    def heap_sort(self, arr):
        n = len(arr)
        self.reset_comparisons()
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self._heapify(arr, i, 0)
        return arr
    
    def _heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n:
            self.comparisons.append((arr.copy(), i, left))  # Record comparisons
            if arr[left] > arr[largest]:
                largest = left
        if right < n:
            self.comparisons.append((arr.copy(), i, right))  # Record comparisons
            if arr[right] > arr[largest]:
                largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self._heapify(arr, n, largest)


# Function to plot the comparison counts

def plot_comparison_counts(algorithms, data_sizes):
    for algorithm, label in algorithms:
        comparisons_per_pass = []
        for data_size in data_sizes:
            arr = random.sample(range(1, data_size * 10), data_size)
            algorithm.reset_comparisons()
            algorithm_method = getattr(algorithm, label)
            algorithm_method(arr)
            comparisons_per_pass.append(len(algorithm.comparisons))
        
        plt.plot(data_sizes, comparisons_per_pass, label=label)
    
    plt.xlabel("Data Size")
    plt.ylabel("Number of Comparisons")
    plt.legend()
    plt.title("Sorting Algorithms: Comparisons per Pass")
    plt.show()


# Main program
def main():
    sorting_algorithms = SortingAlgorithms()
    algorithms = [
        (sorting_algorithms, 'bubble_sort'),
        (sorting_algorithms, 'selection_sort'),
        (sorting_algorithms, 'insertion_sort'),
        (sorting_algorithms, 'quick_sort'),
        (sorting_algorithms, 'merge_sort'),
        (sorting_algorithms, 'heap_sort')
    ]
    
    data_sizes = [10, 50, 100, 200, 500, 1000]
    plot_comparison_counts(sorting_algorithms, data_sizes)

# Execute the program
if __name__ == "__main__":
    main()
