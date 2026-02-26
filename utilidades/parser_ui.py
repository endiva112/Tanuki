# parser_ui.py recibe la ruta del XML y devuelve una lista limpia de elementos interactivos con sus coordenadas calculadas.
import xml.etree.ElementTree as ET
import re

# Funciones auxiliares
def calcularCentroBounds(bounds):
    coordenadas = list(map(int, re.findall(r'\d+', bounds)))
    x1 = coordenadas[0]
    y1 = coordenadas[1]
    x2 = coordenadas[2]
    y2 = coordenadas[3]

    # // hace division entera, sin decimales, mejor que parsear la ecuacion a int
    x_mb = (x1+x2) // 2
    y_mb = (y1+y2) // 2
    centroBounds = x_mb, y_mb
    return centroBounds

# Ignora la mayoría de la UI y se retorna solo los elementos interactuables
def parsear_ui(rutaXML):
    arbolDeNodos = ET.parse(rutaXML)
    elementos = []

    for nodo in arbolDeNodos.iter():
        if nodo.attrib.get("clickable") == "true":
            elemento = {
                "texto": nodo.attrib.get("text", ""),
                "descripcion": nodo.attrib.get("content-desc", ""),
                "coordenadas": calcularCentroBounds(nodo.attrib.get("bounds", ""))
            }
            if elemento["texto"] == "":
                for hijo in nodo.iter():
                    texto = hijo.attrib.get("text", "")
                    if texto != "":
                        elemento["texto"] = texto
            
            if elemento["descripcion"] == "":
                for hijo in nodo.iter():
                    descripcion = hijo.attrib.get("content-desc", "")
                    if descripcion != "":
                        elemento["descripcion"] = descripcion
            elementos.append(elemento)
    return elementos

