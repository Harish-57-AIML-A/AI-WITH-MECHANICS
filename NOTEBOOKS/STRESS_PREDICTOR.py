import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Create synthetic dataset
data = {
    'Load': np.random.randint(100, 1000, 100),
    'Area': np.random.randint(10, 100, 100),
    'Material_Strength': np.random.randint(200, 500, 100)
}

df = pd.DataFrame(data)

# Stress Calculation
df['Stress'] = df['Load'] / df['Area']

# Label: SAFE (0) if stress < Material_Strength, else UNSAFE (1)
df['Status'] = np.where(df['Stress'] < df['Material_Strength'], 0, 1)

df.head()

# Create synthetic dataset
data = {
    'Load': np.random.randint(100, 1000, 100),
    'Area': np.random.randint(10, 100, 100),
    'Material_Strength': np.random.randint(200, 500, 100)
}

df = pd.DataFrame(data)

# Stress Calculation
df['Stress'] = df['Load'] / df['Area']

# Label: SAFE (0) if stress < Material_Strength, else UNSAFE (1)
df['Status'] = np.where(df['Stress'] < df['Material_Strength'], 0, 1)

df.head()

X = df[['Load', 'Area', 'Material_Strength']]
y = df['Status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Example test
sample = pd.DataFrame([[800, 50, 300]], columns=['Load', 'Area', 'Material_Strength'])
prediction = model.predict(sample)[0]
print("Prediction:", "SAFE ✅" if prediction == 0 else "UNSAFE ⚠️")


import joblib
joblib.dump(model, "stress_model.pkl")

