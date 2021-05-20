import flask
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)


@app.route('/',methods=['GET'])
def default():
    return ''' <h1> Helloo.  Data scientist.....How are you </h1>'''


@app.route('/corona',methods=['GET'])
def corona():
    return ''' <h1> Corona curve is decreasing trend now.. </h1>'''

@app.route('/search',methods=['GET'])
def search():
    return ''' <h1> Searching...  '''+ request.args['s']+ '''</h1>'''



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


app.run()
