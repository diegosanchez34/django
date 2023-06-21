from django.urls import path
from  . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('crud', views.crud, name='crud'),
    path('AgregarAlumno', views.AgregarAlumno, name='AgregarAlumno'),
    path('EliminarAlumno', views.EliminarAlumno, name='EliminarAlumno'),
    path('ModificarAlumno', views.ModificarAlumno, name='ModificarAlumno')
]

