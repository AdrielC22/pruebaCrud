from django.urls import path
from . import views
urlpatterns = [
    path ("",views.home,name="home"),
    path ("agregar/", views.agregar, name="agregar"),
    path ("agregaractividad/", views.agregaractividad, name="actividad"),
    path ("eliminar/<int:tarea_id>/", views.eliminar,name = "eliminar"),
    path ("eliminar/<int:actividad_id>/", views.eliminaractividad,name = "eliminaractividad"),
    path ("editar/<int:tarea_id>/", views.editar, name = "editar"),
    path ("editaractividad/<int:actividad_id>/", views.editaractividad, name = "editaractividad"),
]