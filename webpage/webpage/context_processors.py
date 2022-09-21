#Se importan todas las librerías necesarias
from multiprocessing import context
from django.contrib.auth.models import User

#Función para guardar todos los objetos en el contexto del proyecto
def project_context(request):
    
    context = {
        'me': User.objects.first(),
    }

    return context