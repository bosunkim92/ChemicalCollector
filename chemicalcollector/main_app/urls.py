from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('chemicals/', views.chemicals_index, name='index'),
    path('chemicals/<int:chemical_id>/', views.chemicals_detail, name="detail"),
    path('chemicals/create/', views.ChemicalCreate.as_view(), name="chemicals_create"),
    path('chemicals/<int:pk>/update/', views.ChemicalUpdate.as_view(), name="chemicals_update"),
    path('chemcials/<int:pk>/delete/', views.ChemicalDelete.as_view(), name="chemicals_delete"),
    path('chemicals/<int:chemical_id>/add_utilization/', views.add_utilization, name="add_utilization"),
    path('chemicals/<int:chemical_id>/assoc_usecase/<int:usecase_id>/', views.assoc_usecase, name="assoc_usecase"),
    path('chemicals/<int:chemical_id>/unassoc_usecase/<int:usecase_id>/', views.unassoc_usecase, name="unassoc_usecase"),
    path('usecases/', views.UsecaseList.as_view(), name='usecases_index'),
    path('usecases/<int:pk>/', views.UsecaseDetail.as_view(), name='usecases_detail'),
    path('usecases/create/', views.UsecaseCreate.as_view(), name='usecases_create'),
    path('usecases/<int:pk>/update/', views.UsecaseUpdate.as_view(), name='usecases_update'),
    path('usecases/<int:pk>/delete/', views.UsecaseDelete.as_view(), name='usecases_delete'),
]