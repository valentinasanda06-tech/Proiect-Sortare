import time
import csv
import os
from src.algoritmi import bubble_sort, insertion_sort, merge_sort, quick_sort

def load_data(path):
    with open(path, 'r') as f:
        return [int(line.strip()) for line in f]

def run_experiment():
    base_dir = 'data'
    results = []
    algos = {
        "BubbleSort": bubble_sort,
        "InsertionSort": insertion_sort,
        "MergeSort": merge_sort,
        "QuickSort": quick_sort,
        "PythonNative": sorted
    }

    for folder in sorted(os.listdir(base_dir)):
        folder_path = os.path.join(base_dir, folder)
        if not os.path.isdir(folder_path): continue
        
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            data = load_data(file_path)
            n = len(data)
            tip_test = file.replace(".txt", "")
            
            print(f"\n--- Test: {folder} | Tip: {tip_test} ---")
            
            for name, func in algos.items():
                # Skip the slowest
                if n > 10000 and name in ["BubbleSort", "InsertionSort"]:
                    continue
                
                print(f"Rulăm {name}...", end=" ", flush=True)
                data_copy = data.copy()
                
                start = time.perf_counter()
                func(data_copy)
                end = time.perf_counter()
                
                results.append([name, n, tip_test, f"{end-start:.6f}"])
                print(f"{end-start:.4f}s")

    with open("rezultate.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Algoritm", "N", "Tip_Date", "Secunde"])
        writer.writerows(results)

if __name__ == "__main__":
    run_experiment()