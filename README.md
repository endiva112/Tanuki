```
- DOABLE    Reconstrucción de flujos internos (interacción/eventos)
- NO        Uso de memoria y tiempos de carga/renderizado
- DOABLE    Permisos solicitados
- MAYBE     Uso de información sensible del usuario
- NO        Comunicaciones externas (HTTPS, sockets)
- DOABLE    Capturas (o al menos análisis) de UI en distintas resoluciones/formatos de dispositivo
```

en \Tanuki ejecutar:
```bash
python main.py
```

Librerias que han hecho falta y deberían agregarse al requirements.txt
pip install python-dotenv