
import pandas as pd
import matplotlib.pyplot as plt
from first_program import get_thetas, get_min_max

def calculate_mse(kms, prices, theta0, theta1, min_km, max_km):
    kms_norm = (kms - min_km) / (max_km - min_km)
    predicted = theta0 + theta1 * kms_norm
    mse = ((predicted - prices) ** 2).mean()
    print(f"Mean Squared Error: {mse}")

def plot_regression_line(kms, prices):
    theta0, theta1 = get_thetas()
    min_km, max_km = get_min_max()
    calculate_mse(kms, prices, theta0, theta1, min_km, max_km)
    kms_norm = (kms - min_km)/(max_km - min_km)
    predicted = theta0 + theta1 * kms_norm
    plt.scatter(kms, prices, color='blue', label='Training data')
    plt.plot(kms, predicted, color='red', label='Regression line')
    plt.xlabel("Mileage (km)")
    plt.ylabel("Price (€)")
    plt.title("Linear Regression Fit")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.1)
    plt.show()


if __name__ == "__main__":
    dataFrame = pd.read_csv('data.csv')
    dataFrame = dataFrame.sort_values(by='km')
    kms = dataFrame['km']
    prices = dataFrame['price']
    plot_regression_line(kms, prices)

