
import pandas as pd
import matplotlib.pyplot as plt
from first_program import get_thetas, get_min_max
    
def plot_regression_line(kms, prices):
    theta0, theta1 = get_thetas()
    min_km, max_km, min_price, max_price = get_min_max()
    kms_norm = (kms - min_km)/(max_km - min_km)
    predicted_norm = theta0 + theta1 * kms_norm
    predicted = predicted_norm * (max_price - min_price) + min_price

    mse = ((predicted - prices) ** 2).mean()
    print(f"Mean Squared Error: {mse}")

    min_idx = kms.idxmin()
    max_idx = kms.idxmax()
    plt.figure(figsize=(8,5))
    plt.scatter(kms, prices, color='green', label='Training data')
    plt.plot(kms, predicted, color='red', label='Regression line')
    plt.scatter(kms[min_idx], prices[min_idx], color='blue', s=100, marker='o', label='Min mileage')
    plt.scatter(kms[max_idx], prices[max_idx], color='purple', s=100, marker='x', label='Max mileage')
    plt.xlabel("Mileage (km)")
    plt.ylabel("Price (€)")
    plt.title("Linear Regression Fit with Min/Max Mileage Highlighted")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.1)
    # plt.show()

    plt.figure()
    plt.hist(prices, bins=10, color='skyblue')
    plt.xlabel("Price (€)")
    plt.ylabel("Count")
    plt.title("Distribution of Prices")
    plt.show()

if __name__ == "__main__":
    dataFrame = pd.read_csv('data.csv')
    dataFrame = dataFrame.sort_values(by='km')
    kms = dataFrame['km']
    prices = dataFrame['price']
    plot_regression_line(kms, prices)

