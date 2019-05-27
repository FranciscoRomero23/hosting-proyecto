<!DOCTYPE html>
<html lang="es">
<html>

<head>
<link href="/style/style.css" rel="stylesheet" />
<link rel="icon" type="image/png" href="/style/images/favicon.png" />
<title>Contratar</title>
</head>

<body>

<div class="container">

<header>
<table>
  <tr>
    <th>
      <h1>Auto Hosting</h1>
    </th>
    <th>
    </th>
    <th>
      <nav>
        <a class="boton_personalizado" href="/">Inicio</a>
        <a class="boton_personalizado" href="/servidores">Servidores</a>
	<a class="boton_personalizado" href="/crearserver">Contratar</a>
        <a class="boton_personalizado" href="/perfil">Perfil</a>
        <a class="boton_personalizado" href="/logout">Desconectar</a>
      </nav>
    </th>
  </tr>
</table>
</header>

<article>
  <h1>Contratar un nuevo servidor</h1>
        <form action="/crearserver" method="post">
                Nombre del servidor<br/>
                <input name="name" type="text" /><br/>
                Tipo de servidor<br/>
		<select name="servidor">
			<option value="basico"/>Servidor Básico</option>
			<option value="estandar"/>Servidor Estándar</option>
			<option value="avanzado"/>Servidor Avanzado</option>
		</select><br/>
                Contraseña Webmaster<br/>
                <input name="passwd_webmaster" type="password" /><br/>
                <input value="Contratar" type="submit" />
        </form>
</article>

<footer>Copyright &copy; Francisco José Romero Morillo, 2019</footer>

</div>

</body>
</html>
