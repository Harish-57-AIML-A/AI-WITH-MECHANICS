from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("../src/stress_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        load = float(request.form["load"])
        area = float(request.form["area"])
        strength = float(request.form["strength"])
        prediction = model.predict([[load, area, strength]])[0]
        result = "Safe" if prediction == 0 else "Unsafe"
        return f"Prediction: {result}"
    return '''
        <form method="post">
            Load: <input type="text" name="load"><br>
            Area: <input type="text" name="area"><br>
            Material Strength: <input type="text" name="strength"><br>
            <input type="submit" value="Predict">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
