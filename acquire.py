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

def get_telco_data():
    filename = "telco_churn.csv"
    sql = '''SELECT *
        FROM customers 
        JOIN contract_types
        ON contract_types.contract_type_id = customers.contract_type_id
        JOIN internet_service_types
        ON internet_service_types.internet_service_type_id = customers.internet_service_type_id
        JOIN payment_types 
        ON payment_types.payment_type_id = customers.payment_type_id'''
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        df = pd.read_sql(sql, get_connection('telco_churn'))
        return df