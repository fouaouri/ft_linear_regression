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
            return min_km, max_km
    except FileNotFoundError:
        print("Min and max values file not found. Using default values (min_km=0, max_km=1).")
        return 0, 1
    except json.JSONDecodeError:
        print("Error decoding min and max values. Using default values (min_km=0, max_km=1).")
        return 0, 1
def predictPrice():
    theta0, theta1 = get_thetas()
    min_km, max_km = get_min_max()
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
            estimatedPrice = theta0 + (theta1 * normalizedKm)
            print(f"Estimated price: {estimatedPrice}")

if __name__ == "__main__":
    predictPrice()

