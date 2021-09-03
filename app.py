from flask import Flask, url_for, render_template, jsonify
from Soccer_Analysis import PredictionsGenie

app = Flask(__name__)

@app.route('/getPredictions/<home>/<away>', methods=['GET'])
def getPredictions(home, away):
    myPG = PredictionsGenie()
    message = {"result": myPG.getPredictions(home, away)}
    return jsonify(message)
    

@app.route('/')
def data():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)