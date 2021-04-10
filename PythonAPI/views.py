from datetime import datetime
from flask import render_template
from PythonAPI import app
import pandas as pd
from PythonAPI import District as ds
from flask import jsonify


disObj = ds.District()


@app.route('/')
@app.route('/home')
def home():
    return jsonify(str(1))

@app.route('/getAllTransaction/<district>/<year>')
def allTransaction(district,year):
    print(district)
    print(year)
    disObj = ds.District(year,str(district))
    disObj.get_All_Transaction()
    return jsonify(str(1))

@app.route('/getTransactionCount')
def transactionCount():
    count = disObj.get_Total_Transaction()
    #out = count.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(str(count))

@app.route('/getTransactionAverageMonth')
def transactionAverageMonth():
     count = disObj.get_Transaction_Average_Month()
     return jsonify(str(count))

@app.route('/getWithMostBills')
def about():
    mostMonth = disObj.get_MaxTransactions_Count_Month()
    return mostMonth.to_json(orient='records')[1:-1].replace('},{', '} {')


@app.route('/getMonthsTransaction')
def getMonthsTransactions():
    list = disObj.get_Transaction_Count_Month().to_dict(orient='records')
    return jsonify(list)

@app.route('/getTransactonMonthPercentage')
def getTransactonMonthPercentage():
    return jsonify(disObj.get_Percentage_Count())


@app.route('/getComulativeTransactionCount')
def getComulativeTransactionCount():
    print(disObj.get_Transaction_Count_Comulative())
    list = disObj.get_Transaction_Count_Comulative().to_dict(orient='records')
    return jsonify(list)

@app.route('/getIntervalTransactions')
def get_Interval_Transactions():
    return returnJsonDF(disObj.get_Transaction_Count_interval())

def returnJsonDF(df):
    list = df.to_dict(orient='records')
    return jsonify(list)