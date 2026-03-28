import pandas as pd
import sys
import json


def checkTheInput(mileage):
    if not mileage:
        print("Please enter a valid mileage.")
        return False
    if mileage < 0:
        print("Mileage cannot be negative. Please enter a valid mileage.")
        return False
    return True

def get_thetas():
    try:
        with open('model_parameters.json', 'r') as f:
            params = json.load(f)
            theta0 = params.get('theta0', 0)
            theta1 = params.get('theta1', 0)
            return theta0, theta1
    except FileNotFoundError:
        print("Model parameters file not found. Using default values (theta0=0, theta1=0).")
        return 0, 0
    except json.JSONDecodeError:
        print("Error decoding model parameters. Using default values (theta0=0, theta1=0).")
        return 0, 0

def get_min_max():
    try:
        with open('min_max.json', 'r') as f:
            params = json.load(f)
            min_km = params.get('min_km', 0)
            max_km = params.get('max_km', 1)
            min_price = params.get('min_price', 0)
            max_price = params.get('max_price', 1)
            return min_km, max_km, min_price, max_price
    except FileNotFoundError:
        print("Min/max file not found.")
        return 0, 1, 0, 1

def predictPrice():
    theta0, theta1 = get_thetas()
    min_km, max_km, min_price, max_price = get_min_max()
    dataFrame = pd.read_csv('data.csv')
    km = dataFrame.drop('price', axis=1)
    price = dataFrame['price']

    while True:
        inputt = input("Enter the mileage: ")
        if inputt == "":
            print("There is no mileage value !")
            continue
        elif inputt == "exit":
            print("Exiting the program.")
            sys.exit(0)
        else:
            if inputt.isalpha():
                print("Please enter a valid mileage.")
                continue
            mileage = float(inputt)
            if not checkTheInput(mileage): 
                continue
            normalizedKm = (mileage - min_km) / (max_km - min_km)
            predicted_norm = theta0 + (theta1 * normalizedKm)
            estimatedPrice = predicted_norm * (max_price - min_price) + min_price
            print(f"Estimated price: {estimatedPrice}")

if __name__ == "__main__":
    predictPrice()

