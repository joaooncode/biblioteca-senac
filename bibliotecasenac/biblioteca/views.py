from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from django.contrib.auth import login
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm
from .models import Livro, Autor, Categoria, Emprestimo, Reserva, Usuario

# Basic views
class HomeView(TemplateView):
    template_name = 'biblioteca/home.html'

class LoginView(AuthLoginView):
    template_name = 'biblioteca/login.html'
    form_class = LoginForm

class LogoutView(AuthLogoutView):
    template_name = 'biblioteca/logout.html'

class RegisterView(TemplateView):
    template_name = 'biblioteca/register.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = RegisterForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Conta criada com sucesso! Bem-vindo(a)!')
            return redirect('biblioteca:home')
        else:
            return self.render_to_response(self.get_context_data(form=form))

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'biblioteca/profile.html'
    login_url = '/login/'

# Livro views
class LivroListView(ListView):
    model = Livro
    template_name = 'biblioteca/livro_list.html'
    context_object_name = 'livros'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Livro.objects.select_related('autor').all()
        
        # Search functionality
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(titulo__icontains=query) |
                Q(autor__nome__icontains=query)
            )
        
        # Filter by genre
        genero = self.request.GET.get('genero')
        if genero:
            queryset = queryset.filter(genero=genero)
            
        return queryset.order_by('titulo')

class LivroDetailView(DetailView):
    model = Livro
    template_name = 'biblioteca/livro_detail.html'
    context_object_name = 'livro'

class LivroBuscarView(ListView):
    model = Livro
    template_name = 'biblioteca/livro_buscar.html'
    context_object_name = 'livros'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Livro.objects.select_related('autor').all()
        
        # Search functionality
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(titulo__icontains=query) |
                Q(autor__nome__icontains=query)
            )
        
        # Filter by genre
        genero = self.request.GET.get('genero')
        if genero:
            queryset = queryset.filter(genero=genero)
            
        return queryset.order_by('titulo')

class LivroCreateView(CreateView):
    model = Livro
    template_name = 'biblioteca/livro_form.html'
    fields = ['titulo', 'autor', 'genero', 'quantidade']
    success_url = reverse_lazy('biblioteca:livro_list')

class LivroUpdateView(UpdateView):
    model = Livro
    template_name = 'biblioteca/livro_form.html'
    fields = ['titulo', 'autor', 'genero', 'quantidade']
    success_url = reverse_lazy('biblioteca:livro_list')

class LivroDeleteView(DeleteView):
    model = Livro
    template_name = 'biblioteca/livro_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:livro_list')

# Autor views
class AutorListView(ListView):
    model = Autor
    template_name = 'biblioteca/autor_list.html'
    context_object_name = 'autores'
    paginate_by = 12

class AutorDetailView(DetailView):
    model = Autor
    template_name = 'biblioteca/autor_detail.html'
    context_object_name = 'autor'

class AutorCreateView(CreateView):
    model = Autor
    template_name = 'biblioteca/autor_form.html'
    fields = ['nome']
    success_url = reverse_lazy('biblioteca:autor_list')

class AutorUpdateView(UpdateView):
    model = Autor
    template_name = 'biblioteca/autor_form.html'
    fields = ['nome']
    success_url = reverse_lazy('biblioteca:autor_list')

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'biblioteca/autor_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:autor_list')

# Reserva views
class ReservaListView(ListView):
    model = Reserva
    template_name = 'biblioteca/reserva_list.html'
    context_object_name = 'reservas'
    paginate_by = 12

class MinhasReservasView(LoginRequiredMixin, ListView):
    model = Reserva
    template_name = 'biblioteca/minhas_reservas.html'
    context_object_name = 'reservas'
    
    def get_queryset(self):
        return Reserva.objects.filter(usuario=self.request.user).order_by('-data_reserva')

class ReservarLivroView(LoginRequiredMixin, TemplateView):
    template_name = 'biblioteca/reservar_livro.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        livro_id = kwargs.get('livro_id')
        try:
            context['livro'] = Livro.objects.get(pk=livro_id)
        except Livro.DoesNotExist:
            context['livro'] = None
        return context

class CancelarReservaView(LoginRequiredMixin, DeleteView):
    model = Reserva
    template_name = 'biblioteca/cancelar_reserva.html'
    success_url = reverse_lazy('biblioteca:minhas_reservas')

# Admin views
class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'biblioteca/admin_dashboard.html'

class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'biblioteca/usuario_list.html'
    context_object_name = 'usuarios'
    paginate_by = 12

class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'biblioteca/usuario_detail.html'
    context_object_name = 'usuario'

class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    template_name = 'biblioteca/usuario_form.html'
    fields = ['username', 'first_name', 'last_name', 'email', 'tipo_usuario']
    success_url = reverse_lazy('biblioteca:usuario_list')

class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'biblioteca/usuario_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:usuario_list')

# Emprestimo views
class EmprestimoListView(ListView):
    model = Emprestimo
    template_name = 'biblioteca/emprestimo_list.html'
    context_object_name = 'emprestimos'
    paginate_by = 12

class EmprestimoDetailView(DetailView):
    model = Emprestimo
    template_name = 'biblioteca/emprestimo_detail.html'
    context_object_name = 'emprestimo'

class EmprestimoCreateView(LoginRequiredMixin, CreateView):
    model = Emprestimo
    template_name = 'biblioteca/emprestimo_form.html'
    fields = ['usuario', 'livro']
    success_url = '/emprestimos/'

# Categoria views
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'biblioteca/categoria_list.html'
    context_object_name = 'categorias'
    paginate_by = 12

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = 'biblioteca/categoria_form.html'
    fields = ['nome', 'descricao']
    success_url = '/categorias/'

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    template_name = 'biblioteca/categoria_form.html'
    fields = ['nome', 'descricao']
    success_url = '/categorias/'

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'biblioteca/categoria_confirm_delete.html'
    success_url = '/categorias/'

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