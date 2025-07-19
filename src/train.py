import os
import joblib
from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from utils import load_config

def main():
    config = load_config('config/config.json')
    data = load_digits()
    X, y = data.data, data.target

    model = LogisticRegression(
        C=config["C"], 
        solver=config["solver"], 
        max_iter=config["max_iter"]
    )
    model.fit(X, y)
    joblib.dump(model, "model_train.pkl")
    print("Model trained and saved as model_train.pkl")

if __name__ == "__main__":
    main()
