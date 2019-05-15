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
  <h1>Servidores en Auto Hosting</h1>
  <p>En Auto Hosting disponemos de los siguientes servidores:</p>
  <h2>Servidor Básico</h2>
  <p>El servidor básico es el que menor categoría tiene entre los servidores que tenemos en Auto Hosting. Dispone de 1 GB de memoria RAM, 1 CPU y 20 GB de disco duro.</p>
  <h2>Servidor Estándar</h2>
  <p>El servidor estándar es el servidor de gama media entre  los servidores que tenemos en Auto Hosting. Dispone de 2 GB de memoria RAM, 1 CPU y 30 GB de disco duro.</p>
  <h2>Servidor Avanzado</h2>
  <p>El servidor avanzado es el mejor servidor que de momento tenemos en Auto Hosting. Dispone de 2 GB de memoria RAM, 2 CPUs y 40 GB de disco duro.</p>
</article>

<footer>Copyright &copy; Francisco José Romero Morillo, 2019</footer>

</div>

</body>
</html>
