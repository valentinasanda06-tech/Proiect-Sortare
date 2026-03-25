import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_plots():
    try:
        df = pd.read_csv('rezultate.csv')
    except FileNotFoundError:
        print("Eroare: Nu am găsit rezultate.csv! Rulează mai întâi main.py.")
        return

    # Style
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(12, 8))
    
    # Graph
    plot = sns.barplot(x='N', y='Secunde', hue='Algoritm', data=df, palette="magma")
    plot.set_yscale("log")
    plt.title('Comparație Performanță Algoritmi de Sortare', fontsize=16, pad=20)
    plt.xlabel('Număr de elemente (N)', fontsize=12)
    plt.ylabel('Timp de execuție (Secunde - Scara Logaritmică)', fontsize=12)
    plt.legend(title='Algoritm', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    plt.savefig('grafic_performanta.png', dpi=300)
    print("Succes! Graficul a fost salvat ca 'grafic_performanta.png'.")

if __name__ == "__main__":
    create_plots()