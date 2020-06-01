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

    path('listar_forma_pagar/', views.listar_forma_pagar, name="listar_forma_pagar"),
    path('cadastro_forma_pagar/', views.cadastro_forma_pagar, name="cadastro_forma_pagar"),
    path('cadastrar_forma_pagar/', views.cadastrar_forma_pagar, name="cadastrar_forma_pagar"),
    path('detalhar_forma_pagar/<int:id_forma>/', views.detalhar_forma_pagar, name="detalhar_forma_pagar"),
    path('editar_forma_pagar/<int:id_forma>/', views.editar_forma_pagar, name="editar_forma_pagar"),
    path('edit_forma_pagar/', views.edit_forma_pagar, name="edit_forma_pagar"),
    path('excluir_forma_pagar/<int:id_forma>/', views.excluir_forma_pagar, name="excluir_forma_pagar"),

    path('listar_pagar/', views.listar_pagar, name="listar_pagar"),
    path('cadastro_pagar/', views.cadastro_pagar, name="cadastro_pagar"),
    path('cadastrar_pagar/', views.cadastrar_pagar, name="cadastrar_pagar"),
    path('detalhar_pagar/<int:id_pagar>/', views.detalhar_pagar, name="detalhar_pagar"),
    path('editar_pagar/<int:id_pagar>/', views.editar_pagar, name="editar_pagar"),
    path('edit_pagar/', views.edit_pagar, name="edit_pagar"),
    path('excluir_pagar/<int:id_pagar>/', views.excluir_pagar, name="excluir_pagar"),

]