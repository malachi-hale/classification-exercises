def clean_data(df):
    df.drop_duplicates(inplace=True)
    df.drop(columns=['species_id'], inplace=True)
    df = df.rename(columns={"species_name": "species"})
    dummy_df = pd.get_dummies(df[['species']], drop_first=True)
    return pd.concat([df, dummy_df], axis=1)

def prep_iris(df):
    df = clean_data(df)
    return df