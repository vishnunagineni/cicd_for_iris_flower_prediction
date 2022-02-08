import os
from get_data import read_params, get_data
import argparse
import category_encoders as ce
def load_and_save(config_path):
    config=read_params(config_path)
    df = get_data(config_path)
    new_cols = [col.replace(' ','_') for col in df.columns]
    raw_data_path = config["load_data"]["raw_data"]
    cols=[]
    for col in df:
        if df[col].isna().sum()>0:
            if df[col].dtypes=='object':
                df[col].fillna(df[col].mode()[0],inplace=True)
            else:
                df[col].fillna(df[col].mean(),inplace=True)
        if df[col].dtypes=='object':
            if col!='Class_labels':
                cols.append(col)
    print(cols)
    if len(cols)>0:
        OHE=ce.OneHotEncoder(cols=cols,use_cat_names=True)
        df=OHE.fit_transform(df)
    df.to_csv(raw_data_path,sep=",",index=False,header=new_cols)

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    load_and_save(config_path=parsed_args.config)