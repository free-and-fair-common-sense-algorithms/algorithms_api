from flask import Flask
from flask import jsonify
from flask import Response
from flask import request
from flask_cors import CORS
from handlers.base import ErrorMessage
from handlers.base import predict


app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def health():
    return Response('ok', 200)


@app.route('/bail-amount', methods=['POST'])
def bail_amount():
    print(request.headers)
    if request.method == 'POST':
        try:
            response = predict('bail_amount.model', 'predict_proba', app, request)
            return Response(response, 200)
        except Exception as e:
            raise e
    else:
        return Response('Method Not Allowed', 403)


@app.route('/health-insurance-claim', methods=['POST'])
def health_insurance():
    if request.method == 'POST':
        try:
            response = predict('health_insurance_claim.model', 'predict_proba', app, request)
            return Response(response, 200)
        except Exception as e:
            raise e
    else:
        return Response('Method Not Allowed', 403)


@app.route('/higher-education-grant', methods=['POST'])
def higher_education_grant():
    if request.method == 'POST':
        try:
            response = predict('higher_education_grant.model', 'predict', app, request)
            return Response(response, 200)
        except Exception as e:
            raise e
    else:
        return Response('Method Not Allowed', 403)


@app.errorhandler(ErrorMessage)
def handle_error(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
