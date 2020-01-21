from functools import lru_cache
import dill
import sklearn_transformers


class Model(object):
    def __init__(self, model_filepath, logger):
        self.model_filepath = model_filepath
        self.logger = logger
        self.load_model()

    @lru_cache(maxsize=None)
    def load_model(self):
        filename = self.model_filepath
        self.logger.info('Downloading model: %s', filename)
        with open(filename, 'rb') as infile:
            model = dill.load(infile)
        self.model = model

    def predict(self, x):
        return self.model.predict([x])

    def predict_proba(self, x):
        return self.model.predict_proba([x])
