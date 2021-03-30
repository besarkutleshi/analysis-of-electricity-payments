import pandas as pd
import numpy as np

class District():

    def __init__(self, data):
        self.df = data
        
    # find count of transaction per month
    def get_Transaction_Count_Month(self):
        tableData = self.df.groupby(['District','Month']).size().to_frame('Count').reset_index()
        return tableData
        
    # find comulative count of transaction 
    def get_Transaction_Count_Comulative(self):
        data = self.get_Transaction_Count_Month()
        return data['Count'].cumsum()

    # get transaction count per month as a pivot table
    def get_Transaction_Count_Month_Pivot(self):
        table = self.get_Transaction_Count_Month()
        pvtTable = pd.pivot_table(data=table,values=['Month'],index=['District','Count'])
        return pvtTable

    # find sum of transaction per month
    def get_Transaction_Sum_Month(self):
        return self.df.groupby(['District','Month']).sum().to_frame('Sum').reset_index()

    # find comulative sum of transaction
    def get_Transaction_Sum_Comulative(self):
        groupedData = self.get_Transaction_Sum_Month()
        return groupedData['Sum'].cumsum()

    # get transaction sum per month as a pivot table
    def get_Transaction_Sum_Month_Pivot(self):
        table = self.get_Transaction_Sum_Month()
        pvtTable = pd.pivot_table(data=table,values=['Month'],index=['District','SUM'])
        return pvtTable

    # find sum average of transaction 
    def get_SumAverage_Transaction(self):
        return np.mean(self.df['TransactionAmount'])





