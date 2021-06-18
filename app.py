from flask import Flask, request, jsonify, render_template
from model import get_output
from flask_cors import CORS,cross_origin

app = Flask(__name__)
cors=CORS(app)
app.config['CROSS-HEADERS']='Content-Type'
@app.route("/")
@cross_origin()
def home():
    return "Hello Welcome to Waste Segregation!!"

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    path = request.get_json(force=True)
    url = path['image']
    print(url)   
    prediction = get_output(url) 
    print(prediction)
    data = {'predict': prediction}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=true,host='0.0.0.0',port=5000)
