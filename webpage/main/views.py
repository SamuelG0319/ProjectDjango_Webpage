#Importo todas las librerías necesarias
from multiprocessing import context
from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from .forms import BlogForm, ContactForm, CreateUserForm, ReviewForm
from .models import (
    Blog,
    Review,
    ContactProfile
    )

#Importo las seis librerías necesarias para que la sección de creación de usuario funcione
from django.contrib.auth.forms import UserCreationForm          #Importo el form para la creación del usuario
from django.contrib.auth import authenticate, login, logout     #Importo la librería de la autenticación, el login y el logout para solo utilizarlos sin crearlos
from django.contrib.auth.decorators import login_required       #Importo la librería que me permitirá pedir una autenticación para poder ir a cierta parte de la página
from django.contrib.auth.forms import UserCreationForm          #Es esta librería necesaria dos veces?
from django.http import HttpResponse                            #Importo la librería que permitirá una respuesta en la página web
from django.shortcuts import redirect                           #Importo la librería para direccionar a los usuarios
from django.contrib.auth.mixins import LoginRequiredMixin

#Creo una vista para el index, que sdrá mi la página principal
class IndexView(generic.TemplateView):
    template_name = "main/index.html"   #La enlazo al template que tengo creado en HTML

    #Obtengo todos los contextos que tengo creados como objetos
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        reviews = Review.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)

        context["reviews"] = reviews
        context["blogs"] = blogs
        return context

#Creo la vista para el contacto
class ContactView(generic.FormView):
    template_name = "main/contact.html"     #Enlazo el template creado en HTML
    form_class = ContactForm                #Enlazo el form que se creó
    success_url = "/"                       #La dirección mostrada si se envió el formulario bien

    def form_valid(self, form):
        form.save()
        messages.success(self.request, '¡Gracias! Nos pondremos en contacto pronto')
        return super().form_valid(form)

#Creo la vista para el Blog
class BlogView(generic.ListView):
    model = Blog                        #Uso el modelo Blog
    template_name = "main/blog.html"    #Enlazo la vista al template que ya está creado en HTML
    paginate_by = 10                    #Solo se mostrarán 10 archivos en la vista

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

#Creo la vista detallada del blog, usa el modelo del Blog y solo mostrará la información completa del blog en específico
class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "main/blog-detail.html"

#Creo la vista para el nuevo blog
class NewBlogView(LoginRequiredMixin, generic.FormView):
    login_url = 'main:login'
    redirect_field_name = 'login'
    template_name = "main/new-blog.html"        #Enlazo el template creado en HTML
    form_class = BlogForm                       #Enlazo la vista con el formulario
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Gracias por añadir un blog.')
        return super().form_valid(form)

#Creo la vista para el Review
class ReviewView(generic.ListView):
    model = Review                          #La enlazo al modelo Review
    template_name = "main/review.html"      #La enlazo al template que se creó
    paginate_by = 10                        #Solo muestro 10 datos en la vista

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

#Creo la vista para el review detallado
class ReviewDetailView(generic.DetailView):
    model = Review                              #La enlazo al modelo Review
    template_name = "main/review-detail.html"   #La enlazo a su template creado en HTML

#Creo la vista para la creación de un review

class NewReviewView(LoginRequiredMixin, generic.FormView):
    login_url = 'main:login'
    redirect_field_name = 'login'
    template_name = "main/new-review.html"      #La enlazo a su template
    form_class = ReviewForm                     #La enlazo al formulario creado
    success_url = "/"                           #Dirección a la que se envía si se recibe el formulario

    #Mensaje que se muestra si se envía correctamente el formulario
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Gracias por añadir un blog.')
        return super().form_valid(form)

#Creo la vista para que el usuario se registre, que será una función y no una clase
def registerPage(request):
    #Si el usuario ya está autenticado lo enviará al index
    if request.user.is_authenticated:
        return redirect("main:home")

    else:                                           #Si no está autenticado...
        form = CreateUserForm()                     #Se creará el form para que entre los datos
        if request.method == 'POST':                
            form = CreateUserForm(request.POST)     #Cuando se llenen los datos se enviarán los datos al form
            if form.is_valid():                     #Si el form es válido
                form.save()                         #Se guardan los datos
                user = form.cleaned_data.get('username')            #Se crea el usuario
                messages.success(request, 'La cuenta fue creada exitosamente para ' + user)     #Se le envía un mensaje al usuario

                return redirect('main:login')       #Finalmente se le envía a la página para iniciar sesión
        
        context = {'form':form}
        return render(request, 'main/register.html', context)

#Creo la vista para la página de inicio de sesión, que también es una función y no una clase
def loginPage(request):
    if request.user.is_authenticated:       #Si el usuario está autenticado lo envía al index
        return redirect("main:home")
    
    else:                                   #Si no lo está se le pedirá el usuario y contraseña con el form
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)      #Se procede a autenticar los datos
            
            if user is not None:                #Si los datos existen se envía al index
                login(request, user)
                return redirect("main:home")
            else:
                messages.info(request, 'Usuario o Contraseña incorrectos')      #Si no existen se le envía el mensaje de que sus datos son incorrectos
        
        context = {}
        return render(request, 'main/login.html', context)      #Al acabar el proceso se devuelve un HttpResponse con los argumentos con el request, el contexto y la vista en html

#Creo la vista para hacer el logout, que también es una función solamente
def logoutUser(request):
    logout(request)
    return redirect('main:login')       #Se realiza el logout con ayuda de la librería de django y se envía al usuario a la vista de iniciar sesión

# Create your views here.
