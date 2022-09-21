#Importo todas las librerías que deseo utilizar
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField

#Creo el modelo ContactProfile para guardar los datos del usuario que quiera contactarme
class ContactProfile(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Profiles'                #Este será el nombre que aparezca en admin como plural
        verbose_name = 'Contact Profile'                        #Este será el nombre que aparezca en admin como singular
        ordering = ["timestamp"]                                #Ordeno los datos por la fecha en que fueron creados

    #Uso las variables para guardar los datos de la fecha, el nombre, el email y el mensaje que envía el usuario
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(verbose_name="Name",max_length=100)
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")

    #Creo una función que devolverá el nombre que ingresó el usuario
    def __str__(self):
        return f'{self.name}'

#Creo el modelo para el Blog como tal
class Blog(models.Model):

    #Agrego al modelo el nombre de este en plural, singular y la fecha en que se subió el blog, para que se observe en admin
    class Meta:
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'
        ordering = ["timestamp"]
    
    #Uso las variables para guardar la fecha, el creador, el titulo, el autor, el resumen, el slug, la imagen y si está activo el blog
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    resume = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="blog")
    is_active = models.BooleanField(default=True)

    #Creo una función para guardar los datos en el slug
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)
    
    #Creo una función que devuelve el titulo
    def __str__(self):
        return self.title
    
    #Creo la función que obtiene la dirección del slug para devolverla al blog
    def get_absolute_url(self):
        return f"/blog/{self.slug}"

#Creo el modelo para el Review
class Review(models.Model):

    #Guardo en la class los nombres en plural y singular que se verán en el admin, así como el orden por la fecha de subida
    class Meta:
        verbose_name_plural = 'Reviews'
        verbose_name = 'Review'
        ordering = ["timestamp"]

    #Uso las variables para guardar la fecha, el creador, el titulo, el autor, el review como tal, su slug, su imagen y si está activo
    timestamp = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    review = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="review")
    is_active = models.BooleanField(default=True)

    #Creo una función para guardar los datos en el slug
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Review, self).save(*args, **kwargs)
    
    #Creo una función para devolver el título del review
    def __str__(self):
        return self.title
    
    #Creo una función para obtener la dirección y devolverla en la url del review
    def get_absolute_url(self):
        return f"/review/{self.slug}"

# Create your models here.
