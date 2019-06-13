<!DOCTYPE html>
<html lang="es">
<html>

<head>
<link href="/style/style.css" rel="stylesheet" />
<link rel="icon" type="image/png" href="/style/images/favicon.png" />
<title>Logs de Apache</title>
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
<h1>Logs de acceso de Apache</h1><br>
<div style="overflow:scroll;height:400px;width:auto;overflow-x:hidden;">
% for i in logs:
<p class="logs">{{i}}</p>
% end
</div>
</article>

<footer>Copyright &copy; Francisco José Romero Morillo, 2019</footer>

</div>

</body>
</html>
