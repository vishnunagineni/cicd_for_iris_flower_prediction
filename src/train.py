import os
import pandas as pd
import numpy as np
from urllib.parse import urlparse
#import seaborn as sns
import pandas as pd
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pickle
from get_data import read_params
import json
import argparse
import mlflow

def train_and_evaluate(config_path):
    config = read_params(config_path)
    train_data_path = config["processed_data_config"]["train_path"]
    test_data_path = config["processed_data_config"]["test_path"]
    model_dir = config["model_dir"]
    random_state = config["base"]["random_state"]
    target = config["base"]["target_col"]
    train = pd.read_csv(train_data_path,sep=",")
    test = pd.read_csv(test_data_path,sep=",")
    mlflow_config=config["mlflow_config"]
    mlflow.set_tracking_uri(mlflow_config["tracking_uri"])
    mlflow.set_experiment(mlflow_config["experiment_name"])
    train_y = train[target]
    test_y = test[target]
    train_x = train.drop([target],axis=1) 
    test_x = test.drop([target],axis=1)
    # Support vector machine algorithm
    with mlflow.start_run(run_name=mlflow_config["run_name"]):
        svc = SVC()
        svc.fit(train_x, train_y)
        # Predict from the test dataset
        predictions = svc.predict(test_x)
        # Calculate the accuracy
        accuracy=accuracy_score(test_y, predictions)
        print("Accuracy is :",accuracy)
        mlflow.log_metric('accuracy',accuracy)
        # A detailed classification report
        print(classification_report(test_y, predictions))
        tracking_uri_type=urlparse(mlflow.get_artifact_uri()).scheme
        if tracking_uri_type != "file":
            mlflow.sklearn.log_model(svc,"model",registered_model_name=mlflow_config["registered_model_name"])
        else:
            mlflow.sklearn.load_model(svc,"model")
    # Load the model
    # with open(model_path, 'rb') as f:
    #     model = pickle.load(f)
    # X_new = np.array([[3, 2, 1, 0.2], [  4.9, 2.2, 3.8, 1.1 ], [  5.3, 2.5, 4.6, 1.9 ]])
    # prediction = svc.predict(X_new)
    # print("Prediction of Species: {}".format(prediction))

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)