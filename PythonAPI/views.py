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
def get_Transaction_Count():
    count = disObj.get_Total_Transaction()
    #out = count.to_json(orient='records')[1:-1].replace('},{', '} {')
    return jsonify(str(count))

@app.route('/getTransactionAverageMonth')
def get_Transaction_Average_Month():
     count = disObj.get_Transaction_Average_Month()
     return jsonify(str(count))

@app.route('/getWithMostBills')
def get_Most_Month_Count():
    mostMonth = disObj.get_MaxTransactions_Count_Month()
    return returnJsonDF(mostMonth)


@app.route('/getMonthsTransaction')
def get_Months_Transactions():
    list = disObj.get_Transaction_Count_Month().to_dict(orient='records')
    return jsonify(list)

@app.route('/getTransactonMonthPercentage')
def getTransactonMonthPercentage():
    return jsonify(disObj.get_Percentage_Count())


@app.route('/getComulativeTransactionCount')
def getComulativeTransactionCount():
    list = disObj.get_Transaction_Count_Comulative().to_dict(orient='records')
    return jsonify(list)

@app.route('/getIntervalTransactions')
def get_Interval_Transactions():
    return returnJsonDF(disObj.get_Transaction_Count_interval())

def returnJsonDF(df):
    list = df.to_dict(orient='records')
    return jsonify(list)






@app.route('/getTransactionAmount')
def transaction_Amount():
    amount = disObj.get_Amount_Transaction()
    return jsonify(str(amount))

@app.route('/getTransactionAverageMonthAmount')
def transaction_Amount_Average_Month():
     amount = disObj.get_SumAverage_Transaction()
     return jsonify(str(amount))

@app.route('/getWithMostBillsAmount')
def month_Most_Amount():
    mostMonth = disObj.get_MaxTransactions_Amount_Month()
    return returnJsonDF(mostMonth)


@app.route('/getMonthsAmountTransaction')
def get_Months_Amount_Transactions():
    list = disObj.get_Transaction_Sum_Month().to_dict(orient='records')
    return jsonify(list)

@app.route('/getTransactonAmountMonthPercentage')
def get_Transacton_Amount_Month_Percentage():
    return jsonify(disObj.get_Percentage_Amount())


@app.route('/getComulativeTransactionAmount')
def get_Comulative_Amount_Transaction():
    list = disObj.get_Transaction_Sum_Comulative().to_dict(orient='records')
    return jsonify(list)

@app.route('/getIntervalTransactionsAmount')
def get_Interval_Amount_Transactions():
    return returnJsonDF(disObj.get_Transaction_Amount_interval())
