# agente_ia.py recibe un prompt y datos, llama a la API, y devuelve la respuesta.
import requests, base64

class AgenteIA:
    # Constructor
    def __init__(self, urlAPI, claveAPI, modelo):
        self.urlAPI = urlAPI
        self.claveAPI = claveAPI
        self.modelo = modelo

    # Métodos auxiliares
    # Headers con autorización
    def _headers(self):
        headers = {
            "Authorization": f"Bearer {self.claveAPI}",
            "Content-Type": "application/json"
        }
        return headers
    
    # Hace la petición POST y retorna la respuesta de la API del agente IA
    def _respuesta(self, headers, body):
        respuesta = requests.post(self.urlAPI, headers=headers, json=body)
        # Comprobar si hubo errores
        if respuesta.status_code != 200:
            print("Error al contactar la API:", respuesta.status_code, respuesta.text)
            return None
        
        resultado = respuesta.json()
        # Extrae el texto de la primera respuesta devuelta por la API
        return resultado["choices"][0]["message"]["content"]


    # Métodos principales
    def atacarAPI(self, mensaje):
        # Cuerpo del mensaje
        body = {
            "model": self.modelo,
            "messages": [{"role": "user", "content": mensaje}],
            #"max_tokens": 50 //TODO posible mejora, pasar por parametro a la función que cantidad de tokens usar puede ser conveniente para ahorrar a futuro en tareas menos importantes
        }

        headers = self._headers()
        return self._respuesta(headers, body)


    def atacarAPI_con_imagen(self, prompt, ruta_imagen):
        # Convertir imagen a base64
        with open(ruta_imagen, "rb") as img_file:
            imagen_base64 = base64.b64encode(img_file.read()).decode("utf-8")

        # Cuerpo del mensaje
        body = {
            "model": self.modelo,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{imagen_base64}"
                            }
                        }
                    ]
                }
            ],
            #"max_tokens": 500
        }

        headers = self._headers()
        return self._respuesta(headers, body)