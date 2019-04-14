from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import UpdateView
from stylemaster.models import StyleOrder
import datetime
import pandas as pd

from .forms import *
# Create your views here.
def matter(request):
    if (request.method == 'POST'):
        form = Matter(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request ,'material/final.html')
        else:
            messages.error(request, "Error")

    else:
        form = Matter()
    return render(request, 'material/matter.html', {'form': form})

class updat(UpdateView):
    model = Material
    fields = ('item_no','shell_fabric', 'lining_fabric', 'trim_fabric', 'fusing', 'trims', 'thread', 'button', 'brand_label',
    'fit_label', 'size_label', 'wash_care_label', 'hangtag', 'polybag', 'carton', 'carton_sticket', 'pallet',
    'corner_protection')

    template_name = "material/matter.html"
    success_url = "/final"

def dash(request):
    a=Material.objects.all()
    d = datetime.now().date()
    return render(request, 'material/dash.html',{'a':a,'d':d})
	


def loadplan(request):
    a=StyleOrder.objects.all()
    li=[]
    v=set()
    for i in a:
        v.add(i.c_o_type)
    if(len(v)==1):
        for i in v:
            b=StyleOrder.objects.filter(c_o_type=i)
            s=0
            for i in b:
                s+=int(i.c_o_qty)
            li.append(s)
    else:
        for i in v:
            b=StyleOrder.objects.filter(c_o_type=i)
            s=0
            for j in b:
                s+=int(j.c_o_qty)
            li.append(s)
    print(li)
    value=[]
    app=[]
    k=[]
    actual=[]
    t=[]
    for n in li:
        m=list(range(0,n,1000))
        try:
            for i,j in enumerate(m):
                s=str(m[i]+1)+'-'+str(m[i+1])
                value.append(s)
        except:
            pass

        try:
            for i,j in enumerate(m):
                app.append(random.choice(range(m[i],m[i+1])))
        except:
            pass
        app.insert(0,0)
        try:
            for i,j in enumerate(app):
                k.append(str(app[i]+1)+'-'+str(app[i+1]))
        except:
            pass
        k.append(n-max(app))
        actual.append(k.copy())
        app.clear()
        k.clear()
        value.append(n-max(m))
        t.append(value.copy())
        value.clear()
    print(t[0]+t[1])
    print()
    print(actual[0]+actual[1])
    date=[]
    start_date= '2018/5/30'
    end_date= '2018/6/30'
    date =pd.date_range(start_date, end_date).strftime("%x")
    return render(request,'material/loadplan.html',{'date':date,'j':t[0]+t[1],
                                                       'a':actual[0]+actual[1],'item':list(v)})
    #ss=[]
    #for i in range(0, 100):
        #ss = datetime.date.today() + datetime.timedelta(days=1)
        #date=ss
        #print(date)
##    l=[]
##    for i,j in enumerate(a):
##        x=j.c_o_qty
##        y=x//500
##        for m in range(0,int(y)):
##            l.append(500)
##        d={i:l}
##        print(d[i])
    
