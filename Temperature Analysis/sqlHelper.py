from sqlalchemy import create_engine
import pandas as pd
import numpy as np

class SQLHelper():

    def __init__(self):
        self.connection_string = r"sqlite:///Resources\\hawaii.sqlite"
        self.engine = create_engine(self.connection_string)

    def get_precipitation(self):
        query = """
                SELECT
                    station, 
                    date,
                    prcp
                FROM
                    measurement
                ORDER BY
                    date, station
                """
        conn = self.engine.connect()
        df = pd.read_sql(query, con=conn)
        conn.close()

        return df

    def get_stations(self):
        query = """
                SELECT 
                    *
                FROM
                    station
                """
        conn = self.engine.connect()
        df = pd.read_sql(query, con=conn)
        conn.close()

        return df
    
    def get_tobs(self):
        query = ""
        with open("queries/tobs.sql", "r") as f:
            query = f.read()
        
        conn = self.engine.connect()
        df = pd.read_sql(query, con=conn)
        conn.close()

        return df

    def get_temp_start(self, start):
        query = f"""
                SELECT
                    min(tobs) as Min_Temp,
                    max(tobs) as Max_Temp,
                    avg(tobs) as Avg_Temp
                FROM
                    measurement
                WHERE
                    date >= '{start}'
                """
        conn = self.engine.connect()
        df = pd.read_sql(query, con=conn)
        conn.close()

        return df

    def get_temp_dates(self, start, end):
        query = f"""
                SELECT
                    min(tobs) as Min_Temp,
                    max(tobs) as Max_Temp,
                    avg(tobs) as Avg_Temp
                FROM
                    measurement
                WHERE
                    date >= '{start}'
                    AND date <= '{end}'
                """
        conn = self.engine.connect()
        df = pd.read_sql(query, con=conn)
        conn.close()

        return df