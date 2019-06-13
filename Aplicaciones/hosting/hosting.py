# -*- coding: utf-8 -*-
from bottle import route, run, request, template, static_file, redirect,error,get,response
import bottle
import bottle_session
from beaker.middleware import SessionMiddleware
import mysql.connector
import hashlib
import os
import subprocess

session_opts = {
    'session.type': 'memory',
    'session.cookie_expires': 1200,
    'session.auto': True
}

app = bottle.app()
plugin = bottle_session.SessionPlugin(cookie_lifetime=600)
app.install(plugin)

listaservidores = []
user = "None"
@route('/')
def inicio(session):
        user = session.get('name')
        return template('/var/www/html/hosting/html/inicio.tpl',user=user)


@route('/servidores')
def servidores(session):
	user = session.get('name')
	return template('/var/www/html/hosting/html/servidores.tpl',user=user)

@route('/registro',method='GET')
def registro1():
	return template('/var/www/html/hosting/html/registro.tpl')

@route('/registro',method='POST')
def registro2(session):
	name = request.forms.get('name')
	surname = request.forms.get('surname')
	dni = request.forms.get('dni')
	email = request.forms.get('email')
	username = request.forms.get('username')
	password = request.forms.get('password')

	# Conexion con la base de datos
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="hosting",
	  passwd="hosting",
	  database="hosting"
	)

	# Ciframos la contraseña que vamos a registrar
	hashpassword=hashlib.md5(password.encode('utf-8')).hexdigest()

	# Insertamos un nuevo usuario en la base de datos
	mycursor = mydb.cursor()
	sql = "INSERT INTO usuarios VALUES (%s, %s, %s, %s, %s, %s)"
	val = (name, surname, dni, email, username, hashpassword)
	mycursor.execute(sql, val)
	mydb.commit()

	user = session.get('name')
	redirect ("/")

@route('/login',method='GET')
def login_user1(session):
	user = session.get('name')
	return template('/var/www/html/hosting/html/login.tpl',user=user)

@route('/login',method='POST')
def login_user2(session):
	username = request.forms.get('username')
	password = request.forms.get('password')

	# Ciframos la contraseña obtenida en el formulario
	hashpassword=hashlib.md5(password.encode('utf-8')).hexdigest()

	# Conexion con la base de datos
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="hosting",
	  passwd="hosting",
	  database="hosting"
	)

	# Comprobamos si el usuario existe
	mycursor = mydb.cursor()
	sql = "select count(*) from usuarios where username = %s"
	user = (username, )
	mycursor.execute(sql, user)
	records = mycursor.fetchall()
	for row in records:
		usercount=row[0]
	mycursor.close()

	if usercount==0:
		session['name'] = 'None'
		user = session.get('name')
		redirect ("/login")
	else:
		# Conexion con la base de datos
		mydb = mysql.connector.connect(
		  host="localhost",
		  user="hosting",
		  passwd="hosting",
		  database="hosting"
		)

		# Buscamos la contraseña en la base de datos
		mycursor = mydb.cursor()
		sql = "select password from usuarios where username = %s"
		user = (username, )
		mycursor.execute(sql, user)
		records = mycursor.fetchall()

		for row in records:
			newpassword=row[0]
		mycursor.close()

		# Comprobamos que la contraseña introducida no esta vacia
		if password=="":
			session['name'] = 'None'
			user = session.get('name')
			redirect ("/login")
		else:
			# Comparamos los hashes de las contraseñas
			if hashpassword==newpassword:
				session['name'] = username
				user = session.get('name')
				redirect ("/perfil")
			else:
				session['name'] = 'None'
				user = session.get('name')
				redirect ("/login")

@route('/logout')
def logout(session):
	session['name'] = 'None'
	redirect ("/")

@route('/perfil')
def perfil(session):
	user = session.get('name')
	if user=='None':
		redirect ("/")
	else:
		listaservidores = []
		# Conexion con la base de datos
		mydb = mysql.connector.connect(
		  host="localhost",
		  user="hosting",
		  passwd="hosting",
		  database="hosting"
		)

		# Obtenemos el dni del dueño del servidor
		mycursor = mydb.cursor()
		sql = "select dni from usuarios where username = %s"
		user = (user, )
		mycursor.execute(sql, user)
		records = mycursor.fetchall()
		for row in records:
			dni=row[0]
		mycursor.close()

		# Obtenemos la cantidad de servidores que tiene el usuario
		mycursor = mydb.cursor()
		sql = "select count(*) from servidores where user = %s"
		user = (dni, )
		mycursor.execute(sql, user)
		records = mycursor.fetchall()
		for row in records:
			servercount=row[0]
		mycursor.close()

		if servercount==0:
			user = session.get('name')
			return template('/var/www/html/hosting/html/perfil.tpl',user=user,servercount=servercount,listaservidores=listaservidores)
		else:
			# Conexion con la base de datos
			mydb = mysql.connector.connect(
			  host="localhost",
			  user="hosting",
			  passwd="hosting",
			  database="hosting"
			)

			listaservidores = []
			# Obtenemos los datos de los servidores del usuario
			mycursor = mydb.cursor()
			sql = "select name,type from servidores where user = %s"
			user = (dni, )
			mycursor.execute(sql, user)
			records = mycursor.fetchall()
			for row in records:
				listaservidores.append([row[0],row[1]])
			mycursor.close()

			user = session.get('name')
			return template('/var/www/html/hosting/html/perfil.tpl',user=user,servercount=servercount,listaservidores=listaservidores)

@route('/crearserver',method='GET')
def crearserver1(session):
	user = session.get('name')
	if user=='None':
		redirect ("/")
	else:
		return template('/var/www/html/hosting/html/crearserver.tpl',user=user)

@route('/crearserver',method='POST')
def crearserver2(session):
	user = session.get('name')
	name = request.forms.get('name')
	tipo = request.forms.get('servidor')
	passwordpanel = request.forms.get('passwordpanel')

	# Creamos el servidor con terraform
	datosservidor='resource "aws_instance" "%s" {\ninstance_type = "t2.micro"\nami = "ami-023143c216b0108ea"\nkey_name = "amazon"\nvpc_security_group_ids = ["sg-45cbb829"]\ntags = { Name = "%s" }\n}\n'%(str(name),str(name))
	fichero = open ('/var/www/html/hosting/terraform/main.tf','a')
	fichero.write(datosservidor)
	fichero.close()
	os.chdir("/var/www/html/hosting/terraform")
	subprocess.run(["/home/terraform/terraform", "plan"])
	subprocess.run(["/home/terraform/terraform", "apply", "-auto-approve"])

	# Obtenemos la ip publica del servidor
	os.chdir("/var/www/html/hosting/terraform")
	cmd = '/home/terraform/terraform state show aws_instance.%s | grep public_ip | sed 1d | sed "s/ //g" | cut -d"=" -f2 | sed "s/^.//g" | sed "s/.$//g"'%(str(name))
	ip=subprocess.check_output(cmd,shell=True)
	publicip=ip.decode('utf-8')[:-1]

	# Ciframos la contraseña para el panel
	hashpasswordpanel=hashlib.md5(passwordpanel.encode('utf-8')).hexdigest()

	# Modificamos el fichero de variables para la instalación del panel
	nombreserver="---\nserver: %s\npassword: %s\n"%(str(name),hashpasswordpanel)
	fichero = open ('/home/admin/hosting-proyecto/Ansible/group_vars/all','w')
	fichero.write(nombreserver)
	fichero.close()

	# Instalamos el panel en el servidor con ansible

	subprocess.call(["ansible-playbook", "/home/admin/hosting-proyecto/Ansible/panel.yml"])

	# Borramos el servidor del ansible_hosts
	hostserver='[%s]\n%s ansible_ssh_private_key_file=/home/admin/amazon\n'%(str(name),publicip)
	fichero = open ('/etc/ansible/hosts','r')
	cambio = fichero.read()
	cambio = cambio.replace(hostserver,"")
	fichero.close()
	fichero = open ('/etc/ansible/hosts','w')
	fichero.write(cambio)
	fichero.close()

	# Añadimos el servidor al ansible_hosts
	hostserver='[%s]\n%s ansible_ssh_private_key_file=/home/admin/amazon\n'%(str(name),publicip)
	fichero = open ('/etc/ansible/hosts','a')
	fichero.write(hostserver)
	fichero.close()

	# Añadimos el servidor al servidor dns
	newserver='%s %s.autohosting.com\n'%(publicip,str(name))
	fichero = open ('/etc/hosts','a')
	fichero.write(newserver)
	fichero.close()

	# Conexion con la base de datos
	mydb = mysql.connector.connect(
	  host="localhost",
	  user="hosting",
	  passwd="hosting",
	  database="hosting"
	)

	# Obtenemos el dni del dueño del servidor
	mycursor = mydb.cursor()
	sql = "select dni from usuarios where username = %s"
	user = (user, )
	mycursor.execute(sql, user)
	records = mycursor.fetchall()
	for row in records:
		dni=row[0]
	mycursor.close()

	# Insertamos un nuevo servidor en la base de datos
	mycursor = mydb.cursor()
	sql = "INSERT INTO servidores VALUES (%s, %s, %s, %s)"
	val = (name, tipo, dni, publicip)
	mycursor.execute(sql, val)
	mydb.commit()

	# Obtenemos la cantidad de servidores que tiene el usuario
	mycursor = mydb.cursor()
	sql = "select count(*) from servidores where user = %s"
	user = (dni, )
	mycursor.execute(sql, user)
	records = mycursor.fetchall()
	for row in records:
		servercount=row[0]
	mycursor.close()

	listaservidores = []
	# Obtenemos los datos de los servidores del usuario
	mycursor = mydb.cursor()
	sql = "select name,type from servidores where user = %s"
	user = (dni, )
	mycursor.execute(sql, user)
	records = mycursor.fetchall()
	for row in records:
		listaservidores.append([row[0],row[1]])
	mycursor.close()

	user = session.get('name')
	redirect ("/perfil")

@route('/borrarserver/<nameserver>')
def borrarserver(session,nameserver):
	user = session.get('name')
	if user=='None':
		redirect ("/")
	else:
		# Obtenemos la ip publica del servidor
		os.chdir("/var/www/html/hosting/terraform")
		cmd = '/home/terraform/terraform state show aws_instance.%s | grep public_ip | sed 1d | sed "s/ //g" | cut -d"=" -f2 | sed "s/^.//g" | sed "s/.$//g"'%(str(nameserver))
		ip=subprocess.check_output(cmd,shell=True)
		publicip=ip.decode('utf-8')[:-1]

		# Borramos el servidor del servidor dns
		newserver='%s %s.autohosting.com\n'%(publicip,str(nameserver))
		fichero = open("/etc/hosts",'r')
		cambio = fichero.read()
		cambio = cambio.replace(newserver,"")
		fichero.close()
		fichero = open("/etc/hosts",'w')
		fichero.write(cambio)
		fichero.close()

		# Borramos el servidor con terraform
		datosservidor='resource "aws_instance" "%s" {\ninstance_type = "t2.micro"\nami = "ami-023143c216b0108ea"\nkey_name = "amazon"\nvpc_security_group_ids = ["sg-45cbb829"]\ntags = { Name = "%s" }\n}\n'%(str(nameserver),str(nameserver))
		f = open("/var/www/html/hosting/terraform/main.tf",'r')
		cambio = f.read()
		cambio = cambio.replace(datosservidor,"")
		f.close()
		f = open("/var/www/html/hosting/terraform/main.tf",'w')
		f.write(cambio)
		f.close()

		os.chdir("/var/www/html/hosting/terraform")
		subprocess.run(["/home/terraform/terraform", "plan"])
		subprocess.run(["/home/terraform/terraform", "apply", "-auto-approve"])

		# Conexion con la base de datos
		mydb = mysql.connector.connect(
		  host="localhost",
		  user="hosting",
		  passwd="hosting",
		  database="hosting"
		)

		# Borramos el servidor de la base de datos
		mycursor = mydb.cursor()
		sql = "delete from servidores where name = %s"
		borrar = (nameserver, )
		mycursor.execute(sql, borrar)
		mycursor.close()
		mydb.commit()

		# Obtenemos el dni del dueño del servidor
		mycursor = mydb.cursor()
		sql = "select dni from usuarios where username = %s"
		user = (user, )
		mycursor.execute(sql, user)
		records = mycursor.fetchall()
		for row in records:
			dni=row[0]
		mycursor.close()

		# Obtenemos la cantidad de servidores que tiene el usuario
		mycursor = mydb.cursor()
		sql = "select count(*) from servidores where user = %s"
		user = (dni, )
		mycursor.execute(sql, user)
		records = mycursor.fetchall()
		for row in records:
			servercount=row[0]
		mycursor.close()

		listaservidores = []
		# Obtenemos los datos de los servidores del usuario
		mycursor = mydb.cursor()
		sql = "select name,type from servidores where user = %s"
		user = (dni, )
		mycursor.execute(sql, user)
		records = mycursor.fetchall()
		for row in records:
			listaservidores.append([row[0],row[1]])
		mycursor.close()

		user = session.get('name')
		redirect ("/perfil")

@route('/style/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/var/www/html/hosting/html/style')

#run(host='0.0.0.0', port=8080)
