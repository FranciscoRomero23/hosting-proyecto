<!DOCTYPE html>
<html lang="es">
<html>

<head>
<link href="/style/style.css" rel="stylesheet" />
<link rel="icon" type="image/png" href="/style/images/favicon.png" />
<title>Perfil</title>
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
  <h1>Perfil de {{user}}</h1>
  <p>Bienvenido a tu perfil, {{user}}.</p>
  <p>Desde esta página podras administrar tus servidores en Auto Hosting.
% if servercount==0:
  <p>Aun no tienes servidores para administrar</p>
% else:
  <p>Tus servidores para administrar son:</p>
% for server in listaservidores:

<table border="2" bordercolor="black">
  <tr>
    <td width="80" align="left"><b>Servidor:</b></td>
    <td width="100" align="left">{{server[0]}}</td>
    <td width="50" align="left"><b>Tipo:</b></td>
    <td width="100" align="left">{{server[1]}}</td>
    <td>
    <a class="boton_servidor" href="http://{{server[0]}}.autohosting.com">Administrar</a>
    </td>
    <td>
    <a class="boton_servidor" href="/borrarserver/{{server[0]}}">Dar de baja</a>
    </td>
  </tr>
</table>
<br/>
% end
% end

</article>

<footer>Copyright &copy; Francisco José Romero Morillo, 2019</footer>

</div>

</body>
</html>
