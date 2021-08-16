import os
import pandas as pd
import env

def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    filename = "titanic.csv"
    sql = '''SELECT passenger_id, survived, pclass, sex, age, sibsp, parch, fare, embarked, class, deck, embark_town, alone 
         FROM passengers'''
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql(sql, get_connection('titanic_db'))

        df.to_csv(filename)
        
        # Return the dataframe to the calling code
        return df  

    
def get_iris_data():
    filename = "iris.csv"
    sql = '''SELECT species.species_id, species_name, sepal_length, sepal_width, petal_length, petal_width 
        FROM species 
        JOIN measurements ON species.species_id = measurements.species_id'''
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql(sql , get_connection('iris_db'))
    
        # Return the dataframe to the calling code
        return df  