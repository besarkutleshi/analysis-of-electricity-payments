import pandas as pd

class District():

    def __init__(self, data):
        self.df = data
        
    def getTransactionCount_Month(self):
        tableData = self.df.groupby(['District','Month']).size().to_frame('Count').reset_index()
        return tableData
        
    def getTransactionCountComulative(self):
        data = self.getTransactionCount_Month()
        return data['Count'].cumsum()

    def getTransactionCount_Month_Pivot(self):
        table = self.getTransactionCount_Month()
        pvtTable = pd.pivot_table(data=table,values=['Month'],index=['District','Count'])
        return pvtTable




