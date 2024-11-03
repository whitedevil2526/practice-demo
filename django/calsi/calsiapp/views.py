from django.shortcuts import render,HttpResponse
from . import views
# Create your views here.
def home(request):
    name = 'samarth sabale'
    print(name)
    return HttpResponse(name)
def contact(request):
    contact = 9988776655
    print(contact)
    return HttpResponse(contact)
def add(request):
    num1 = 10
    num2 = 20
    num3 = num1 + num2
    print(num3)
    return HttpResponse(num3)
def welcome(request):
    if request.method == 'POST':
        exp = request.POST['exp_name']
        answer = eval(exp)
        print(f"the expression is ={exp} \n the ans is ={answer}")
        return render(request,'index.html',{'exp':exp,'answer':answer})
    