from dotenv import load_dotenv
import os
import requests
import utilidades.utilidades_shell as sUtils
from colecciones.comandos import COMANDOS
from colecciones.mensajes import MENSAJES


# Función que toma un mensaje y lo envia al agente IA, retorna la respuesta del agente como cadena de texto
def atacarAPI(mensaje):
    # Cargar varaibles del .env
    load_dotenv()
    urlAPI = os.getenv("AI_API_URL")
    claveAPI = os.getenv("AI_API_KEY")
    modelo = os.getenv("AI_MODEL")

    #region PETICION
    # Se arma la petición usando la URL, clave y modelo
    # Se crea el cuerpo del mensaje
    data = {
        "model": modelo,
        "messages": [{"role": "user", "content": mensaje}],
        #"max_tokens": 50 //TODO posible mejora, pasar por parametro a la función que cantidad de tokens usar puede ser conveniente para ahorrar a futuro en tareas menos importantes
    }

    # Headers con autorización
    headers = {
        "Authorization": f"Bearer {claveAPI}",
        "Content-Type": "application/json"
    }

    # Hacer la petición POST
    response = requests.post(urlAPI, headers=headers, json=data)

    # Revisar si hubo error
    if response.status_code != 200:
        print("Error al contactar la API:", response.status_code, response.text)
        return None
    #endregion

    # Extraer texto de la IA
    resultado = response.json()
    respuesta = resultado["choices"][0]["message"]["content"]
    return respuesta

# Explora los permisos de la app y devuelve la lista de permisos ya tratada como cadena de texto
def explorarPermisos(dispositivo, appSeleccionada):
    permisosSinProcesar = sUtils.extraerPermisos(dispositivo, appSeleccionada)
    
    # Abrir y leer un archivo completo
    with open("prompts/PERMISOS.txt", "r", encoding="utf-8") as f:
        prompt = f.read()
    peticion = prompt + permisosSinProcesar
    respuestaIA = atacarAPI(peticion)
    return respuestaIA
