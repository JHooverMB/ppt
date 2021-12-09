from django.urls import path
from core.ppt.views.pais.views import *
from core.ppt.views.elector.views import *
from core.ppt.views.dashboard.views import *
#from core.ppt.views import myfirstview, mysecondview

app_name = 'ppt'

urlpatterns = [
    path('pais/list/', PaisListView.as_view(), name='pais_list'),
    path('pais/add/', PaisCreateView.as_view(), name='pais_create'),
    path('pais/update/<int:pk>/', PaisUpdateView.as_view(), name='pais_update'),
    path('pais/delete/<int:pk>/', PaisDeleteView.as_view(), name='pais_delete'),
    # product
    path('elector/list/', ElectorListView.as_view(), name='elector_list'),
    path('elector/add/', ElectorCreateView.as_view(), name='elector_create'),
    path('elector/update/<int:pk>/', ElectorUpdateView.as_view(), name='elector_update'),
    path('elector/delete/<int:pk>/', ElectorDeleteView.as_view(), name='elector_delete'),
    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
