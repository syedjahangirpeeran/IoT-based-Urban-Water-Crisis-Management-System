from django.shortcuts import render
from .models import Sensors
from django.http import HttpResponse
def f(request):
    return HttpResponse("But this works")
def Display(request,sensor1=None,sensor2=None,sensor3=None,sensor4=None,sensor5=None,sensor6=None,time=None):
    all_sensors=Sensors()
    all_sensors.sensor1=float(sensor1)
    all_sensors.sensor2=float(sensor2)
    all_sensors.sensor3=float(sensor3)
    all_sensors.sensor4=float(sensor4)
    all_sensors.sensor5=float(sensor5)
    all_sensors.sensor6=float(sensor6)
    all_sensors.time=str(time)
    all_sensors.save()
    p=Sensors.objects.all()[len(Sensors.objects.all())-10::][::-1]
    return render(request,'uwc/map.html',{'all_sensors':p})
def func(request):
    return render(request,'uwc/start.html')
def map(request):
    a=Sensors.objects.all()[len(Sensors.objects.all())-10::][::-1]
    return render(request ,'uwc/map.html',{'all_sensors':a})
def map2(request):
    a=Sensors.objects.all()[len(Sensors.objects.all())-10::][::-1]
    return render(request ,'uwc/map2.html',{'all_sensors':a})
def sensortable(request):
    a=Sensors.objects.all()[len(Sensors.objects.all())-10::][::-1]
    return render(request ,'uwc/sensortable.html',{'all_sensors':a})
def turbidity(request):
    a=Sensors.objects.all()[len(Sensors.objects.all())-1::]
    return render(request ,'uwc/turbiditycheck.html',{'all_sensors':a})
def home(request):
    a=Sensors.objects.all()[len(Sensors.objects.all())-1::]
    return render(request ,'uwc/hack-home.html',{'all_sensors':a})
def flowrate(request):
    a=Sensors.objects.all()[len(Sensors.objects.all())-10::][::-1]
    count=0
    for i in a:
        i.serialId=str(count)
        count+=1
    return render(request ,'uwc/flowrate.html',{'all_sensors':a})
def turgraph(request):
    a=Sensors.objects.all()[len(Sensors.objects.all())-10::][::-1]
    count=0
    for i in a:
        i.serialId=str(count)
        count+=1
    return render(request ,'uwc/turgraph.html',{'all_sensors':a})
def moisture(request):
    a=Sensors.objects.all()[len(Sensors.objects.all())-10::][::-1]
    count=0
    for i in a:
        i.serialId=str(count)
        count+=1
    return render(request ,'uwc/moisture.html',{'all_sensors':a})
def levelrange(request):
    a=Sensors.objects.all()[len(Sensors.objects.all())-10::][::-1]
    count=0
    for i in a:
        i.serialId=str(count)
        count+=1
    return render(request ,'uwc/levelrange.html',{'all_sensors':a})
def passage(request):
    a=Sensors.objects.all()[len(Sensors.objects.all())-10::][::-1]
    count=0
    for i in a:
        i.serialId=str(count)
        count+=1
    return render(request ,'uwc/passage.html',{'all_sensors':a})
