from flask import Flask, request
from tensorflow.keras.models import load_model
import sys
import json

# Get your flask app object
app = Flask(__name__)

# Load model from local FS on server start
#model = load_model('./3/')
model = load_model(sys.argv[1])

with open(sys.argv[2]) as json_file:
    data = json.loads(json_file.read())

print(data)
#inputs = {'instances': ['-1', '1']}

inputs = [float(value[0]) for value in data['instances']]

@app.route("/", methods=["GET"])
def predict():
#    inputs = json.loads(request.data)['instances']
    preds = model.predict(inputs).tolist()
    return {
            'predictions': preds
            }

app.run(debug=True, host="0.0.0.0", port=8080)
