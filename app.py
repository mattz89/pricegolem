# -----------------------------------------------------------
# This app tracks the prices of items and sends a text 
# message when the item reaches your desired 'buy price'.
#
# Copyright (c) 2020 Matthew Zenittini
# Released under MIT License
# Email matt@playstowin.com
# -----------------------------------------------------------

# Standard Library Imports
import os

# Third Party Imports
from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

# Local Imports
import pricechecker


app = Flask(__name__)

# ---------------
# App Settings  
# ---------------
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)


# ---------------
# Models  
# ---------------
class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    selling_price = db.Column(db.String(255))
    imageurl = db.Column(db.String(255))
    buy_price = db.Column(db.String(255))
    link = db.Column(db.String(255))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(255))


# ---------------
# Main Routes   
# ---------------
@app.route('/')
def index():
    items = pricechecker.get_items()

    return render_template('index.html', items=items)


# Html button to test price check function
@app.route('/test_price_check', methods=['POST'])
def test_price_check():
    pricechecker.price_check()

    return redirect(url_for('index'))


# Add item page
@app.route('/add')
def add():
    
    return render_template('add.html')


# Add new item to db
@app.route('/submit', methods=['POST'])
def add_submit():
    link = request.form['link']
    buy_price = request.form['price']
    pricechecker.create_item(link, buy_price)

    return redirect(url_for('index'))


# Add MBP to DB with higher price for testing refresh + text
@app.route('/macbook')
def macbook():
    item = Items(title='Macbook Pro', selling_price='1550', imageurl='https://static.bhphoto.com/images/images500x500/apple_mxk32ll_a_13_3_macbook_pro_with_1588701104_1560523.jpg', buy_price='1300', link='https://www.bhphotovideo.com/c/product/1560523-REG/apple_mxk32ll_a_13_3_macbook_pro_with.html')
    db.session.add(item)
    db.session.commit()

    return redirect(url_for('index'))


# Creates CLI command that updates prices with 'flask update-prices'
@app.cli.command()
def update_prices():
    pricechecker.price_check()
    print('Price Check job complete.')


# ---------------
# Auth Routes  
# ---------------
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/logout')
def logout():
    return 'logout'


@app.route('/profile')
def profile():
    return render_template('profile.html')