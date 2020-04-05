from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, TemplateView, ListView
from django.db.models import Q, max, min


User = get_user_model()

class Indice(TemplateView):
    template_name = 'index.html'

class test(TemplateView):
    template_name = 'test.html'

class ListadoProducto(ListView):
    template_name = 'listado_productos.html'
    model = Product
    paginate_by = 1

    def get_queryset(self):
        query = None
        if ('name' in self.request.GET)  and self.request.GET['name'] =! "":
            query = Q(name=self.request.GET['name'])

        if ('maximo' in self.request.GET) and self.request.GET['maximo'] != "":
            

        


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context