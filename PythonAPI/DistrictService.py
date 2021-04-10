import pyodbc as py
import pandas as pd
from PythonAPI import DbConnection as dbConnection
class DistrictService():

    def __init__(self):
        self.db = dbConnection.DbConnection()
    
    def get_Transaction_Count_Interval(self,year):
        conn = self.db.get_Connection()
        cursor = conn.cursor()
        execProcedure = "Exec dbo.usp_TransactionCount_Interval @year = " + str(year)
        df = pd.read_sql(execProcedure, conn)
        return df

    def get_All_Transaction(self,year,district):
        conn = self.db.get_Connection()
        cursor = conn.cursor()
        query = "SELECT MCTLD.JournalID,MCTLD.TransactionLocation,MCTLD.TransactionDate, MCTLD.TransactionAmount FROM dbo.MCCacheTransactionLocation" + district + " AS MCTLD where Year(MCTLD.TransactionDate) = " + str(year)
        df = pd.read_sql(query, conn)
        return df
        
    def get_Transaction_Count_Interval(self,year):
        conn = self.db.get_Connection()
        cursor = conn.cursor()
        execProcedure = "Exec dbo.usp_TransactionAmount_Interval @year = " + str(year)
        df = pd.read_sql(execProcedure, conn)
        return df




