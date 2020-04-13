from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, TemplateView, ListView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from modain.products.models import Product, Comment
from django.db.models import Q, Max, Min
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse


User = get_user_model()

class Indice(TemplateView):
    template_name = 'index.html'
    

class test(TemplateView):
    template_name = 'test.html'

class ListadoProducto(ListView):
    template_name = 'listado_productos.html'
    model = Product
    paginate_by = 10

    def get_queryset(self):
        query = None
        if ('name' in self.request.GET) and self.request.GET['name'] != "":
            query = Q(name=self.request.GET['name'])

        if ('maximo' in self.request.GET) and self.request.GET['maximo'] != "":
            try:
                if query == None:
                    query = Q(price__lte = int(float(self.request.GET(['maximo']))))
                else:
                    query = query & Q(price__lte=int(float(self.request.GET['maximo'])))

            except:
                pass

        if ('minimo' in self.request.GET) and self.request.GET['minimo'] != "":
            try:
                if query == None:
                    query = Q(price__gte = int(float(self.request.GET(['minimo']))))
                else:
                    query = query & Q(price__gte=int(float(self.request.GET['minimo'])))

            except:
                pass

        if query is not None:
            productos = Product.objects.filter(query)
        else:
            productos = Product.objects.all()
        return productos
    
    def dump(obj):
        for attr in dir(obj):
            if hasattr( obj, attr ):
                print( "obj.%s = %s" % (attr, getattr(obj, attr)))

    def get_context_data(self, **kwargs):
        context = super(ListadoProducto, self).get_context_data(**kwargs)
        context['maximo'] = Product.objects.all().aggregate(Max('price'))['price__max']
        context['minimo'] = Product.objects.all().aggregate(Min('price'))['price__min']
        return context

class DetalleProducto(DetailView):
    template_name = "detalle.html"
    model = Product

class ComentarioProducto(CreateView):
    template_name = "detalle.html"
    model = Comment
    fields = ('comment', 'usuario', 'producto')

    def get_success_url(self):
        return "/detalle_producto/{}".format(self.object.producto.pk)

class Salir(LogoutView):
    next_page = reverse_lazy('index')

class Ingresar(LoginView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        else:
            context = self.get_context_data(**kwargs)
            return self.render_to_response(context)

    def get_success_url(self):
        return reverse('index')       

class CambiarPerfil(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('phone', 'last_name', 'first_name', 'email')
    success_url = '/'
    template_name = 'perfil.html'

    def get_object(self, queryset=None):
        return self.request.user