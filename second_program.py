import pandas as pd
import sys
import json

def trainingData(dataFrame):
    theta0, theta1 = 0, 0
    learningRate, target, max_iteration = 0.0001, 0.001, 100000

    kms = dataFrame['km'].values
    prices = dataFrame['price'].values
    m = len(kms)

    min_km, max_km = kms.min(), kms.max()
    min_price, max_price = prices.min(), prices.max()
    kms_norm = (kms - min_km) / (max_km - min_km)
    prices_norm = (prices - min_price) / (max_price - min_price)

    for i in range(max_iteration):
        predicted = theta0 + theta1 * kms_norm
        error = predicted - prices_norm

        loss = ((predicted - prices_norm)**2).mean()
        if loss <= target:
            break

        tmp_theta0 = (learningRate / m) * error.sum()
        tmp_theta1 = (learningRate / m) * (error * kms_norm).sum()

        theta0 -= tmp_theta0
        theta1 -= tmp_theta1

    print(f"theta0: {theta0}, theta1: {theta1}")
    print(f"min_km: {min_km}, max_km: {max_km}")

    with open('model_parameters.json', 'w') as f:
        json.dump({'theta0': float(theta0), 'theta1': float(theta1)}, f)
    with open("min_max.json", 'w') as f:
        json.dump({'min_km': float(min_km), 'max_km': float(max_km), 'min_price': float(min_price), 'max_price': float(max_price)}, f)

if __name__ == "__main__":
    dataFrame = pd.read_csv(sys.argv[1])
    trainingData(dataFrame)

