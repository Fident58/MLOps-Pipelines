from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Load a dummy model (replace with your actual model loading logic)
# For demonstration, we'll create a dummy model
class DummyModel:
    def predict(self, X):
        # Simulate a prediction
        return np.array([sum(x) for x in X])

dummy_model = DummyModel()

@app.route(\"/predict\", methods=[\"POST\"])
def predict():
    try:
        data = request.get_json(force=True)
        features = np.array(data[\"features\"])
        
        # Make prediction
        prediction = dummy_model.predict(features)
        
        return jsonify({\"prediction\": prediction.tolist()})
    except Exception as e:
        return jsonify({\"error\": str(e)}), 400

if __name__ == \"__main__\":
    app.run(host=\"0.0.0.0\", port=5000)
