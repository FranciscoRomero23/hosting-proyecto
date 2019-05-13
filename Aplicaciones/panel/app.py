# -*- coding: utf-8 -*-
from bottle import route, run, request, template, static_file, redirect, get, response
import bottle
import bottle_session

app = bottle.app()
plugin = bottle_session.SessionPlugin(cookie_lifetime=600)
app.install(plugin)

@route('/')
def inicio(session):
	user = session.get('name')
	if user=='None':
		return template('html/login.tpl',user=user)
	else:
		return template('html/inicio.tpl',user=user)

@route('/software')
def software(session):
	user = session.get('name')
	if user=='None':
		return template('html/login.tpl',user=user)
	else:
		return template('html/software.tpl',user=user)

@route('/logs')
def logs(session):
	user = session.get('name')
	if user=='None':
		return template('html/login.tpl',user=user)
	else:
		return template('html/logs.tpl',user=user)

@route('/login',method='GET')
def login_user1(session):
	user = session.get('name')
	return template('html/login.tpl',user=user)

@route('/login',method='POST')
def login_user2(session):
	username = request.forms.get('username')
	password = request.forms.get('password')
	passwd = "francisco"
	if password==passwd:
		session['name'] = username
		user = session.get('name')
		return template('html/inicio.tpl',user=user)
	else:
		session['name'] = 'None'
		user = session.get('name')
		return template('html/login.tpl',user=user)

@route('/logout')
def logout(session):
	session['name'] = 'None'
	redirect ("/login")

@route('/drupal')
def drupal(session):
        user = session.get('name')
        if user=='None':
                return template('html/login.tpl',user=user)
        else:
                return template('html/drupal.tpl',user=user)

@route('/prestashop')
def prestashop(session):
        user = session.get('name')
        if user=='None':
                return template('html/login.tpl',user=user)
        else:
                return template('html/prestashop.tpl',user=user)

@route('/mediawiki')
def mediawiki(session):
        user = session.get('name')
        if user=='None':
                return template('html/login.tpl',user=user)
        else:
                return template('html/mediawiki.tpl',user=user)

@route('/apache-logs')
def logs_apache(session):
        user = session.get('name')
        if user=='None':
                return template('html/login.tpl',user=user)
        else:
                return template('html/apache-logs.tpl',user=user)

@route('/mysql-logs')
def logs_mysql(session):
        user = session.get('name')
        if user=='None':
                return template('html/login.tpl',user=user)
        else:
                return template('html/mysql-logs.tpl',user=user)

@route('/php-logs')
def logs_php(session):
        user = session.get('name')
        if user=='None':
                return template('html/login.tpl',user=user)
        else:
                return template('html/php-logs.tpl',user=user)

@route('/style/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='html/style')

run(host='0.0.0.0', port=8080)
