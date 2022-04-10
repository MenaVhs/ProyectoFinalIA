import flask
import os
from flask import Response

app = flask.Flask(__name__)
port = int (os.getenv("PORT", 9099))

#model = pickle.load(open("SVCmodel_failurePrediction.pkl","rb"))

@app.route('/cascadeModel', methods=['get'])
def predict():
    with open('cascade.xml', 'r') as f:
        data = f.read()

    return Response(data, mimetype='text/xml')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
