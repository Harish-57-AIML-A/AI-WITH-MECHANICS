import joblib
import numpy as np

# Load model
model = joblib.load("stress_model.pkl")

def predict_stress(load, area, strength):
    features = np.array([[load, area, strength]])
    prediction = model.predict(features)[0]
    return "Safe" if prediction == 0 else "Unsafe"

if __name__ == "__main__":
    print(predict_stress(500, 50, 300))  # Example test
