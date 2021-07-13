from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Chemical, Usecase
from .forms import UtilizationForm

# Create your views here.

class ChemicalCreate(CreateView):
    model = Chemical
    fields = ['chemicalName', 'commonName', 'formula', 'molarMass', 'acidity', 'polarity', 'solubility']

class ChemicalUpdate(UpdateView):
    model = Chemical
    fields = ['formula', 'molarMass', 'acidity', 'polarity', 'solubility']

class ChemicalDelete(DeleteView):
    model = Chemical
    success_url = '/chemicals/'

class UsecaseList(ListView):
    model = Usecase

class UsecaseDetail(DetailView):
    model = Usecase

class UsecaseCreate(CreateView):
    model = Usecase
    fields = '__all__'

class UsecaseUpdate(UpdateView):
    model = Usecase
    fields = '__all__'

class UsecaseDelete(DeleteView):
    model = Usecase
    success_url = '/usecases/'

def home(request):
    return redirect('about')

def about(request):
    return render(request, 'about.html')

def chemicals_index(request):
    chemicals = Chemical.objects.all()
    return render(request, 'chemicals/index.html', { 'chemicals': chemicals })

def chemicals_detail(request, chemical_id):
    chemical = Chemical.objects.get(id=chemical_id)

    usecases_chemical_doesnt_have = Usecase.objects.exclude(id__in = chemical.usecases.all().values_list('id'))

    utilization_form = UtilizationForm()

    return render(request, 'chemicals/detail.html', {
        'chemical': chemical,
        'utilization_form': utilization_form,
        'usecases': usecases_chemical_doesnt_have
    })

def add_utilization(request, chemical_id):
    form = UtilizationForm(request.POST)
    if form.is_valid():
        new_utilization = form.save(commit=False)
        new_utilization.chemical_id = chemical_id
        new_utilization.save()
    return redirect('detail', chemical_id=chemical_id)

def assoc_usecase(request, chemical_id, usecase_id):
    Chemical.objects.get(id=chemical_id).usecases.add(usecase_id)
    return redirect('detail', chemical_id=chemical_id)

def unassoc_usecase(request, chemical_id, usecase_id):
    Chemical.objects.get(id=chemical_id).usecases.remove(usecase_id)
    return redirect('detail', chemical_id=chemical_id)