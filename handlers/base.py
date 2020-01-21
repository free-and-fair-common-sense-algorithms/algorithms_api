import json
from utils import load_model
from sklearn_transformers import classifier_helpers

class ErrorMessage(Exception):
    status_code = 400
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


def predict(model_name, method, app, request):
    model = load_model(model_name, app.logger)
    request_json = request.get_json()
    app.logger.info(f'request json: {json.dumps(request_json)}')
    if method == 'predict_proba':
        prediction = model.predict_proba(request_json)[0]
    elif method == 'predict':
        prediction = model.predict(request_json)[0]
    app.logger.info(f'prediction: {json.dumps(prediction)}')
    response = json.dumps(prediction)
    return response
