import pyodbc
class DbConnection():
    
    def get_Connection(self):
        server = '10.150.1.70' 
        database = 'REPORTS' 
        username = 'besark' 
        password = 'besark'  
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        return conn


