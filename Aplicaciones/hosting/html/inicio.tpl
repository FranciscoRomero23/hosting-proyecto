<!DOCTYPE html>
<html lang="es">
<html>

<head>
<link href="/style/style.css" rel="stylesheet" />
<link rel="icon" type="image/png" href="/style/images/favicon.png" />
<title>Inicio</title>
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
  <h1>El hosting automatico</h1>
  <p>Bienvenido a la página principal de Auto Hosting, un hosting automatizado mediante el uso de los servicios de Ansible y Terraform.</p>
  <p>Desde nuestra página podrás contratar el servidor que más se ajuste a las necesidades de tu sitio web.</p>
  <p>Puedes ver los servidores que tenemos disponibles para contratar en la pestaña <i>Servidores</i>.</p>
</article>

<footer>Copyright &copy; Francisco José Romero Morillo, 2019</footer>

</div>

</body>
</html>
