import json
import logging
import os
import joblib
import pytest
from prediction_service.prediction import form_response, api_response
import prediction_service

input_data = {
    "incorrect_range": 
    {
        "Sepal_length":12,
        "Sepal_width":6,
        "Petal_length":7,
        "Petal_width":8
    },

    "correct_range":
    {
        "Sepal_length":5,
        "Sepal_width":4,
        "Petal_length":5,
        "Petal_width":2
    },

    "incorrect_col":
    {
        "sepal length":5,
        "Sepal_width":3,
        "Petal length": 2,
        "Petal_width":2
    }
}

TARGET_range = ['Iris-setosa','Iris-versicolor','Iris-virginica']

def test_form_response_correct_range(data=input_data["correct_range"]):
    res = form_response(data)
    assert  res[0] in TARGET_range

def test_api_response_correct_range(data=input_data["correct_range"]):
    res = api_response(data)
    assert  res["response"][0] in TARGET_range

def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotInRange):
        res = form_response(data)

def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInRange().message

def test_api_response_incorrect_col(data=input_data["incorrect_col"]):
    res = api_response(data)
    assert res["response"] == prediction_service.prediction.NotInCols().message