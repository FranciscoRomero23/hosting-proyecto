<!DOCTYPE html>
<html lang="es">
<html>

<head>
<link href="/style/style.css" rel="stylesheet" />
<link rel="icon" type="image/png" href="/style/images/favicon.png" />
<title>Registro</title>
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
  <h1>Registro</h1>
        <form action="/registro" method="post">
                Nombre<br/>
                <input name="name" type="text" /><br/>
                Apellidos<br/>
                <input name="surname" type="text" /><br/>
                DNI<br/>
                <input name="dni" type="text" /><br/>
                Correo electrónico<br/>
                <input name="email" type="text" /><br/>
                Usuario<br/>
                <input name="username" type="text" /><br/>
                Clave<br/>
                <input name="password" type="password" /><br/>
                <input value="Registrarse" type="submit" />
        </form>
</article>

<footer>Copyright &copy; Francisco José Romero Morillo, 2019</footer>

</div>

</body>
</html>
