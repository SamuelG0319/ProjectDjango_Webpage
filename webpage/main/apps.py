#Importo la librería AppConfig de django
from django.apps import AppConfig

#Clase que permite llevar los modelos a la base de datos
class MainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main"
