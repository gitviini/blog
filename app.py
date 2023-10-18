from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
	list = {'posts':['news']}
	posts = {'Novo site feito por mim':'foto','':'fototwo','Estou assistindo The men and a half':'','Criando um blog':''}
	return render_template('home.html',list=list,posts=posts)

if __name__ == '__main__':
	app.run(debug=True, port=5000)