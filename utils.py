import os
import pathlib
import boto3
from model import Model
from config import LOCAL_FOLDER, BUCKET


class s3(object):
    def __init__(self, local_folder, bucket_name):
        self.local_folder = local_folder
        self.bucket = bucket_name
        self.client = boto3.client('s3', region_name='us-east-1')
        create_folder(self.local_folder)

    def download(self, key):
        local_file = os.path.join(self.local_folder, key)
        self.client.download_file(self.bucket, key, local_file)
        return local_file


def load_model(model_filename, logger):
    model_filepath = s3(LOCAL_FOLDER, BUCKET).download(model_filename)
    model = Model(model_filepath, logger=logger)
    return model

def create_folder(filepath):
    pathlib.Path(filepath).mkdir(parents=True, exist_ok=True)
