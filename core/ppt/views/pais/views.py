from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.ppt.models import Pais
from core.ppt.forms import PaisForm

class PaisListView(ListView):
    model = Pais
    template_name = 'pais/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Pais.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Paises'
        context['create_url'] = reverse_lazy('ppt:pais_create')
        context['list_url'] = reverse_lazy('ppt:pais_list')
        context['entity'] = 'Paises'
        return context

class PaisCreateView(CreateView):
    model = Pais
    form_class = PaisForm
    template_name = 'pais/create.html'
    success_url = reverse_lazy('ppt:pais_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Pais'
        context['entity'] = 'Paises'
        context['list_url'] = reverse_lazy('ppt:pais_list')
        context['action'] = 'add'
        return context


class PaisUpdateView(UpdateView):
    model = Pais
    form_class = PaisForm
    template_name = 'pais/create.html'
    success_url = reverse_lazy('ppt:pais_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición un Pais'
        context['entity'] = 'Paises'
        context['list_url'] = reverse_lazy('ppt:pais_list')
        context['action'] = 'edit'
        return context


class PaisDeleteView(DeleteView):
    model = Pais
    template_name = 'pais/delete.html'
    success_url = reverse_lazy('ppt:pais_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Pais'
        context['entity'] = 'Paises'
        context['list_url'] = reverse_lazy('ppt:pais_list')
        return context

