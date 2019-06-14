# -*- coding: utf-8 -*-
from bottle import route, run, request, template, static_file, redirect, get, response
import bottle
import bottle_session
from beaker.middleware import SessionMiddleware
import subprocess
import hashlib

session_opts = {
    'session.type': 'memory',
    'session.cookie_expires': 1200,
    'session.auto': True
}

app = bottle.app()
plugin = bottle_session.SessionPlugin(cookie_lifetime=600)
app.install(plugin)

user = "None"
@route('/')
def web():
	return template('/var/www/html/panel/html/web.tpl')

@route('/panel')
def inicio(session):
	user = session.get('name')
	if user=='None':
		redirect ("/panel/login")
	else:
		return template('/var/www/html/panel/html/inicio.tpl',user=user)

@route('/panel/software')
def software(session):
	user = session.get('name')
	if user=='None':
		redirect ("/panel/login")
	else:
		return template('/var/www/html/panel/html/software.tpl',user=user)

@route('/panel/logs')
def logs(session):
	user = session.get('name')
	if user=='None':
		redirect ("/panel/login")
	else:
		return template('/var/www/html/panel/html/logs.tpl',user=user)

@route('/panel/login',method='GET')
def login_user1(session):
	user = session.get('name')
	return template('/var/www/html/panel/html/login.tpl',user=user)

@route('/panel/login',method='POST')
def login_user2(session):
	username = request.forms.get('username')
	password = request.forms.get('password')

	# Ciframos la contraseña obtenida desde el formulario
	hashpassword=hashlib.md5(password.encode('utf-8')).hexdigest()

	# Leemos la contraseña desde el fichero passwordfile
	fichero = open ('/var/www/html/panel/passwordfile','r')
	passwordfile = fichero.read()
	fichero.close()
	passwordfile = passwordfile[:-1]

	if username=='webmaster' and hashpassword==passwordfile:
		session['name'] = username
		user = session.get('name')
		redirect ("/panel")
	else:
		session['name'] = 'None'
		user = session.get('name')
		redirect ("/panel/login")

@route('/panel/logout')
def logout(session):
	session['name'] = 'None'
	redirect ("/panel/login")

@route('/panel/drupal',method='GET')
def drupal1(session):
	user = session.get('name')
	if user=='None':
		redirect ("/panel/login")
	else:
		return template('/var/www/html/panel/html/drupal.tpl',user=user)

@route('/panel/drupal',method='POST')
def drupal2(session):
	user = session.get('name')

	namedb = request.forms.get('namedb')
	userdb = request.forms.get('userdb')
	passdb = request.forms.get('passdb')
	domain = request.forms.get('domain')
	site_name = request.forms.get('site_name')
	admin_name = request.forms.get('admin_name')
	admin_passwd = request.forms.get('admin_passwd')
	name_user = request.forms.get('name_user')
	surname_user = request.forms.get('surname_user')

	# Modificamos el fichero de variables para la instalación
	dominio="---\ndomain: %s\n"%(str(domain))
	datosmysql="mysql_db: %s\nmysql_user: %s\nmysql_password: %s\n"%(str(namedb),str(userdb),str(passdb))
	datoscms='site_name: "%s"\nadmin_user: %s\nadmin_password: %s\nname_user: %s\nsurname_user: %s'%(str(site_name),str(admin_name),str(admin_passwd),str(name_user),str(surname_user))

	fichero = open ('/home/admin/hosting-proyecto/Ansible/group_vars/all','w')
	fichero.write(dominio)
	fichero.write(datosmysql)
	fichero.write(datoscms)
	fichero.close()

	# Instalamos drupal con ansible
	subprocess.call(["ansible-playbook", "/home/admin/hosting-proyecto/Ansible/site_drupal.yml"])
	redirect ("/panel/drupal")

@route('/panel/prestashop',method='GET')
def prestashop1(session):
	user = session.get('name')
	if user=='None':
		redirect ("/panel/login")
	else:
		return template('/var/www/html/panel/html/prestashop.tpl',user=user)

@route('/panel/prestashop',method='POST')
def prestashop2(session):
	user = session.get('name')

	namedb = request.forms.get('namedb')
	userdb = request.forms.get('userdb')
	passdb = request.forms.get('passdb')
	domain = request.forms.get('domain')
	site_name = request.forms.get('site_name')
	admin_name = request.forms.get('admin_name')
	admin_passwd = request.forms.get('admin_passwd')
	name_user = request.forms.get('name_user')
	surname_user = request.forms.get('surname_user')

	# Modificamos el fichero de variables para la instalación
	dominio="---\ndomain: %s\n"%(str(domain))
	datosmysql="mysql_db: %s\nmysql_user: %s\nmysql_password: %s\n"%(str(namedb),str(userdb),str(passdb))
	datoscms='site_name: "%s"\nadmin_user: %s\nadmin_password: %s\nname_user: %s\nsurname_user: %s'%(str(site_name),str(admin_name),str(admin_passwd),str(name_user),str(surname_user))

	fichero = open ('/home/admin/hosting-proyecto/Ansible/group_vars/all','w')
	fichero.write(dominio)
	fichero.write(datosmysql)
	fichero.write(datoscms)
	fichero.close()

	# Instalamos prestashop con ansible
	subprocess.call(["ansible-playbook", "/home/admin/hosting-proyecto/Ansible/site_prestashop.yml"])
	redirect ("/panel/prestashop")

@route('/panel/mediawiki',method='GET')
def mediawiki1(session):
	user = session.get('name')
	if user=='None':
		redirect ("/panel/login")
	else:
		return template('/var/www/html/panel/html/mediawiki.tpl',user=user)

@route('/panel/mediawiki',method='POST')
def mediawiki2(session):
	user = session.get('name')

	namedb = request.forms.get('namedb')
	userdb = request.forms.get('userdb')
	passdb = request.forms.get('passdb')
	domain = request.forms.get('domain')
	site_name = request.forms.get('site_name')
	admin_name = request.forms.get('admin_name')
	admin_passwd = request.forms.get('admin_passwd')
	name_user = request.forms.get('name_user')
	surname_user = request.forms.get('surname_user')

	# Modificamos el fichero de variables para la instalación
	dominio="---\ndomain: %s\n"%(str(domain))
	datosmysql="mysql_db: %s\nmysql_user: %s\nmysql_password: %s\n"%(str(namedb),str(userdb),str(passdb))
	datoscms='site_name: "%s"\nadmin_user: %s\nadmin_password: %s\nname_user: %s\nsurname_user: %s'%(str(site_name),str(admin_name),str(admin_passwd),str(name_user),str(surname_user))

	fichero = open ('/home/admin/hosting-proyecto/Ansible/group_vars/all','w')
	fichero.write(dominio)
	fichero.write(datosmysql)
	fichero.write(datoscms)
	fichero.close()

	# Instalamos mediawiki con ansible
	subprocess.call(["ansible-playbook", "/home/admin/hosting-proyecto/Ansible/site_mediawiki.yml"])
	redirect ("/panel/mediawiki")

@route('/panel/apache-access-log')
def logs_apache(session):
	user = session.get('name')
	if user=='None':
		redirect ("/panel/login")
	else:
		archivolog=open('/var/www/html/panel/apache-access-log','r')
		logs=archivolog.readlines()
		return template('/var/www/html/panel/html/apache-access-log.tpl',user=user,logs=logs)

@route('/panel/apache-error-log')
def logs_apache(session):
	user = session.get('name')
	if user=='None':
		redirect ("/panel/login")
	else:
		archivolog=open('/var/www/html/panel/apache-error-log','r')
		logs=archivolog.readlines()
		return template('/var/www/html/panel/html/apache-error-log.tpl',user=user,logs=logs)

@route('/panel/mysql-error-log')
def logs_mysql(session):
	user = session.get('name')
	if user=='None':
		redirect ("/panel/login")
	else:
		archivolog=open('/var/www/html/panel/mysql-error-log','r')
		logs=archivolog.readlines()
		return template('/var/www/html/panel/html/mysql-error-log.tpl',user=user,logs=logs)


@route('/style/<filepath:path>')
def server_static(filepath):
	return static_file(filepath, root='/var/www/html/panel/html/style')

#run(host='0.0.0.0', port=8080)
