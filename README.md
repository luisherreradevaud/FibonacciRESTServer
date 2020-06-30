# FibonacciRESTServer
Servicio REST hecho en Python3 con la librería Flask.
Se entrega un entero positivo <n> vía consulta http GET, retornando el número de la secuencia de Fibonacci para ese índice.

El formato para consulta http es:
http://<server_url>:5000/phi/<n>

Dependecias:
- flask
- flask_restful

# Pruebas
Para las pruebas unitarias se utilizó pytest.

Para ejecutar las pruebas:
>py.test test.py

Pruebas realizadas:
- n negativo
- n no numérico
- n positivo

Dependencias:
- pytest
