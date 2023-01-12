# zk-Lectura-TXT
Este script lee los datos que se obtienen desde los relojes biometricos, encuentra la ultima fichada de un usuario especifico y le envia con un boot de telegram el horario de entrada y el horario de finalizacion de su jornada laboral.


Utilizando la libreria zklib se genera un TXT con los datos de las fichadas del personal, el fichero tiene el siguiente aspecto:

1254:11:01:2023:11:12:02:6666

1207:11:01:2023:11:15:02:6666

1095:11:01:2023:11:23:02:6666

1246:11:01:2023:11:38:02:6666

1077:11:01:2023:12:00:02:6666

para generar este archivo se crea una tarea con crontab que ejecuta dicho scriptr luego 
se realiza otra tarea en crontab que ejecuta entradasNahuel.py 
Este archivo busca en el txt un numero de legajo especifico y su ultimo ingreso una vez que tiene 
esos datos le suma 7 horas al horario de entrada y le envia el msg por telegram al usuario.

El mensaje que se envia es asi:

Buenos dias Nahuel hoy 11/01/2023 llegastes a las: 15:24 hs. La jornada laboral concluye a las: 22:24Hs.

Solo funciona con un usuario ya que lo realice para mi pero se podria generar para n usuarios.

![telegrammsg](https://user-images.githubusercontent.com/37049113/212178817-d73721c4-06e6-49a0-b0b8-532effd24228.jpeg)
