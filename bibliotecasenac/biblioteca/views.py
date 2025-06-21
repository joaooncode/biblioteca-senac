from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import JsonResponse
from .models import Livro, Autor, Categoria, Emprestimo, Usuario
from .forms import LivroForm, AutorForm, CategoriaForm, EmprestimoForm, UsuarioForm

# Home View
class HomeView(TemplateView):
    template_name = 'biblioteca/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Biblioteca SENAC - Home'
        context['total_livros'] = Livro.objects.count()
        context['total_usuarios'] = Usuario.objects.count()
        context['emprestimos_ativos'] = Emprestimo.objects.filter(data_devolucao__isnull=True).count()
        return context

# Livro Views
class LivroListView(ListView):
    model = Livro
    template_name = 'biblioteca/livro_list.html'
    context_object_name = 'livros'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Livro.objects.all().select_related('categoria', 'autor')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(titulo__icontains=search) |
                Q(autor__nome__icontains=search) |
                Q(categoria__nome__icontains=search)
            )
        return queryset

class LivroDetailView(DetailView):
    model = Livro
    template_name = 'biblioteca/livro_detail.html'
    context_object_name = 'livro'

class LivroCreateView(LoginRequiredMixin, CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'biblioteca/livro_form.html'
    success_url = reverse_lazy('biblioteca:livro_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Livro cadastrado com sucesso!')
        return super().form_valid(form)

class LivroUpdateView(LoginRequiredMixin, UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'biblioteca/livro_form.html'
    success_url = reverse_lazy('biblioteca:livro_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Livro atualizado com sucesso!')
        return super().form_valid(form)

class LivroDeleteView(LoginRequiredMixin, DeleteView):
    model = Livro
    template_name = 'biblioteca/livro_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:livro_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Livro removido com sucesso!')
        return super().delete(request, *args, **kwargs)

# Autor Views
class AutorListView(ListView):
    model = Autor
    template_name = 'biblioteca/autor_list.html'
    context_object_name = 'autores'
    paginate_by = 10

class AutorDetailView(DetailView):
    model = Autor
    template_name = 'biblioteca/autor_detail.html'
    context_object_name = 'autor'

class AutorCreateView(LoginRequiredMixin, CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'biblioteca/autor_form.html'
    success_url = reverse_lazy('biblioteca:autor_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Autor cadastrado com sucesso!')
        return super().form_valid(form)

class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'biblioteca/autor_form.html'
    success_url = reverse_lazy('biblioteca:autor_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Autor atualizado com sucesso!')
        return super().form_valid(form)

class AutorDeleteView(LoginRequiredMixin, DeleteView):
    model = Autor
    template_name = 'biblioteca/autor_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:autor_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Autor removido com sucesso!')
        return super().delete(request, *args, **kwargs)

# Categoria Views
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'biblioteca/categoria_list.html'
    context_object_name = 'categorias'
    paginate_by = 10

class CategoriaCreateView(LoginRequiredMixin, CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'biblioteca/categoria_form.html'
    success_url = reverse_lazy('biblioteca:categoria_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Categoria cadastrada com sucesso!')
        return super().form_valid(form)

class CategoriaUpdateView(LoginRequiredMixin, UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'biblioteca/categoria_form.html'
    success_url = reverse_lazy('biblioteca:categoria_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Categoria atualizada com sucesso!')
        return super().form_valid(form)

class CategoriaDeleteView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'biblioteca/categoria_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:categoria_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Categoria removida com sucesso!')
        return super().delete(request, *args, **kwargs)

# Usuario Views
class UsuarioListView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'biblioteca/usuario_list.html'
    context_object_name = 'usuarios'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Usuario.objects.all()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search) |
                Q(email__icontains=search) |
                Q(telefone__icontains=search)
            )
        return queryset

class UsuarioDetailView(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'biblioteca/usuario_detail.html'
    context_object_name = 'usuario'

class UsuarioCreateView(LoginRequiredMixin, CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'biblioteca/usuario_form.html'
    success_url = reverse_lazy('biblioteca:usuario_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Usuário cadastrado com sucesso!')
        return super().form_valid(form)

class UsuarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'biblioteca/usuario_form.html'
    success_url = reverse_lazy('biblioteca:usuario_list')
    
    def form_valid(self, form):
        messages.success(self.request, 'Usuário atualizado com sucesso!')
        return super().form_valid(form)

class UsuarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Usuario
    template_name = 'biblioteca/usuario_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:usuario_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Usuário removido com sucesso!')
        return super().delete(request, *args, **kwargs)

# Emprestimo Views
class EmprestimoListView(LoginRequiredMixin, ListView):
    model = Emprestimo
    template_name = 'biblioteca/emprestimo_list.html'
    context_object_name = 'emprestimos'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Emprestimo.objects.all().select_related('livro', 'usuario')
        status = self.request.GET.get('status')
        if status == 'ativo':
            queryset = queryset.filter(data_devolucao__isnull=True)
        elif status == 'devolvido':
            queryset = queryset.filter(data_devolucao__isnull=False)
        return queryset.order_by('-data_emprestimo')

class EmprestimoDetailView(LoginRequiredMixin, DetailView):
    model = Emprestimo
    template_name = 'biblioteca/emprestimo_detail.html'
    context_object_name = 'emprestimo'

class EmprestimoCreateView(LoginRequiredMixin, CreateView):
    model = Emprestimo
    form_class = EmprestimoForm
    template_name = 'biblioteca/emprestimo_form.html'
    success_url = reverse_lazy('biblioteca:emprestimo_list')
    
    def form_valid(self, form):
        # Verificar se o livro está disponível
        livro = form.cleaned_data['livro']
        if Emprestimo.objects.filter(livro=livro, data_devolucao__isnull=True).exists():
            messages.error(self.request, 'Este livro já está emprestado!')
            return self.form_invalid(form)
        
        messages.success(self.request, 'Empréstimo realizado com sucesso!')
        return super().form_valid(form)

@login_required
def devolver_livro(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    if emprestimo.data_devolucao is None:
        emprestimo.devolver()
        messages.success(request, 'Livro devolvido com sucesso!')
    else:
        messages.warning(request, 'Este livro já foi devolvido!')
    return redirect('biblioteca:emprestimo_detail', pk=pk)

@login_required
def renovar_emprestimo(request, pk):
    emprestimo = get_object_or_404(Emprestimo, pk=pk)
    if emprestimo.data_devolucao is None:
        emprestimo.renovar()
        messages.success(request, 'Empréstimo renovado com sucesso!')
    else:
        messages.warning(request, 'Não é possível renovar um livro já devolvido!')
    return redirect('biblioteca:emprestimo_detail', pk=pk)

# Ajax Views
def livros_disponiveis(request):
    """Retorna livros disponíveis para empréstimo em formato JSON"""
    livros_emprestados = Emprestimo.objects.filter(
        data_devolucao__isnull=True
    ).values_list('livro_id', flat=True)
    
    livros_disponiveis = Livro.objects.exclude(
        id__in=livros_emprestados
    ).values('id', 'titulo')
    
    return JsonResponse(list(livros_disponiveis), safe=False)

def verificar_disponibilidade(request, livro_id):
    """Verifica se um livro específico está disponível"""
    disponivel = not Emprestimo.objects.filter(
        livro_id=livro_id, 
        data_devolucao__isnull=True
    ).exists()
    
    return JsonResponse({'disponivel': disponivel})

# Relatórios
class RelatoriosView(LoginRequiredMixin, TemplateView):
    template_name = 'biblioteca/relatorios.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_livros'] = Livro.objects.count()
        context['total_usuarios'] = Usuario.objects.count()
        context['emprestimos_ativos'] = Emprestimo.objects.filter(data_devolucao__isnull=True).count()
        context['emprestimos_atrasados'] = Emprestimo.objects.emprestimos_atrasados().count()
        context['livros_mais_emprestados'] = Livro.objects.mais_emprestados()[:5]
        return context

# Dashboard Admin
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'biblioteca/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estatisticas'] = {
            'total_livros': Livro.objects.count(),
            'total_usuarios': Usuario.objects.count(),
            'emprestimos_ativos': Emprestimo.objects.filter(data_devolucao__isnull=True).count(),
            'emprestimos_hoje': Emprestimo.objects.filter(data_emprestimo__date=timezone.now().date()).count(),
        }
        context['emprestimos_recentes'] = Emprestimo.objects.select_related('livro', 'usuario').order_by('-data_emprestimo')[:5]
        context['livros_populares'] = Livro.objects.mais_emprestados()[:5]
        return context
