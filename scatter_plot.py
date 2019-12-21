import pandas as pd
import matplotlib.pyplot as plt
import sys

def isNumber(value):
    try:
        float(value)
        return True
    except:
        return False

def showAll(f):
    count = 0
    for i in f:
        if isNumber(f[i][0]):
            count += 1

    for i in f:
        index = 1
        if isNumber(f[i][0]):
            fig = plt.figure()
            for j in f:
                if isNumber(f[j][0]):
                    ax = fig.add_subplot(count / 3, count / 3, index)
                    ax.scatter(f[i][f["Hogwarts House"] == "Gryffindor"], f[j][f["Hogwarts House"] == "Gryffindor"], color="r", alpha=0.5)
                    ax.scatter(f[i][f["Hogwarts House"] == "Slytherin"], f[j][f["Hogwarts House"] == "Slytherin"], color="g", alpha=0.5)
                    ax.scatter(f[i][f["Hogwarts House"] == "Ravenclaw"], f[j][f["Hogwarts House"] == "Ravenclaw"], color="y", alpha=0.5)
                    ax.scatter(f[i][f["Hogwarts House"] == "Hufflepuff"], f[j][f["Hogwarts House"] == "Hufflepuff"], color="b", alpha=0.5)
                    ax.set_ylabel(i)
                    ax.set_xlabel(j)
                    index += 1
            plt.show()

def scatter():
    if len(sys.argv) < 2:
        print("Error")
    else:
        f = pd.read_csv(sys.argv[1])
        if (len(sys.argv) > 2 and "-v" in sys.argv[2]):
            showAll(f)
        else:
            plt.scatter(f["Defense Against the Dark Arts"], f["Astronomy"])
            plt.ylabel("Defense Against the Dark Arts")
            plt.xlabel("Astronomy")
            plt.show()


scatter()