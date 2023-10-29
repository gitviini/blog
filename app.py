from flask import Flask, render_template, request, redirect

import database as db

app = Flask(__name__)

list = {'posts':['news']}
posts = {'Novo site feito por mim':'foto','':'fototwo','Estou assistindo The men and a half':'','Criando um blog':''}

@app.route('/')
def index():
	return render_template('login.html')

@app.post('/login')
def login():
    name_email = request.form['name_email']
    password = request.form['password']
    print(name_email+'\n'+password)
    return redirect('/home')

@app.post('/sign')
def sign():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    print(name+'\n'+email+'\n'+password)
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('home.html',list=list,posts=posts)

@app.route('/admin')
def admin():
	return render_template('admin.html',list=list,posts=posts)

if __name__ == '__main__':
	app.run(debug=True, port=5000)
