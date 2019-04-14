#import django_tables2 as tables

#from Dashboard.models import Abc


#class PersonTable(tables.Table):
#    class Meta:
#        model = Abc
#        template_name = 'django_tables2/bootstrap.html'

import django_tables2 as tables

data = [
    {'name': 'Bradley'},
    {'name': 'Stevie'},
    {'age':'12'},
    {'age':'12'}
]
lines = ['LINE1','LINE2','LINE3','LINE4']
m3 = ['MAN','MACHINE','MATERIAL']
men = ['man1','man2','man3','man4']
machines = ['machine1','machine2','machine3','machine4']
material = ['material1','material2','material3','material4']
departments = ['CUTTING','SEWING','WASHING','FINISHING']
cutting_sections  =[{'A':'Collar'},{'B':'Front'},{'C':'Lining'},{'D':'Sleeve'}]

class NameTable(tables.Table):
    name = tables.Column()
    age = tables.Column()
    class Meta:
        template_name = 'django_tables2/bootstrap.html'
        row_attrs = {'class':'warning'}
        attrs = {'class':'table table-bordered'}

table = NameTable(data)