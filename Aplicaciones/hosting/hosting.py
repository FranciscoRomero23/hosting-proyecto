# -*- coding: utf-8 -*-
from bottle import route, run, request, template, static_file, redirect,error,get,response
import bottle
import bottle_session
from beaker.middleware import SessionMiddleware
import mysql.connector

session_opts = {
    'session.type': 'memory',
    'session.cookie_expires': 1200,
    'session.auto': True
}

app = bottle.app()
plugin = bottle_session.SessionPlugin(cookie_lifetime=600)
app.install(plugin)

@route('/')
def inicio(session):
        user = session.get('name')
        return template('html/inicio.tpl',user=user)


@route('/servidores')
def servidores(session):
	user = session.get('name')
	return template('html/servidores.tpl',user=user)

@route('/perfil')
def perfil(session):
	user = session.get('name')
	if user=='None':
		redirect ("/")
	else:
		return template('html/perfil.tpl',user=user)

@route('/registro',method='GET')
def registro1():
	return template('html/registro.tpl')

@route('/registro',method='POST')
def registro2(session):
	name = request.forms.get('name')
	surname = request.forms.get('surname')
	dni = request.forms.get('dni')
	email = request.forms.get('email')
	username = request.forms.get('username')
	password = request.forms.get('password')

	mydb = mysql.connector.connect(
	  host="localhost",
	  user="root",
	  passwd="usuario",
	  database="hosting"
	)
	mycursor = mydb.cursor()
	sql = "INSERT INTO usuarios VALUES (%s, %s, %s, %s, %s, %s)"
	val = (name, surname, dni, email, username, password)
	mycursor.execute(sql, val)
	mydb.commit()

	user = session.get('name')
	return template('html/inicio.tpl',user=user)

@route('/login',method='GET')
def login_user1(session):
	user = session.get('name')
	return template('html/login.tpl',user=user)

@route('/login',method='POST')
def login_user2(session):
	username = request.forms.get('username')
	password = request.forms.get('password')

#	mydb = mysql.connector.connect(
#	  host="localhost",
#	  user="root",
#	  passwd="usuario",
#	  database="hosting"
#	)
#	mycursor = mydb.cursor()
#	sql = "select password from usuarios where username = %s"
#	user = (username, )
#	mycursor.execute(sql, user)
#	myresult = mycursor.fetchall()
#	print(myresult)

	passwd = 'francisco'

	if password==passwd:
		session['name'] = username
		user = session.get('name')
		redirect ("/perfil")
	else:
		session['name'] = 'None'
		user = session.get('name')
		return template('html/login.tpl',user=user)

@route('/logout')
def logout(session):
	session['name'] = 'None'
	redirect ("/")


@route('/style/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='html/style')

#run(host='0.0.0.0', port=8080)
