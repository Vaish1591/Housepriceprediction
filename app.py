import flask
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)

@app.route('/predict',methods=['GET'])
def predict():
    import joblib
    model = joblib.load('hp_trained_model.pkl')
    price = model.predict([[int(request.args['sqft']),
                            int(request.args['place']),
                            int(request.args['yo']),
                            int(request.args['tf']),
                            int(request.args['bhk']),
                           ]])
    return str(round(price[0]))


if __name__ == '__main__':
    app.run()
