📂 `src/` Folder Description

* **`train_model.py`** 🏋️‍♂️

  * Script to **train the stress prediction model** using Scikit-learn.
  * Reads dataset (`data/stress_data.csv`), processes features (Load, Area, Material Strength), and trains the ML model.
  * Saves the trained model as `stress_model.pkl` for later use in prediction or deployment.

---

* **`predict.py`** 🔮

  * Loads the trained model (`stress_model.pkl`).
  * Accepts new input values (Load, Area, Material Strength).
  * Predicts **Stress Status → SAFE ✅ / UNSAFE ⚠️**.
  * Can be connected to Flask/Streamlit for a web interface.

---

* **`utils.py`** 🛠️

  * Contains **helper functions** used by both training and prediction scripts.
  * Examples:

    * `calculate_stress(load, area)` → returns Load/Area.
    * `load_data(path)` → loads dataset.
    * `evaluate_model(model, X_test, y_test)` → prints accuracy & metrics.
  * Keeps the code **modular, clean, and reusable**.

---
