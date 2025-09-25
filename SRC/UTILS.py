# utils.py
"""
Utility functions for Stress Prediction Project
AI with Mechanics - Mini Project
"""

import pandas as pd

# ------------------------------
# Load dataset
# ------------------------------
def load_data(filepath: str):
    """
    Loads dataset from CSV file.

    Args:
        filepath (str): Path to CSV file.

    Returns:
        DataFrame: Loaded dataset.
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


# ------------------------------
# Calculate stress
# ------------------------------
def calculate_stress(load: float, area: float) -> float:
    """
    Calculates stress = load / area.

    Args:
        load (float): Applied force/load (N).
        area (float): Cross-sectional area (mm^2).

    Returns:
        float: Stress value.
    """
    if area == 0:
        raise ValueError("Area cannot be zero!")
    return load / area


# ------------------------------
# Evaluate model performance
# ------------------------------
from sklearn.metrics import accuracy_score, classification_report

def evaluate_model(model, X_test, y_test):
    """
    Evaluates model on test data.

    Args:
        model: Trained ML model.
        X_test: Features of test dataset.
        y_test: True labels.

    Returns:
        dict: Accuracy and classification report.
    """
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    report = classification_report(y_test, predictions, output_dict=True)
    return {
        "accuracy": acc,
        "report": report
    }
