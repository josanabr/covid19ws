# Web Service básico de COVID 19 

Este proyecto tiene como propósito el exponer a través de web services diversos datos relacionados al COVID 19.

# Requerimientos

Ejecutar los siguientes comandos para preparar el ambiente donde se ejecutara la aplicacion:

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

# Ejecutar la aplicación

```
export FLASK_APP=main.py FLASK_DEBUG=1
flask run --host=0.0.0.0
```

---

# Notas para el programador

* Si se hacen cambios en los campos que se monitorean, se debe cambiar el archivo `fields.py` y la función `findCountryData` debe considerar el nuevo campo para ingresarlo en el diccionario devuelto como respuesta.
