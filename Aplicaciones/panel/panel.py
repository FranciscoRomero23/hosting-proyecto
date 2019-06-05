# -*- coding: utf-8 -*-
from bottle import route, run, request, template, static_file, redirect, get, response
import bottle
import bottle_session
from beaker.middleware import SessionMiddleware

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
	return template('html/web.tpl')

@route('/panel')
def inicio(session):
	user = session.get('name')
	if user=='None':
		return template('html/login.tpl',user=user)
	else:
		return template('html/inicio.tpl',user=user)

@route('/panel/software')
def software(session):
	user = session.get('name')
	if user=='None':
		return template('html/login.tpl',user=user)
	else:
		return template('html/software.tpl',user=user)

@route('/panel/logs')
def logs(session):
	user = session.get('name')
	if user=='None':
		return template('html/login.tpl',user=user)
	else:
		return template('html/logs.tpl',user=user)

@route('/panel/login',method='GET')
def login_user1(session):
	user = session.get('name')
	return template('html/login.tpl',user=user)

@route('/panel/login',method='POST')
def login_user2(session):
	username = request.forms.get('username')
	password = request.forms.get('password')

	# Leemos la contraseña del webmaster desde un fichero, el cual se crea durante la creación del servidor
	fichero = open ('webmasterpassword.txt','r')
	secretpasswd = fichero.read()[:-1]
	fichero.close()

	if username=='webmaster' and password==secretpasswd:
		session['name'] = username
		user = session.get('name')
		return template('html/inicio.tpl',user=user)
	else:
		session['name'] = 'None'
		user = session.get('name')
		return template('html/login.tpl',user=user)

@route('/panel/logout')
def logout(session):
	session['name'] = 'None'
	redirect ("/panel/login")

@route('/panel/drupal',method='GET')
def drupal1(session):
	user = session.get('name')
	if user=='None':
		return template('html/login.tpl',user=user)
	else:
		return template('html/drupal.tpl',user=user)

@route('/panel/drupal',method='POST')
def drupal2(session):
	user = session.get('name')
	if user=='None':
		return template('html/login.tpl',user=user)
	else:
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

		fichero = open ('/home/usuario/hosting-proyecto/Ansible/group_vars/all','w')
		fichero.write(dominio)
		fichero.write(datosmysql)
		fichero.write(datoscms)
		fichero.close()

		# Instalamos drupal con ansible
		subprocess.call(["ansible-playbook", "/home/usuario/hosting-proyecto/Ansible/site_drupal.yml"])

		return template('html/drupal.tpl',user=user)

@route('/panel/prestashop',method='GET')
def prestashop1(session):
        user = session.get('name')
        if user=='None':
                return template('html/login.tpl',user=user)
        else:
                return template('html/prestashop.tpl',user=user)

@route('/panel/prestashop',method='POST')
def prestashop2(session):
	user = session.get('name')
	if user=='None':
		return template('html/login.tpl',user=user)
	else:
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

		fichero = open ('/home/usuario/hosting-proyecto/Ansible/group_vars/all','w')
		fichero.write(dominio)
		fichero.write(datosmysql)
		fichero.write(datoscms)
		fichero.close()

		# Instalamos prestashop con ansible
		subprocess.call(["ansible-playbook", "/home/usuario/hosting-proyecto/Ansible/site_prestashop.yml"])

		return template('html/prestashop.tpl',user=user)

@route('/panel/mediawiki',method='GET')
def mediawiki1(session):
        user = session.get('name')
        if user=='None':
                return template('html/login.tpl',user=user)
        else:
                return template('html/mediawiki.tpl',user=user)

@route('/panel/mediawiki',method='POST')
def mediawiki2(session):
	user = session.get('name')
	if user=='None':
		return template('html/login.tpl',user=user)
	else:
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

		fichero = open ('/home/usuario/hosting-proyecto/Ansible/group_vars/all','w')
		fichero.write(dominio)
		fichero.write(datosmysql)
		fichero.write(datoscms)
		fichero.close()

		# Instalamos mediawiki con ansible
		subprocess.call(["ansible-playbook", "/home/usuario/hosting-proyecto/Ansible/site_mediawiki.yml"])

		return template('html/mediawiki.tpl',user=user)

@route('/panel/apache-logs')
def logs_apache(session):
        user = session.get('name')
        if user=='None':
                return template('html/login.tpl',user=user)
        else:
                return template('html/apache-logs.tpl',user=user)

@route('/panel/mysql-logs')
def logs_mysql(session):
        user = session.get('name')
        if user=='None':
                return template('html/login.tpl',user=user)
        else:
                return template('html/mysql-logs.tpl',user=user)

@route('/panel/php-logs')
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
