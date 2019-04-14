from django.shortcuts import render
from itertools import zip_longest
from django_tables2 import RequestConfig
from django.http import HttpResponse
from Dashboard.models import Abc
from Dashboard.tables import table, lines, m3,men,machines,material,departments,cutting_sections

# Create your views here.

def index(request):
    return HttpResponse("<H2>Dashboard!!</H2>")

def people(request) :
    return render(request, 'people.html',{
        'table': table
    })
def dashboard_preview(request):
    return  render(request,'dashboard.html', {
        'lines' : lines , 'm3': m3,'men':men,'machines':machines,'material':material,'departments':departments,
        'cutting_sections':cutting_sections
    })