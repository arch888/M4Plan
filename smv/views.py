from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from absenteeism.models import *
from skill_matrix.models import *
from leave_calendar.models import *
from .forms import *
from .models import *
import datetime

def smv(request):
    if(request.method=='POST'):
        form = Smv(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>SMV is submitted</h1>")
        else:
            messages.error(request,"Error")
    else:
        form = Smv()
    return render(request,'smv/smv.html',{'form':form})

def dashsmv(request):
    a=SMV.objects.all()
    return render(request,'smv/dash_smv.html',{'a':a})

def dashpfm(request):
    a=SMV.objects.all()
    sam=[]
    mcs=[]
    for i in a:
        #time=((i.pick_in_sec+i.main_Process_in_sec+i.turn_in_sec+i.dispose_in_sec)*i.s_P_I.s_p_i)/12
        sam.append((((((((i.pick_in_sec+i.main_Process_in_sec+i.turn_in_sec+i.dispose_in_sec)/60)/12)*i.s_P_I.s_p_i)/20)*i.stitch_Length.stitch_length)*int(i.complexity.complx))*(1+int(i.personal_Allowance+i.fatigue_Allowance+i.delay_Allowance))*0.02*0.9)
        print(sam)
    for i in sam:
        mcs.append(560/(480/(i*0.85)))
        print(mcs)
    return render(request,'smv/dash_pfm.html',{'a':a,'sam':sam,'mcs':mcs})

def newdashpfm(request):
    a=PFM.objects.all()
    return render(request,'smv/new_dash_pfm.html',{'a':a})

def ob(request):
    if(request.method=='POST'):
        form=Pfm(request.POST)
        if(form.is_valid()):
            global a
            global d
            global s
            s=request.POST.get('section')
            a=PFM.objects.filter(sec__name=s)
            d=a
            return redirect('/newob')
        else:
            messages.error(request,"Error")
    else:
        form=Pfm()
    return render(request,'smv/ob.html',{'form':form})

def newob(request):
    if(request.method=='POST'):
        global d
        myself=Ob(request.POST,operation=d)
        if(myself.is_valid()):
            global get
            cat=myself.cleaned_data['category']
            sub=myself.cleaned_data['subcategory']
            get=myself.cleaned_data['Add Neccessary Operation']
            print(get)
            print(cat,sub)
            return redirect('/dashob')
        else:
            messages.error(request,"Error")
    else:
        global a
        global s
        form = Ob(operation=a)
    return render(request,'smv/ob.html',{'form':form,'s':s})

def dashob(request):
    global get
    global q
    q=[]
    sam=[]
    for i in get:
        q.append(SMV.objects.get(operation=i))
    for i in q:
        print(i.operation)
        print(i.s_P_I)
        sam.append((((((((i.pick_in_sec + i.main_Process_in_sec + i.turn_in_sec + i.dispose_in_sec) / 60) / 12) * i.s_P_I.s_p_i) / 20) * i.stitch_Length.stitch_length) * int(i.complexity.complx)) * ( 1 + int(i.personal_Allowance + i.fatigue_Allowance + i.delay_Allowance)) * 0.02 * 0.9)
    return render(request,'smv/dashob.html',{'a':q,'sam':sam})
	
def layout(request):
    global s
    global q
    return render(request,'smv/layout.html',{'a':s,'q':q})
	
def dashboard(request):
    global s
    global q
    global get
    ab=[]
    d=datetime.datetime.now().date()
    a=LeaveApplication.objects.all()
    for i in a:
        if(d<=i.end_date):
            ab.append(i.key.user)
    print(ab)
    b=Person.objects.all()
    ab2=[]
    for j in b:
        if(j.date==d):
            if(j.status=='Absent' or j.status=='Leave' or j.status==None):
                ab2.append(User.objects.get(username=j.name))
    print(ab2)
    c=Scale.objects.all()
    #e=Employee.objects.all()
    ss=ab+ab2
    for m in ss:
        for n in c:
            if(m==n.use):
                c=c.exclude(use=m)
    print(c)
    print(get)
    for i in get:
        for j in c:
            if(str(j.operation)==i):
                print(j.use,j.operation,j.level)                
##    m=lambda x:x==y
##    for i in c:
##        y=str(i.operation)
##        print(list(map(m,get)))
    list=zip(c,q)
    return render(request,'smv/dashboard.html',{'a':s,'q':q,'c':c,'get':get,'list':list})


def desc(request):
    return render(request,'smv/desc.html')
