# The second program will be used to train your model. It will read your dataset file
# and perform a linear regression on the data.
# Once the linear regression has completed, you will save the variables theta0 and
# theta1 for use in the first program.

import pandas as pd
import sys
import json

def trainingData(dataFrame):
    theta0 = 0
    theta1 = 0
    learningRate = 0.1
    iterations = 10000

    kms = dataFrame['km'].values
    prices = dataFrame['price'].values
    m = len(kms)

    min_km = kms.min()
    max_km = kms.max()
    kms_norm = (kms - min_km) / (max_km - min_km)

    for _ in range(iterations):
        predicted = theta0 + theta1 * kms_norm
        error = predicted - prices

        tmp_theta0 = (learningRate / m) * error.sum()
        tmp_theta1 = (learningRate / m) * (error * kms_norm).sum()

        theta0 -= tmp_theta0
        theta1 -= tmp_theta1

    print(f"theta0: {theta0}, theta1: {theta1}")
    print(f"min_km: {min_km}, max_km: {max_km}")

    with open('model_parameters.json', 'w') as f:
        json.dump({'theta0': float(theta0), 'theta1': float(theta1)}, f)
    with open("min_max.json", 'w') as f:
        json.dump({'min_km': float(min_km), 'max_km': float(max_km)}, f)
if __name__ == "__main__":
    dataFrame = pd.read_csv(sys.argv[1])
    trainingData(dataFrame)

