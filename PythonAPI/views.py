"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from PythonAPI import app
import pandas as pd
from PythonAPI import District as ds

@app.route('/')
@app.route('/home')
def home():
    df = pd.read_excel (r'C:\Users\keds30604\Desktop\PythonDataset.xlsx');
    df['Year'] = pd.DatetimeIndex(df['TransactionDate']).year
    df['Month'] = pd.DatetimeIndex(df['TransactionDate']).month
    df['District'] = df['JournalID'].str[0:3]
    disObj = ds.District(df)
    pd.set_option("display.max_columns", 8)

    averageAmount = disObj.get_SumAverage_Transaction()

    print(averageAmount)

    #data = disObj.get_Transaction_Count_Month()
    #print(data)

    #comulative = disObj.get_Transaction_Count_Comulative()
    #print(comulative)

    #pivotData = disObj.get_Transaction_Count_Month_Pivot()
    #print(pivotData)

    out = df.to_json(orient='records')[1:-1].replace('},{', '} {')
    return out;

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
