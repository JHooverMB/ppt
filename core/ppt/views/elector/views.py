from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.ppt.forms import ElectorForm
from core.ppt.models import Elector


class ElectorListView(ListView):
    model = Elector
    template_name = 'elector/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Electores'
        context['create_url'] = reverse_lazy('ppt:elector_create')
        context['list_url'] = reverse_lazy('ppt:elector_list')
        context['entity'] = 'Electores'
        return context


class ElectorCreateView(CreateView):
    model = Elector
    form_class = ElectorForm
    template_name = 'elector/create.html'
    success_url = reverse_lazy('ppt:elector_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
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
        context['title'] = 'Creación de un Elector'
        context['entity'] = 'Electores'
        context['list_url'] = reverse_lazy('ppt:elector_list')
        context['action'] = 'add'
        return context


class ElectorUpdateView(UpdateView):
    model = Elector
    form_class = ElectorForm
    template_name = 'elector/create.html'
    success_url = reverse_lazy('ppt:elector_list')

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
        context['title'] = 'Edición de un Elector'
        context['entity'] = 'Electores'
        context['list_url'] = reverse_lazy('ppt:elector_list')
        context['action'] = 'edit'
        return context


class ElectorDeleteView(DeleteView):
    model = Elector
    template_name = 'elector/delete.html'
    success_url = reverse_lazy('ppt:elector_list')

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
        context['title'] = 'Eliminación de un Elector'
        context['entity'] = 'Electores'
        context['list_url'] = reverse_lazy('ppt:elector_list')
        return context
