import pandas as pd
import numpy as np
import json
import csv
import sys

SELECTED_FEATURES = ["Herbology", "Ancient Runes", "Astronomy", "Charms", "Defense Against the Dark Arts"]

def prediction(thetas, data):
    house = None
    score= None
    # Looping in each house
    for key, _ in thetas.items():
        tmp = np.dot(thetas[key], data)
        if (score is None or tmp > score):
            score = tmp
            house = key
    return house

def standardize(matrix, mean, std):
    return (matrix - mean) / std

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Error")
    else:
        df = pd.read_csv(sys.argv[1])
        json_file = open(sys.argv[2])
        data = json.load(json_file)
        theta_dic = data['houses']
        std = data['standard']['std']
        means = data['standard']['mean']

        df.loc[:, SELECTED_FEATURES] = standardize(df.loc[: , SELECTED_FEATURES], means, std)
        df = df.loc[:, SELECTED_FEATURES]
        df.insert(1, "t0", np.ones(df.shape[0]))
        df = df.dropna()
        predictions = []
        for index, row in df.iterrows():
            predictions.append((index, prediction(theta_dic, row)))
        with open("houses.csv", 'w+') as fd:
            writer = csv.writer(fd)
            writer.writerow(['Index', "Hogwarts House"])
            for prediction in predictions:
                writer.writerow([prediction[0], prediction[1]])