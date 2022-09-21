#Importo la librería path y todas las views que se crearon
from django.urls import path
from . import views

app_name = "main"           #El nombre de mi app

#Le doy una dirección a todas las vistas que creé y las enlazo con un nombre
urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),                               #Url para el index
    path('contact/', views.ContactView.as_view(), name="contact"),                  #Url para el contact view
    path('blog/', views.BlogView.as_view(), name="blogs"),                          #Url para la vista del blog
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),          #Url para la vista detallada del blog, con ayuda del slug
    path('review/', views.ReviewView.as_view(), name="reviews"),                    #Url para la vista de la review
    path('review/<slug:slug>', views.ReviewDetailView.as_view(), name="review"),    #Url para la vista detallada del review, con ayuda del slug
    path('newblog/', views.NewBlogView.as_view(), name="newblog"),                  #Url para la vista del NewBlog, donde se crean los blogs
    path('newreview/', views.NewReviewView.as_view(), name='newreview'),            #Url para la vista del NewReview, donde se crean los reviews
    path('register/', views.registerPage, name="register"),                         #Url para la vista de la página de registro
    path('login/', views.loginPage, name="login"),                                  #Url para la vista de inicio de sesión
    path('logout/', views.logoutUser, name="logout"),                               #Url para la vista de cerrar sesión
    ]