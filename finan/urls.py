from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('listar_class_pagar/', views.listar_class_pagar, name="listar_class_pagar"),
    path('cadastro_class_pagar/', views.cadastro_class_pagar, name="cadastro_class_pagar"),
    path('cadastrar_class_pagar/', views.cadastrar_class_pagar, name="cadastrar_class_pagar"),
    path('detalhar_class_pagar/<int:id_class>/', views.detalhar_class_pagar, name="detalhar_class_pagar"),
    path('editar_class_pagar/<int:id_class>/', views.editar_class_pagar, name="editar_class_pagar"),
    path('edit_class_pagar/', views.edit_class_pagar, name="edit_class_pagar"),
    path('excluir_class_pagar/<int:id_class>/', views.excluir_class_pagar, name="excluir_class_pagar"),
]