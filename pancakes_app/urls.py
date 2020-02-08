from django.urls import path
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from pancakes_app import views

urlpatterns = [
    path('', views.list, name='list'),                                      #List
    path('home', views.home, name='home'),                                  #Home
    path('categ/<categ_name>', views.listbycateg, name='listbycateg'),      #Category
    path('edit/<id>', views.edit, name='edit'),                             #Edit
    path('add', views.add, name='add'),                                     #Add
    path('delete/<id>', views.delete, name='delete'),                       #Delete
    path('about/', views.about, name='about'),                              #About
    path('contactus/', views.contactus, name='contactus'),                  #Contactus
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
