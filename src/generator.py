import random
import os

def create_subfolders():
    for size in ['mici_1000', 'medii_100000', 'gigant_100M']:
        path = os.path.join('data', size)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Subfolder creat: {path}")

def save_list(folder, name, data):
    path = os.path.join('data', folder, f"{name}.txt")
    with open(path, 'w') as f:
        for item in data:
            f.write(f"{item}\n")
    print(f"Creat fișier date: {path}")

def generate_scenarios(size_val, folder_name):
    # 1. Aleator
    save_list(folder_name, "aleator", (random.randint(0, size_val*10) for _ in range(size_val)))
    # 2. Sortat
    save_list(folder_name, "sortat", range(size_val))
    # 3. Invers sortat
    save_list(folder_name, "invers", range(size_val, 0, -1))
    # 4. Aproape sortat
    arr = list(range(size_val))
    for _ in range(max(1, int(size_val * 0.05))):
        idx1, idx2 = random.randint(0, size_val-1), random.randint(0, size_val-1)
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    save_list(folder_name, "aproape_sortat", arr)
    # 5. Plat
    save_list(folder_name, "plat", (random.randint(0, 10) for _ in range(size_val)))

def generate_all():
    create_subfolders()
    
    print("Generăm seturile MICI (1.000)...")
    generate_scenarios(1000, "mici_1000")
    
    print("Generăm seturile MEDII (100.000)...")
    generate_scenarios(100000, "medii_100000")
    
    print("Generăm seturile GIGANT (100.000.000)...")
    save_list("gigant_100M", "aleator", (random.randint(0, 10**9) for _ in range(10**8)))
    save_list("gigant_100M", "plat", (random.randint(0, 10) for _ in range(10**8)))

if __name__ == "__main__":
    generate_all()