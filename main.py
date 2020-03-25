# All includes
# import os
import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# import tensorflow as tf  # Version 2.1.x
import csv

# TODO: faster read function -> Chris

data_chris_thomas = "data_chris_thomas.csv"
data_david_timur = "data_david_timur.csv"
data_jonas = "data_jonas.csv"
data_merged = "data_merged.csv"


def read_from_csv(file):
    print("Loading data...")
    path = "data/" + file
    data_X = np.array([])
    data_y = np.array([])
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in reader:
            sample = np.array([row[1:]])
            if line_count == 0:
                data_X = sample
                line_count += 1
            else:
                data_X = np.append(data_X, sample, axis=0)
                line_count += 1
            data_y = np.append(data_y, int(float(row[0])))
            data_y = data_y.reshape(-1, 1)
    data_X = data_X.astype('float64')
    data_y = data_y.astype('int')
    csv_file.close()
    return data_X, data_y


test_X, test_y = read_from_csv(data_david_timur)

print(len(test_X))
print(len(test_y))

