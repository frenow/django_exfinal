from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
#PAGAR
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
#RECEBER
    path('listar_class_receber/', views.listar_class_receber, name="listar_class_receber"),
    path('cadastro_class_receber/', views.cadastro_class_receber, name="cadastro_class_receber"),
    path('cadastrar_class_receber/', views.cadastrar_class_receber, name="cadastrar_class_receber"),
    path('detalhar_class_receber/<int:id_class>/', views.detalhar_class_receber, name="detalhar_class_receber"),
    path('editar_class_receber/<int:id_class>/', views.editar_class_receber, name="editar_class_receber"),
    path('edit_class_receber/', views.edit_class_receber, name="edit_class_receber"),
    path('excluir_class_receber/<int:id_class>/', views.excluir_class_receber, name="excluir_class_receber"),

    path('listar_forma_receber/', views.listar_forma_receber, name="listar_forma_receber"),
    path('cadastro_forma_receber/', views.cadastro_forma_receber, name="cadastro_forma_receber"),
    path('cadastrar_forma_receber/', views.cadastrar_forma_receber, name="cadastrar_forma_receber"),
    path('detalhar_forma_receber/<int:id_forma>/', views.detalhar_forma_receber, name="detalhar_forma_receber"),
    path('editar_forma_receber/<int:id_forma>/', views.editar_forma_receber, name="editar_forma_receber"),
    path('edit_forma_receber/', views.edit_forma_receber, name="edit_forma_receber"),
    path('excluir_forma_receber/<int:id_forma>/', views.excluir_forma_receber, name="excluir_forma_receber"),

    path('listar_receber/', views.listar_receber, name="listar_receber"),
    path('cadastro_receber/', views.cadastro_receber, name="cadastro_receber"),
    path('cadastrar_receber/', views.cadastrar_receber, name="cadastrar_receber"),
    path('detalhar_receber/<int:id_receber>/', views.detalhar_receber, name="detalhar_receber"),
    path('editar_receber/<int:id_receber>/', views.editar_receber, name="editar_receber"),
    path('edit_receber/', views.edit_receber, name="edit_receber"),
    path('excluir_receber/<int:id_receber>/', views.excluir_receber, name="excluir_receber"),
#RELATORIOS
    path('relatorio_pagar/', views.relatorio_pagar, name="relatorio_pagar"),
    path('rel_pagar/', views.rel_pagar, name="rel_pagar"),
    path('relatorio_receber/', views.relatorio_receber, name="relatorio_receber"),
    path('rel_receber/', views.rel_receber, name="rel_receber"),
    path('relatorio_fluxo/', views.relatorio_fluxo, name="relatorio_fluxo"),

]