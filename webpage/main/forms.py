#Importo la librería forms de django
from django import forms
from django.forms import ModelForm

#Importo los modelos creados, que tienen que ver con un forms
from .models import (
	Blog,
	ContactProfile,
	Review,
	)

#Importo el UserCreationForm de la librería de Django para crear el usuario
from django.contrib.auth.forms import UserCreationForm

#Importo el User de la librería de Django que sería para guardar el usuario como tal
from django.contrib.auth.models import User

#Creo un nuevo forms llamado ContactForm y me servirá para recibir un mensaje de los usuarios
class ContactForm(forms.ModelForm):

	#Agrego a la class la metadata del modelo ContactProfile con los campos que quiero traer de ese modelo
	class Meta:
		model = ContactProfile
		fields = ('name', 'email', 'message',)

#Creo un nuevo forms llamado BlogForm y me servirá para recibir un blog de los usuarios
class BlogForm(forms.ModelForm):

	#Le agrego a la class la metadata del modelo NewBlog con los campos que quiero de dicho modelo
	class Meta:
		model = Blog
		fields = ('owner', 'title', 'author', 'resume', 'image',)


#Creo un nuevo forms llamado BlogForm y me servirá para recibir un blog de los usuarios
class ReviewForm(forms.ModelForm):

	#Le agrego a la class la metadata del modelo NewReview con los campos que quiero de dicho modelo
	class Meta:
		model = Review
		fields = ('owner', 'title', 'author', 'review', 'image',)


#Creo la clase que permitirá crear el usuario en la página
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User												#Utilizamos el modelo del User que ya importamos
		fields = ['username', 'email', 'password1', 'password2']		#Los campos que usará serán los del usuario, el email y la contraseña, dos veces para verificarla como en la creación del superuser

