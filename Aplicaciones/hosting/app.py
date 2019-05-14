# -*- coding: utf-8 -*-
from bottle import route, run, request, template, static_file, redirect,error,get,response
import bottle
import bottle_session

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
def registro2():
	name = request.forms.get('name')
	surname = request.forms.get('surname')
	dni = request.forms.get('dni')
	email = request.forms.get('email')
	username = request.forms.get('username')
	password = request.forms.get('password')
	# Insertar datos nuevo usuario en base de datos

@route('/login',method='GET')
def login_user1(session):
	user = session.get('name')
	return template('html/login.tpl',user=user)

@route('/login',method='POST')
def login_user2(session):
	username = request.forms.get('username')
	password = request.forms.get('password')
	# Buscar la clave para el usuario $username.
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

run(host='0.0.0.0', port=8080)
