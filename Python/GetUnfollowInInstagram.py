# Procesar y comparar los archivos subidos para identificar usuarios que sigues pero no te siguen.
import json

# Solicitar a instagram (Tu actividad -> Descarga de información). Seguir los pasos y esperar a que llege la informacion solicitada. 
# Link sobre como realizar la descarga: https://www.movilzona.es/noticias/aplicaciones/descargar-informacion-instagram-sobre-ti/
# Rango de fecha: Desde el inicio de los tiempos. En formato JSON. Puedes solicitar solo la informacion de Seguidores y Seguidos, por no descargar toda la informacion.
# Se te descargara un archivo .zip , pero solo nos interesa la parte de seguidores/seguidos. Buscar los siguientes archivos (followers_1.json ; following.json) e incluir la ruta en la variable: 
# Ejemplo de como deberia quedar la variable followers_path = "C:......\\followers_1.json"
# Ejemplo de como deberia quedar la variable following_path = "C:......\\following.json"

# Rutas de los archivos JSON
followers_path = "INCLUIR RUTA ARCHIVO (followers_1.json)"
following_path = " INCLUIR RUTA ARCHIVO (following.json) "

# Cargar la lista de seguidores y seguidos
with open(followers_path, 'r') as f:
    followers_data = json.load(f)
with open(following_path, 'r') as f:
    following_data = json.load(f)

followers_usernames = {entry['string_list_data'][0]['value'] for entry in followers_data}
following_usernames = {entry['string_list_data'][0]['value'] for entry in following_data['relationships_following']}
not_following_back = following_usernames - followers_usernames

not_following_back_list = list(not_following_back)
print(f"Usuarios que no te siguen de vuelta ({len(not_following_back_list)}):")
for username in not_following_back_list:
    print(username)
