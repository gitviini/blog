import sqlite3 as sq

def connect():
	try:
		con = sq.connect('banco.db')
		cur = con.cursor()
		return con, cur
	except Exception as erro: print(erro)
	finally: con.commit()

def create_table():
	try:
		con, cur = connect()
		cur.execute('''
			CREATE TABLE posts(
				post TEXT NOT NULL,
				foto BLOB NOT NULL
			)''')
	except Exception as erro: print(erro)
	finally: con.commit()

def select_post():
	try:
		con, cur = connect()
		cur.execute('SELECT * FROM posts')
		return cur.fetchall()
	except Exception as erro: print(erro)
	finally: con.commit()

def insert_post(post='',foto=''):
	try:
		con, cur = connect()
		cur.execute(f'INSERT INTO posts(post, foto) VALUES("{post}",foto)')
	except Exception as erro: print(erro)
	finally: con.commit()


def delete_post(post=''):
	try:
		con, cur = connect()
		cur.execute(f'DELETE * FROM posts WHERE post = "{post}"')
	except Exception as erro: print(erro)
	finally: con.commit()