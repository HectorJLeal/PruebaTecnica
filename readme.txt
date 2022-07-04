-------------------------------------------------------- ASPECTOS TECNICOS ------------------------------------------------------------------------------
#Para la siguiente prueba se utilizaron los siguientes elementos:

asgiref==3.5.2
Django==4.0.5
django-filter==22.1
django-model-utils==4.2.0
djangorestframework==3.13.1
Markdown==3.3.7
psycopg2==2.9.3
pytz==2022.1
sqlparse==0.4.2
types-pkg-resources==0.1.3
tzdata==2022.1

#Base de datos (PostgreSQL)
Contraseña: PruebaTecnica
Nombre de la base de datos: NEXTIA
nombre de usuario: ADMIN
Contraseña de la DB: pru3b4-t3cn1c4
Puerto: 5432

#Admin Django
Usuario: Hector
mail: contacto@hectorjleal.com
Contraseña: Prueba
-------------------------------------------------------- DETALLES ------------------------------------------------------------------------------
#Puntos cubiertos 
Creación del proyecto y configuración
Creación del modelo “Base”
Generación del modelo Users que hereda de Base
Creación de modelo llamado Bienes que hereda de BaseModel y relación al modelo Users (usuario_id)

#Faltantes
Endpoints y lógica para autenticación de usuarios 
Script de registro de usuarios 
Endpoint SCRUD para modelo de bienes
Endpoint para Bienes (Envio de múltiples Ids)

