import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import sys

def pair_plot(filename):
    df = pd.read_csv(filename)
    df = df.dropna(how='any',axis=0) 
    sns.pairplot(df, hue="Hogwarts House")
    plt.show()


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("usage: python3 describe.py <dataset>")
    else:
        pair_plot(sys.argv[1])