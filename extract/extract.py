import pandas as pd

def extract():
    df = pd.read_csv("data/data.csv", encoding='latin1')
    return df