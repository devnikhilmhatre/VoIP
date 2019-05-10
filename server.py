from flask import Flask, render_template
app = Flask(__name__)
#
"""Experimental code"""
# def generate_stock_table():
#     yield render_template('index.html')
#     # for stock in Stock.query.all():
#     # yield render_template('stock_row.html', stock=stock)
#     yield render_template('index.html')


@app.route('/')
def hello_world():
    # return Response(generate_stock_table())
    return render_template('index.html')
