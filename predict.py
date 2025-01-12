
import pickle 
from flask import Flask, request, jsonify

model_file = 'model_lr.bin'


with open(model_file, 'rb') as f_in :
    dv, model = pickle.load(f_in)
    
    
app = Flask('flood_prediction')

@app.route('/predict', methods=['POST'])

def predict():
    
    data = request.get_json()
    
    X = dv.transform([data])
    y_pred = model.predict(X)
    
    def categorize_flood_risk(prob):
        if prob < 0.2:
            return 0  # Low risk
        elif prob < 0.5:
            return 1  # Moderate risk
        else:
            return 2  # High risk
    
    flood_risk_code = categorize_flood_risk(y_pred[0])

    label_mapping = {
        0: "Low Risk",
        1: "Moderate Risk",
        2: "High Risk"
    }
    
    flood_class = label_mapping.get(flood_risk_code, "Unknown")

    result = {
        'Predicted Flood Risk Probability': y_pred[0],
        'Flood_Risk': flood_class
    }
        
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8686)

