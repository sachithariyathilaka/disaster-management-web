import sys

from google.api_core.client_options import ClientOptions
from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2
import os
import json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="crested-vortex-256214-6e0b03b18a24.json"

def inline_text_payload(file_path):
  with open(file_path, 'rb') as ff:
    content = ff.read()
  return {'text_snippet': {'content': content, 'mime_type': 'text/plain'} }

def pdf_payload(file_path):
  return {'document': {'input_config': {'gcs_source': {'input_uris': [file_path] } } } }

def get_prediction(file_path, model_name):
  options = ClientOptions(api_endpoint='automl.googleapis.com')
  prediction_client = automl_v1beta1.PredictionServiceClient(client_options=options)

  payload = inline_text_payload(file_path)
  # Uncomment the following line (and comment the above line) if want to predict on PDFs.
  # payload = pdf_payload(file_path)

  params = {}
  request = prediction_client.predict(model_name, payload, params)
  return request  # waits until request is returned

if __name__ == '__main__':
  file_path = sys.argv[1]
  model_name = sys.argv[2]

 print get_prediction(content, model_name)
