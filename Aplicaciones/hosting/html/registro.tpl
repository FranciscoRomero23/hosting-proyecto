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
  <p>Aquí podras crear una nueva cuenta de usuario para gestionar tus servidores. Inserta los datos siguientes:</p>
        <form action="/registro" method="post">
                <input name="name" type="text" placeholder="Nombre" />
                <input name="surname" type="text" placeholder="Apellidos" /><br/>
                <input name="dni" type="text" placeholder="DNI" />
                <input name="email" type="text" placeholder="Correo Electrónico" /><br>
                <input name="username" type="text" placeholder="Nombre de usuario" />
                <input name="password" type="password" placeholder="Contraseña" /><br/>
                <input value="Registrarse" type="submit" />
        </form>
</article>

<footer>Copyright &copy; Francisco José Romero Morillo, 2019</footer>

</div>

</body>
</html>

