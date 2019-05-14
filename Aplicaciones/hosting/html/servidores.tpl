<!DOCTYPE html>
<html lang="es">
<html>

<head>
<link href="/style/style.css" rel="stylesheet" />
<link rel="icon" type="image/png" href="/style/images/favicon.png" />
<title>Servidores</title>
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
% if user=='None':
      <nav>
        <a class="boton_personalizado" href="/">Inicio</a>
        <a class="boton_personalizado" href="/servidores">Servidores</a>
        <a class="boton_personalizado" href="/registro">Registro</a>
        <a class="boton_personalizado" href="/login">Login</a>
      </nav>
% else:
      <nav>
        <a class="boton_personalizado" href="/">Inicio</a>
        <a class="boton_personalizado" href="/servidores">Servidores</a>
        <a class="boton_personalizado" href="/perfil">Perfil</a>
        <a class="boton_personalizado" href="/logout">Desconectar</a>
      </nav>
% end
    </th>
  </tr>
</table>
</header>

<article>
  <h1>Tipos de Servidores</h1>
  <h2>Servidor 1</h2>
  <p>Este servidor tiene 1 gb de ram, 1 cpu virtual y 20 gb de disco duro.</p>
  <h2>Servidor 2</h2>
  <p>Este servidor tiene 2 gb de ram, 2 cpu virtual y 30 gb de disco duro.</p>
  <h2>Servidor 3</h2>
  <p>Este servidor tiene 2 gb de ram, 1 cpu virtual y 30 gb de disco duro.</p>
</article>

<footer>Copyright &copy; Francisco José Romero Morillo, 2019</footer>

</div>

</body>
</html>
