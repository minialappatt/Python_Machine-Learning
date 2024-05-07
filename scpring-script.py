import json
import numpy as np
import os
import pickle
import joblib
from sklearn.tree import DecisionTreeClassifier

from azureml.core import Model

def init():

    global model

    model_name = 'iris'

    path = Model.get_model_path(model_name)

    model = joblib.load(path)

def run(data):

    try:

        data = json.loads(data)

        result = model.predict(data['data'])

        return {'data' : result.tolist() , 'message' : "Successfully classified Iris"}

    except Exception as e:

        error = str(e)

        return {'data' : error , 'message' : 'Failed to classify iris'}