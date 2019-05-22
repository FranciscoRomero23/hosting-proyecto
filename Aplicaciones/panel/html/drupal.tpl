<!DOCTYPE html>
<html lang="es">
<html>

<head>
<link href="/style/style.css" rel="stylesheet" />
<link rel="icon" type="image/png" href="/style/images/favicon.png" />
<title>Drupal</title>
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
<h1>Instalación de Drupal</h1>
<p>Desde esta página podras instalar un Drupal en tu servidor. Para que se pueda realizar la instalación, necesito que nos facilites los siguientes datos:</p><br/>
<form action="/panel/drupal" method="post">
	Base de datos<br/>
	<input name="namedb" type="text" size="30" /><br/>
	Usuario<br/>
	<input name="userdb" type="text" size="30" /><br/>
	Clave<br/>
	<input name="passdb" type="password" size="30" /><br/><br/>
	Dominio<br/>
	<input name="domain" type="text" size="30" /><br/>
	Nombre del sitio web<br/>
	<input name="site_name" type="text" size="30" /><br/><br/>
	Nombre de administrador<br/>
	<input name="admin_name" type="text" size="30" /><br/>
	Clave de administrador<br/>
	<input name="admin_passwd" type="password" size="30" /><br/>
	Nombre de usuario<br/>
	<input name="name_user" type="text" size="30" /><br/>
	Apellido de usuario<br/>
	<input name="surname_user" type="text" size="30" /><br/>
	<input value="Instalar" type="submit" />
</form>
</article>

<footer>Copyright &copy; Francisco José Romero Morillo, 2019</footer>

</div>

</body>
</html>
