import joblib
from sklearn.datasets import load_digits

def main():
    model = joblib.load("model_train.pkl")
    data = load_digits()
    X, y = data.data, data.target
    preds = model.predict(X)
    print("Sample predictions:", preds[:10])
    accuracy = (preds == y).mean()
    print("Inference Accuracy: {:.4f}".format(accuracy))

if __name__ == "__main__":
    main()
