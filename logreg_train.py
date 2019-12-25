import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import sys

SELECTED_FEATURES = ["Herbology", "Ancient Runes", "Astronomy", "Charms", "Defense Against the Dark Arts"]

class Train:
    def __init__(self, data, learning_rate, iterations, visualizer):
        data.insert(0, "t0", np.ones(data.shape[0]))        
        self.selected_features = ["Hogwarts House"] + ["t0"] + SELECTED_FEATURES
        self.data = data.loc[:, self.selected_features]
        self.data = self.data.dropna()
        self.lr = learning_rate
        self.iterations = iterations
        self.predictions = {}
        self.houses = self.data.loc[:, "Hogwarts House"]
        self.houses_set = self.data.loc[:, "Hogwarts House"].unique()
        self.visualizer = visualizer

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def is_from_house(self, house):
        return np.where(self.houses == house, 1, 0)

    def ft_standardize(self, matrix):
        return [matrix.std(), matrix.mean(), ((matrix - matrix.mean()) / matrix.std())]

    def train(self):
        std, means, x = self.ft_standardize(self.data.loc[:, self.selected_features[2:]])
        x.insert(0, "t0", self.data.loc[:, "t0"])
        self.predictions['standard'] = {'std' : list(std), 'mean': list(means)}
        self.predictions['houses'] = {}
        m = x.shape[0]            # Rows
        for house in self.houses_set:
            cost = []
            thetas = np.zeros((x.shape[1]))
            y = self.is_from_house(house)
            # Starting the training
            for _ in range(self.iterations):
                z = np.dot(x, thetas)   # Linear regression formula
                h = self.sigmoid(z)
                # Cost function
                j = (1 / m) * (np.dot((-y).T, np.log(h)) - np.dot((1 - y).T, np.log(1 - h)))
                cost.append(j)
                gradient = np.dot(x.T, (h - y)) / y.size
                thetas -= self.lr * gradient
            self.predictions['houses'][house] = list(thetas)
            if self.visualizer:
                plt.plot(cost ,label=house)
        if self.visualizer:
            plt.legend()
            plt.show()
        with open("weights.json", 'w+') as json_file:
            json.dump(self.predictions,  json_file)

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("usage python3 logreg_train <dataset> [-v]")
    else:
        df = pd.read_csv(sys.argv[1], sep=',')
        if (len(sys.argv) > 2 and "-v" in sys.argv[2]):
            Train(df, 0.1, 2000, True).train()
        else:
            Train(df, 0.1, 2000, False).train()