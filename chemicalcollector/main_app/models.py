from django.db import models
from django.urls import reverse

USEDFOR = (
    ('Ex', 'Experiment'),
    ('Co', 'Cooking'),
    ('Cl', 'Cleaning')
)

class Usecase(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.TextField(max_length=300)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('usecases_detail', kwargs={'pk': self.id})

# Create your models here.
class Chemical(models.Model):
        chemicalName = models.CharField(max_length=100)
        commonName = models.CharField(max_length=100)
        formula= models.CharField(max_length=100)
        molarMass = models.FloatField()
        acidity = models.CharField(max_length=100)
        polarity = models.CharField(max_length=100)
        solubility = models.CharField(max_length=100)
        usecases = models.ManyToManyField(Usecase)

        def __str__(self):
            return self.chemicalName

        def get_absolute_url(self):
            return reverse('detail', kwargs={'chemical_id': self.id})

class Utilization(models.Model):
    date = models.DateField('used date')
    usedFor = models.CharField(
        max_length=2,
        choices=USEDFOR,
        default=USEDFOR[0][0]
    )

    chemical = models.ForeignKey(Chemical, on_delete=models.CASCADE)

    def __str__(self):
        return f"Used for {self.get_usedFor_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
