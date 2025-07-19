import pytest
import os
import joblib
from sklearn.linear_model import LogisticRegression
from utils import load_config
from train import main as train_main
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score

def test_configs():
    config = load_config('config/config.json')
    assert "C" in config and isinstance(config["C"], float)
    assert "solver" in config and isinstance(config["solver"], str)
    assert "max_iter" in config and isinstance(config["max_iter"], int)

def test_model_creation_and_fit():
    train_main()
    assert os.path.exists("model_train.pkl")
    model = joblib.load("model_train.pkl")
    assert isinstance(model, LogisticRegression)
    assert hasattr(model, "coef_")
    assert hasattr(model, "classes_")

def test_model_accuracy():
    model = joblib.load("model_train.pkl")
    data = load_digits()
    X, y = data.data, data.target
    preds = model.predict(X)
    acc = accuracy_score(y, preds)
    assert acc > 0.85  # reasonable threshold for digits dataset
