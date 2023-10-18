from flask import Flask, render_template, request, redirect

import database as db

app = Flask(__name__)

list = {'posts':['news']}
posts = {'Novo site feito por mim':'foto','':'fototwo','Estou assistindo The men and a half':'','Criando um blog':''}

@app.route('/')
def home():
	return render_template('home.html',list=list,posts=posts)

@app.route('/admin')
def admin():
	return render_template('admin.html',list=list,posts=posts)

if __name__ == '__main__':
	app.run(debug=True, port=5000)