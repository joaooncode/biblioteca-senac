from django.urls import path
from . import views

app_name = 'biblioteca'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    
    
    #Autenticação
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    
    #URLs para livros e autores
    path('livros/', views.LivroListView.as_view(), name='livro_list'),
    path('livros/<int:pk>/', views.LivroDetailView.as_view(), name='livro_detail'),
    path('livros/buscar/', views.LivroBuscarView.as_view(), name='livro_buscar'),
    
    # URLs para administração de livros e autores
    path('admin/livros/criar/', views.LivroCreateView.as_view(), name='livro_create'),
    path('admin/livros/<int:pk>/editar/', views.LivroUpdateView.as_view(), name='livro_update'),
    path('admin/livros/<int:pk>/deletar/', views.LivroDeleteView.as_view(), name='livro_delete'),
    
    # URLs para administração de autores
    path('autores/', views.AutorListView.as_view(), name='autor_list'),
    path('autores/<int:pk>/', views.AutorDetailView.as_view(), name='autor_detail'),
    
    
    # URLs para criação, edição e exclusão de autores
    path('admin/autores/criar/', views.AutorCreateView.as_view(), name='autor_create'),
    path('admin/autores/<int:pk>/editar/', views.AutorUpdateView.as_view(), name='autor_update'),
    path('admin/autores/<int:pk>/deletar/', views.AutorDeleteView.as_view(), name='autor_delete'),
    
    
    # URLs para reservas de livros
    path('reservas/', views.ReservaListView.as_view(), name='reserva_list'),
    path('reservas/minhas/', views.MinhasReservasView.as_view(), name='minhas_reservas'),
    path('livros/<int:livro_id>/reservar/', views.ReservarLivroView.as_view(), name='reservar_livro'),
    path('reservas/<int:pk>/cancelar/', views.CancelarReservaView.as_view(), name='cancelar_reserva'),
    
    
    # URLs para administração1
    path('admin/dashboard/', views.AdminDashboardView.as_view(), name='admin_dashboard'),
    path('admin/usuarios/', views.UsuarioListView.as_view(), name='usuario_list'),
    path('admin/usuarios/<int:pk>/', views.UsuarioDetailView.as_view(), name='usuario_detail'),
    
    # URLs para administração de usuários
    path('api/livros/disponibilidade/<int:livro_id>/', views.VerificarDisponibilidadeView.as_view(), name='verificar_disponibilidade'),
    path('api/reservas/expirar/', views.ExpirarReservasView.as_view(), name='expirar_reservas'),
]