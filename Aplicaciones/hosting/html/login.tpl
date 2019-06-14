<!DOCTYPE html>
<html lang="es">
<html>

<head>
<link href="/style/style.css" rel="stylesheet" />
<link rel="icon" type="image/png" href="/style/images/favicon.png" />
<title>Login</title>
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
        <a class="boton_personalizado" href="/registro">Registro</a>
        <a class="boton_personalizado" href="/login">Login</a>
      </nav>
    </th>
  </tr>
</table>
</header>

<article>
<h1>Inicio de sesión</h1>
	<form action="/login" method="post">
		<input name="username" type="text" placeholder="Nombre de usuario" /><br/>
		<input name="password" type="password" placeholder="Contraseña" /><br/>
		<input value="Login" type="submit" />
        </form>
</article>

<footer>Copyright &copy; Francisco José Romero Morillo, 2019</footer>

</div>

</body>
</html>

