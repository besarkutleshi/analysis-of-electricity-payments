import pyodbc
class DbConnection():
    
    def get_Connection(self):
        server = '' 
        database = '' 
        username = '' 
        password = ''  
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        return conn


