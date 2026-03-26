import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_pro_plots():
    try:
        df = pd.read_csv('rezultate.csv') 
    except FileNotFoundError:
        print("Eroare: Nu am găsit rezultate.csv!")
        return

    sns.set_theme(style="whitegrid")

    g = sns.catplot(
        data=df, 
        kind="bar",
        x="Tip_Date", y="Secunde", hue="Algoritm",
        row="N",
        palette="viridis", height=4, aspect=3,
        sharey=False
    )

    for ax in g.axes.flat:
        ax.set_yscale("log")
        ax.grid(True, which="both", ls="-", alpha=0.2)

    g.set_axis_labels("Scenariu Date (Tip)", "Timp Execuție (Secunde - Log Scale)")
    g.set_titles("Dimensiune Listă: N = {row_name}")
    g.fig.suptitle('Benchmark Sortare: Influența Tipului de Date vs. Scalabilitatea N', fontsize=16, y=1.02)

    plt.savefig('grafic_final.png', dpi=300, bbox_inches='tight')
    print("Graficul a fost generat: grafic_final.png")

if __name__ == "__main__":
    create_pro_plots()