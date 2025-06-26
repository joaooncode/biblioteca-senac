from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from django.http import JsonResponse

# Basic views
class HomeView(TemplateView):
    template_name = 'biblioteca/home.html'

class LoginView(AuthLoginView):
    template_name = 'biblioteca/login.html'

class LogoutView(AuthLogoutView):
    template_name = 'biblioteca/logout.html'

class RegisterView(TemplateView):
    template_name = 'biblioteca/register.html'

class ProfileView(TemplateView):
    template_name = 'biblioteca/profile.html'

# Livro views
class LivroListView(TemplateView):
    template_name = 'biblioteca/livro_list.html'

class LivroDetailView(TemplateView):
    template_name = 'biblioteca/livro_detail.html'

class LivroBuscarView(TemplateView):
    template_name = 'biblioteca/livro_buscar.html'

class LivroCreateView(TemplateView):
    template_name = 'biblioteca/livro_form.html'

class LivroUpdateView(TemplateView):
    template_name = 'biblioteca/livro_form.html'

class LivroDeleteView(TemplateView):
    template_name = 'biblioteca/livro_confirm_delete.html'

# Autor views
class AutorListView(TemplateView):
    template_name = 'biblioteca/autor_list.html'

class AutorDetailView(TemplateView):
    template_name = 'biblioteca/autor_detail.html'

class AutorCreateView(TemplateView):
    template_name = 'biblioteca/autor_form.html'

class AutorUpdateView(TemplateView):
    template_name = 'biblioteca/autor_form.html'

class AutorDeleteView(TemplateView):
    template_name = 'biblioteca/autor_confirm_delete.html'

# Reserva views
class ReservaListView(TemplateView):
    template_name = 'biblioteca/reserva_list.html'

class MinhasReservasView(TemplateView):
    template_name = 'biblioteca/minhas_reservas.html'

class ReservarLivroView(TemplateView):
    template_name = 'biblioteca/reservar_livro.html'

class CancelarReservaView(TemplateView):
    template_name = 'biblioteca/cancelar_reserva.html'

# Admin views
class AdminDashboardView(TemplateView):
    template_name = 'biblioteca/admin_dashboard.html'

class UsuarioListView(TemplateView):
    template_name = 'biblioteca/usuario_list.html'

class UsuarioDetailView(TemplateView):
    template_name = 'biblioteca/usuario_detail.html'

class UsuarioUpdateView(TemplateView):
    template_name = 'biblioteca/usuario_form.html'

class UsuarioDeleteView(TemplateView):
    template_name = 'biblioteca/usuario_confirm_delete.html'

# Emprestimo views
class EmprestimoListView(TemplateView):
    template_name = 'biblioteca/emprestimo_list.html'

class EmprestimoDetailView(TemplateView):
    template_name = 'biblioteca/emprestimo_detail.html'

class EmprestimoCreateView(TemplateView):
    template_name = 'biblioteca/emprestimo_form.html'

# Categoria views
class CategoriaListView(TemplateView):
    template_name = 'biblioteca/categoria_list.html'

class CategoriaCreateView(TemplateView):
    template_name = 'biblioteca/categoria_form.html'

class CategoriaUpdateView(TemplateView):
    template_name = 'biblioteca/categoria_form.html'

class CategoriaDeleteView(TemplateView):
    template_name = 'biblioteca/categoria_confirm_delete.html'

# Dashboard views
class RelatoriosView(TemplateView):
    template_name = 'biblioteca/relatorios.html'

class DashboardView(TemplateView):
    template_name = 'biblioteca/dashboard.html'

class VerificarDisponibilidadeView(TemplateView):
    template_name = 'biblioteca/verificar_disponibilidade.html'

class ExpirarReservasView(TemplateView):
    template_name = 'biblioteca/expirar_reservas.html'

# Function-based views
def devolver_livro(request, pk):
    return JsonResponse({'status': 'success'})

def renovar_emprestimo(request, pk):
    return JsonResponse({'status': 'success'})

def livros_disponiveis(request):
    return JsonResponse({'livros': []})

def verificar_disponibilidade(request, livro_id):
    return JsonResponse({'disponivel': True})