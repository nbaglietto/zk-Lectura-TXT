# zk-Lectura-TXT
Este script lee los datos que se obtienen desde los relojes biometricos, encuentra la ultima fichada de un usuario especifico y le envia con un boot de telegram el horario de entrada y el horario de finalizacion de su jornada laboral.


Utilizando la libreria zklib se genera un TXT con los datos de las fichadas del personal, el fichero tiene el siguiente aspecto:

445:11:01:2023:11:12:02:6666
1254:11:01:2023:11:12:02:6666
1207:11:01:2023:11:15:02:6666
1095:11:01:2023:11:23:02:6666
1246:11:01:2023:11:38:02:6666
1077:11:01:2023:12:00:02:6666
1047:11:01:2023:12:03:02:6666
1169:11:01:2023:12:07:02:6666
1013:11:01:2023:12:16:02:6666
1148:11:01:2023:12:34:02:6666
1135:11:01:2023:13:04:02:6666
1085:11:01:2023:13:14:02:6666
1196:11:01:2023:13:37:02:6666
1188:11:01:2023:13:52:02:6666
1104:11:01:2023:15:07:02:6666
1229:11:01:2023:15:24:02:6666

para generar este archivo se crea una tarea con crontab que ejecuta dicho scriptrado se realiza otra tarea en crontab que ejecuta entradasNahuel.py 
Este archivo busca en el txt un numero de legajo especifico y su ultimo ingreso una vez que tiene esos datos le suma 7 horas al horario de entrada y le envia el msg por telegram al usuario.

Solo funciona con un usuario ya que lo realice para mi pero se podria generar para n usuarios.
