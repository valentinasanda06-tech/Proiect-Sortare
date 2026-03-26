import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_detailed_plots():
    try:
        df = pd.read_csv('rezultate.csv') 
    except FileNotFoundError:
        print("Eroare: Nu am găsit rezultate.csv!")
        return

    sns.set_theme(style="whitegrid")

    g = sns.catplot(
        data=df, 
        kind="bar",
        x="N", y="Secunde", hue="Algoritm",
        col="Tip_Date", col_wrap=3,
        palette="magma", height=5, aspect=1.2,
        sharey=True
    )

    for ax in g.axes.flat:
        ax.set_yscale("log")
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

    g.set_axis_labels("Număr elemente (N)", "Secunde (Log Scale)")
    g.set_titles("{col_name}")
    g.fig.suptitle('Analiza Detaliată a Algoritmilor de Sortare pe Scenarii', fontsize=18, y=1.05)

    plt.savefig('grafic_performanta.png', dpi=300, bbox_inches='tight')
    print("Succes! Graficul detaliat a fost salvat.")

if __name__ == "__main__":
    create_detailed_plots()