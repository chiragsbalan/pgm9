from flask import Flask, render_template, url_for, request, redirect
import pandas as pd

app = Flask(__name__)

# Load CSV data into pandas dataframes
sp500_companies = pd.read_csv('datasets/sp500_companies.csv')
sp500_stocks = pd.read_csv('datasets/sp500_stocks.csv')
sp500_index = pd.read_csv('datasets/sp500_index.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/companies')
def companies():
    return render_template('companies.html')

@app.route('/stocks')
def stocks():
    return render_template('stocks.html')

if __name__ == "__main__":
    app.run(debug=True)
