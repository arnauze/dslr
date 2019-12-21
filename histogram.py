import pandas as pd
import matplotlib.pyplot as plt
import sys

def isNumber(value):
    try:
        float(value)
        return True
    except:
        return False

def histogram():
    if len(sys.argv) != 2:
        print("Error")
    else:
        f = pd.read_csv(sys.argv[1])

        count = 0
        for i in f:
            if isNumber(f[i][0]) and i != "Index":
                count += 1

        fig = plt.figure()

        index = 1
        for i in f:
            if isNumber(f[i][0]) and i != "Index":
                ax = fig.add_subplot(count / 3, count / 3, index)
                index += 1
                ax.hist(f[i][f["Hogwarts House"] == "Gryffindor"], color="r", alpha=0.5)
                ax.hist(f[i][f["Hogwarts House"] == "Slytherin"], color="g", alpha=0.5)
                ax.hist(f[i][f["Hogwarts House"] == "Ravenclaw"], color="y", alpha=0.5)
                ax.hist(f[i][f["Hogwarts House"] == "Hufflepuff"], color="b", alpha=0.5)
                ax.set_title(i)
                ax.set_ylabel("Frequency")
                ax.set_xlabel("Grade")

        plt.subplots_adjust(hspace=.5, wspace=.5)
        plt.show()


histogram()