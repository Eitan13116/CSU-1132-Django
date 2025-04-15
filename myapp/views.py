from datetime import datetime
import random
from django.shortcuts import render
from myapp.models import student

# Create your views here.
from django.http import HttpResponse
def sayhello(request):
    return HttpResponse("Hello WuZhongMing!")

def hello2(request, username):
    return HttpResponse("Hello " + username)

def hello3(request, username):
    now = datetime.now()
    return render(request, "hello3.html", {"now": now, "username": username})

def hello4(request, username):
    now = datetime.now()
    return render(request, "hello4.html", {"now": now, "username": username})

def dice(request):
    dicer = random.randint(1, 6)
    return render(request, "dice.html", locals())

def dice2(request):
    dicer1 = random.randint(1, 6)
    dicer2 = random.randint(1, 6)
    dicer3 = random.randint(1, 6)
    return render(request, "dice2.html", locals())

timeDict = {}
def dice3(request):
    global times
    times = times + 1
    local_times = times
    name = "David"
    dicer = random.randint(1, 6)
    return render(request, "dice3.html", {"local_times": local_times, "name": name, "dicer": dicer})

def show(request):
    person1 = {"name": "Amy", "phone": "049-1234567", "age": 20}
    person2 = {"name": "Jack", "phone": "02-4455666", "age": 25}
    person3 = {"name": "Nacy", "phone": "04-9876543", "age": 17}
    persons = [person1, person2, person3]
    return render(request, "show.html", {"persons": persons})

def filter(request):
    value=4
    list1=[1,2,3]
    pw="芝麻開門"
    
    html="<h1>Hello</h1>"
    value2=False
    return render(request,"filter.html",locals())

def listone(request): 
    try: 
        unit = student.objects.get(cName="吳忠明") #讀取一筆資料
    except:
          errormessage = " (讀取錯誤!)"
    return render(request, "listone.html", locals())

def listall(request):  
    students = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "listall.html", locals())
    
def index(request):  
    students = student.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    return render(request, "index.html", locals())		
