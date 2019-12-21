import sys
import math

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# -------------------------------------
# Describe math functions
# -------------------------------------

def mean(dataset):
    total = 0
    for data in dataset:
        total += data
    return total / len(dataset)

def std(dataset):
    s = 0
    m = mean(dataset)
    for data in dataset:
        s += ((data - m) ** 2)
    s /= len(dataset)
    return math.sqrt(s)

def percentile(N, percent):
    l = len(N)
    N.sort()
    k = (l - 1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return N[f]
    d0 = N[f] * (c-k)
    d1 = N[c] * (k-f)
    return d0+d1

# -------------------------------------
# Outputting the informations
# -------------------------------------

def getInformations(dataset):
    new_dataset = {}
    index = 0
    for i in range(0, len(dataset)):
        if dataset[i]["is_number"]:
            new_dataset[index] = {
                "name": dataset[i]["name"],
                "mean": round(mean(dataset[i]["elements"]), 6),
                "std": round(std(dataset[i]["elements"]), 6),
                "min": round(min(dataset[i]["elements"]), 6),
                "max": round(max(dataset[i]["elements"]), 6),
                "25%": round(percentile(dataset[i]["elements"], 0.25), 6),
                "50%": round(percentile(dataset[i]["elements"], 0.50), 6),
                "75%": round(percentile(dataset[i]["elements"], 0.75), 6)
            }
            index += 1
    outputDataset(new_dataset, dataset)
    return new_dataset

def outputDataset(dataset, old_dataset):
    data = {
        "name": [""],
        "count": ["count"],
        "mean": ["mean"],
        "std": ["std"],
        "min": ["min"],
        "25%": ["25%"],
        "50%": ["50%"],
        "75%": ["75%"],
        "max": ["max"]
    }
    for i in range(0, len(dataset)):
        if len(str(dataset[i]["name"])) > 20:
            name = str(dataset[i]["name"])[:19] + "."
        else:
            name = str(dataset[i]["name"])
        data["name"].append(name)
        data["count"].append(str(len(old_dataset[i]["elements"])))
        data["mean"].append(str(dataset[i]["mean"]))
        data["std"].append(str(dataset[i]["std"]))
        data["min"].append(str(dataset[i]["min"]))
        data["25%"].append(str(dataset[i]["25%"]))
        data["50%"].append(str(dataset[i]["50%"]))
        data["75%"].append(str(dataset[i]["75%"]))
        data["max"].append(str(dataset[i]["max"]))

    col_width = max(len(word) for row in data.values() for word in row) + 2  # padding
    for row in data.values():
        print ("".join(word.rjust(col_width) for word in row))

def getMaxLength(data):
    length = len(data["name"])
    if len(str(data["mean"])) > length:
        length = len(str(data["mean"]))
    if len(str(data["std"])) > length:
        length = len(str(data["std"]))
    if len(str(data["min"])) > length:
        length = len(str(data["min"]))
    if len(str(data["max"])) > length:
        length = len(str(data["max"]))
    if len(str(data["25%"])) > length:
        length = len(str(data["25%"]))
    if len(str(data["50%"])) > length:
        length = len(str(data["50%"]))
    if len(str(data["75%"])) > length:
        length = len(str(data["75%"]))
    return length


# -------------------------------------
# Parsing the csv file
# -------------------------------------

def parseLine(line, index, dataset):
    if index == 0:
        keys = line.split(",")
        for i in range(0, len(keys)):
            dataset[i] = {"name": keys[i], "elements": []}
    elif index == 1:
        values = line.split(",")
        for i in range(0, len(values)):
            dataset[i]["is_number"] = is_number(values[i])
            if dataset[i]["is_number"]:
                dataset[i]["elements"].append(float(values[i]))
            else:
                dataset[i]["elements"].append(values[i])
    else:
        values = line.split(",")
        for i in range(0, len(values)):
            if (values[i]):
                if dataset[i]["is_number"]:
                    dataset[i]["elements"].append(float(values[i]))
                else:
                    dataset[i]["elements"].append(values[i])
            # else:
            #     dataset[i]["elements"].append(0)
    return dataset

# -------------------------------------
# Parsing the file to create a dictionary of dictionaries:
#           -> Index: number
#               -> name: string
#               -> is_number: bool
#               -> elements: list
# -------------------------------------
def parseFile(filename):
    i = 0
    file = open(filename, "r")
    lines = file.readlines()
    dataset = {}
    for i in range(0, len(lines)):
        dataset = parseLine(lines[i].replace("\n", ""), i, dataset)
    return dataset

# -------------------------------------
# Describe function
# -------------------------------------

def describe(file):
    dataset = parseFile(file)
    return getInformations(dataset)

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("usage: python3 describe.py <dataset>")
    else:
        describe(sys.argv[1])