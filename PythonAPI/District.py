import pandas as pd
import numpy as np
from PythonAPI import DistrictService as ds
class District:

    df = ''
        
    def __init__(self,year=2020,district='DPR'):
        self.year = year
        self.district = district
        self.districtService = ds.DistrictService()

    def get_All_Transaction(self):
        df = self.districtService.get_All_Transaction(self.year,self.district)
        df['Year'] = pd.DatetimeIndex(df['TransactionDate']).year
        df['Month'] = pd.DatetimeIndex(df['TransactionDate']).month 
        df['District'] = df['JournalID'].str[0:3]
        District.df = df

    # -------------------------------------------- Count Analysis ----------------------------------------------------------


    # find total transaction number 
    def get_Total_Transaction(self):
        return District.df['JournalID'].count()

    # get transaction average   
    def get_Transaction_Average_Month(self):
        average = self.get_Total_Transaction() / 12;
        return average
        
    # get month that has the largest count of transactions
    def get_MaxTransactions_Count_Month(self):
        month_Counts = self.get_Transaction_Count_Month()
        month_Counts.sort_values("Count", ascending=False)
        return month_Counts.head(1)

    #find percentage of months in total transaction
    def get_Percentage_Count(self): 
        totalCounts = self.get_Total_Transaction()
        counts = self.get_Transaction_Count_Month()
        counts.sort_values("Month")
        percentage_List = []
        for index, row in counts.iterrows():
            percentage = (row['Count'] / totalCounts) * 100
            obj = {
                "Month":row['Month'],
                "Count":percentage
            }
            percentage_List.append(obj)
        return percentage_List

    # find count of transaction per month
    def get_Transaction_Count_Month(self):
        tableData = District.df.groupby(['District','Month']).size().to_frame('Count').reset_index()
        return tableData
        
    # find comulative count of transaction 
    def get_Transaction_Count_Comulative(self):
        data = self.get_Transaction_Count_Month()
        return data.cumsum()

    # get transaction count per month as a pivot table
    def get_Transaction_Count_Month_Pivot(self):
        table = self.get_Transaction_Count_Month()
        pvtTable = pd.pivot_table(data=table,values=['Month'],index=['District','Count'])
        return pvtTable

    def get_Transaction_Count_interval(self):
        df = self.districtService.get_Transaction_Count_Interval(self.year)
        return df
            



    #---------------------------- Amount Analysis --------------------------------------
    
    # find total transaction amount 
    def get_Amount_Transaction(self):
        return District.df['TransactionAmount'].sum()

    # get transaction average 
    def get_SumAverage_Transaction(self):
        return np.mean(District.df['TransactionAmount'])

    # get month that has the largest amount of transactions
    def get_MaxTransactions_Amount_Month(self):
        month_Amounts = self.get_Transaction_Sum_Month()
        month_Amounts.sort_values("Month", ascending=False)
        return month_Amounts.head(1)

    #find percentage of months in total transaction
    def get_Percentage_Amount(self): 
        totalAmount = self.get_Amount_Transaction()
        amounts = self.get_Transaction_Sum_Month()
        amounts.sort_values("Month")
        print(amounts)
        percentage_List = []
        for index, row in amounts.iterrows():
            percentage = (row['Count'] / totalAmount) * 100
            obj = {
                "Month":row['Month'],
                "Count":percentage
            }
            percentage_List.append(obj)
        print(percentage_List)
        return percentage_List

    # find sum of transaction per month
    def get_Transaction_Sum_Month(self):
        df = District.df.groupby('Month', sort=False)["TransactionAmount"].sum().reset_index(name ='Count')
        return df.sort_values("Month")

    # find comulative sum of transaction
    def get_Transaction_Sum_Comulative(self):
        groupedData = self.get_Transaction_Sum_Month()
        return groupedData.cumsum()

    # get transaction sum per month as a pivot table
    def get_Transaction_Sum_Month_Pivot(self):
        table = self.get_Transaction_Sum_Month()
        pvtTable = pd.pivot_table(data=table,values=['Month'],index=['District','SUM'])
        return pvtTable


    def get_Transaction_Amount_interval(self):
       df = self.districtService.get_Transaction_Amount_Interval(self.year)
       return df
            




