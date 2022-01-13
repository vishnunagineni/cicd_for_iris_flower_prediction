import os
import yaml
import pandas as pd
import argparse

def read_params(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config


def get_data(config_path):
    config=read_params(config_path)
    data_path=config["data_source"]["data_path"]
    columns=config["data_source"]["columns"]
    df=pd.read_csv(data_path,names=columns)
    return df

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    data=get_data(config_path=parsed_args.config)