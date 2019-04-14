from django.db import models
from stylemaster.models import Stylemaster
from datetime import datetime
# Create your models here.
ch=[
    ('Y','Y'),
    ('N','N'),
]

class Material(models.Model):
    value=models.DateTimeField(default=datetime.now,blank=True)
    item_no = models.ForeignKey(Stylemaster, on_delete=models.CASCADE, null=True, blank=True)
    shell_fabric=models.CharField(max_length=15,choices=ch)
    lining_fabric=models.CharField(max_length=15,choices=ch)
    trim_fabric=models.CharField(max_length=15,choices=ch)
    fusing=models.CharField(max_length=15,choices=ch)
    trims=models.CharField(max_length=15,choices=ch)
    thread=models.CharField(max_length=15,choices=ch)
    button=models.CharField(max_length=15,choices=ch)
    brand_label=models.CharField(max_length=15,choices=ch)
    fit_label=models.CharField(max_length=15,choices=ch)
    size_label=models.CharField(max_length=15,choices=ch)
    wash_care_label=models.CharField(max_length=15,choices=ch)
    hangtag=models.CharField(max_length=15,choices=ch)
    polybag=models.CharField(max_length=15,choices=ch)
    carton=models.CharField(max_length=15,choices=ch)
    carton_sticket=models.CharField(max_length=15,choices=ch)
    pallet=models.CharField(max_length=15,choices=ch)
    corner_protection=models.CharField(max_length=15,choices=ch)

    def __str__(self):
        return str(self.item_no)