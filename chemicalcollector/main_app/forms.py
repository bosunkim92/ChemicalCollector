from django.forms import ModelForm
from .models import Utilization

class UtilizationForm(ModelForm):
    class Meta:
        model = Utilization
        fields = ['date', 'usedFor']