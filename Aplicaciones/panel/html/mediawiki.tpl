<!DOCTYPE html>
<html lang="es">
<html>

<head>
<link href="/style/style.css" rel="stylesheet" />
<link rel="icon" type="image/png" href="/style/images/favicon.png" />
<title>Mediawiki</title>
</head>

<body>

<div class="container">

<header>
<table>
  <tr>
    <th>
      <h1>Panel de control</h1>
    </th>
    <th>
    </th>
    <th>
      <nav>
        <a class="boton_personalizado" href="/panel">Inicio</a>
        <a class="boton_personalizado" href="/panel/software">Software</a>
        <a class="boton_personalizado" href="/panel/logs">Logs</a>
        <a class="boton_personalizado" href="/panel/logout">Desconectar</a>
      </nav>
    </th>
  </tr>
</table>
</header>

<article>
<h1>Instalación de Mediawiki</h1>
<p>Desde esta página podras instalar un Mediawiki en tu servidor. Para que se pueda realizar la instalación, inserta los siguientes datos:</p>
<form action="/panel/mediawiki" method="post">
	<input name="namedb" type="text" size="20" placeholder="Nombre base de datos"/>
	<input name="userdb" type="text" size="20" placeholder="Usuario base de datos"/>
	<input name="passdb" type="password" size="20" placeholder="Contraseña base de datos"/><br/><br/>

	<input name="domain" type="text" size="33" placeholder="Dominio"/>
	<input name="site_name" type="text" size="32" placeholder="Nombre del sitio web"/><br/><br/>

	<input name="admin_name" type="text" size="33" placeholder="Nombre del administrador" />
	<input name="admin_passwd" type="password" size="32" placeholder="Clave del administrador"/><br/><br/>

	<input name="name_user" type="text" size="33" placeholder="Nombre de usuario" />
	<input name="surname_user" type="text" size="32" placeholder="Apellido de usuario" /><br/>
	<input value="Instalar" type="submit" />
</form>
</article>

<footer>Copyright &copy; Francisco José Romero Morillo, 2019</footer>

</div>

</body>
</html>
