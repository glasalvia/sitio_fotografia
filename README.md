# Portal Fotografico
Portal para publicar y promocionar trabajos fotograficos


# Instrucciones

1 . VirtualENV

Se recomienda trabajar con virtualenv para hacer el deploy del proyecto

Sobre una terminal(tener en cuenta las variables de entorno)

-- pip install virtualenv
-- virtualenv nombredelambiente
-- \nombredelambiente\scripts\activate


2. Dependencias

Django==1.11.6
PyMySQL==0.7.11
pytz==2017.2

Para instalar las dependencias:

pip install -r requirements.txt


3- Settings.py

Setear la conexion a la base de datos sobre la etiqueta "DATABASES"


4 - Ejecucion

-- python manage.py runserver



