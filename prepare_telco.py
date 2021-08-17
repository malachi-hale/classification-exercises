import pandas as pd
import os
import env
import matplotlib.pyplot as plt
import pandas as pd

def prep_telco(df):
    df = df.loc[:,~df.columns.duplicated()]
    df = df.drop(columns='species_id')
    df = df.rename(columns={"species_name": "species"})
    dummy_df = pd.get_dummies(df[['species']], drop_first=True)
    return pd.concat([df, dummy_df], axis=1)