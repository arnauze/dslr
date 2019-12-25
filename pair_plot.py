import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import sys

SELECTED_FEATURES = ["Hogwarts House", "Herbology", "Ancient Runes", "Astronomy", "Charms", "Defense Against the Dark Arts"]

def pair_plot(filename, opti):
    df = pd.read_csv(filename)
    if opti:
        df = df.loc[:, SELECTED_FEATURES]
    df = df.dropna(how='any',axis=0) 
    sns.pairplot(df, hue="Hogwarts House")
    plt.show()


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("usage: python3 describe.py <dataset>")
    else:
        if len(sys.argv) > 2 and "-o" in sys.argv[2]:
            pair_plot(sys.argv[1], True)
        else:
            pair_plot(sys.argv[1], False)