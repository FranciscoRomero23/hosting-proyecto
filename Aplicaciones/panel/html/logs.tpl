<!DOCTYPE html>
<html lang="es">
<html>

<head>
<link href="/style/style.css" rel="stylesheet" />
<link rel="icon" type="image/png" href="/style/images/favicon.png" />
<title>Logs</title>
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
<h1>Logs</h1>
<p>Desde esta pagina podrás consultar los archivos de log de los servicios de tu servidor.</p> 
<p>Puedes ver los logs de los siguientes servicios:</p><br/><br/>
      <nav>
        <a class="boton_opcion" href="/panel/apache-access-log">Logs de Apache (Acceso)</a><br><br>
        <a class="boton_opcion" href="/panel/apache-error-log">Logs de Apache (Errores)</a><br><br>
        <a class="boton_opcion" href="/panel/mysql-error-log">Logs de Mysql (Errores)</a>
      </nav>
</article>

<footer>Copyright &copy; Francisco José Romero Morillo, 2019</footer>

</div>

</body>
</html>
