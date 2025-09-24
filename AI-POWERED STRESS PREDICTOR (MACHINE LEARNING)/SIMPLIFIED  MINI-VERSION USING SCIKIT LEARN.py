import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers

# ---------------------------
# 1. Create Synthetic Dataset
# ---------------------------
np.random.seed(42)

n = 1000
length = np.random.uniform(50, 200, n)
width = np.random.uniform(10, 100, n)
thickness = np.random.uniform(5, 50, n)
load = np.random.uniform(100, 1000, n)
material_strength = np.random.uniform(200, 600, n)

# Formula (synthetic relation)
max_stress = (load * length) / (width * thickness) + np.random.normal(0, 5, n)

# Put into DataFrame
data = pd.DataFrame({
    'length': length,
    'width': width,
    'thickness': thickness,
    'load': load,
    'material_strength': material_strength,
    'max_stress': max_stress
})

print(data.head())

# ---------------------------
# 2. Train/Test Split
# ---------------------------
X = data.drop('max_stress', axis=1)
y = data['max_stress']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ---------------------------
# 3. Neural Network Model
# ---------------------------
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1)  # regression output
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

history = model.fit(X_train_scaled, y_train, epochs=50, validation_split=0.2, verbose=0)

# ---------------------------
# 4. Evaluate Model
# ---------------------------
loss, mae = model.evaluate(X_test_scaled, y_test, verbose=0)
print(f"Test MAE: {mae:.2f} MPa")

# ---------------------------
# 5. Visualization
# ---------------------------
plt.plot(history.history['mae'], label='Train MAE')
plt.plot(history.history['val_mae'], label='Val MAE')
plt.xlabel('Epochs')
plt.ylabel('MAE')
plt.legend()
plt.show()

# ---------------------------
# 6. Prediction Example
# ---------------------------
sample = np.array([[120, 40, 20, 500, 300]])  # (length, width, thickness, load, material_strength)
sample_scaled = scaler.transform(sample)
pred = model.predict(sample_scaled)
print(f"Predicted Stress: {pred[0][0]:.2f} MPa")
