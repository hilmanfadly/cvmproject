from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import JA
from django.urls import reverse
# Create your views here.

def index(request):
   # return render (request, 'JobApply/JA.html')
   if request.method == 'POST':
      data1 = request.POST['firstName'],
      data2 = request.POST['lastName'],
      data3 = request.POST['phone'],
      data4 = request.POST['email'],
      data5 = request.POST['address'],
      data6 = request.POST['skills'],
      data7 = request.POST['langguages'],
      data8 = request.POST['AboutMe'],
      data9 = request.POST['education'],
      data10 = request.POST['exp'],

     
      newjobapply = JA(first_name= data1, last_name=data2,phone_number=data3,email=data4,current_location=data5,skills=data6,langguage=data7,about_me=data8,education=data9,experience=data10)
      newjobapply.save()
      
   return render(request, 'JobApply/JA.html')
  # template = loader.get_template('JA.html')
   #return HttpResponse(template.render())


#def create(request):
  # template = loader.get_template('JA.html')
   #return render(request,'base.html')
 #  return HttpResponse(template.ender({},request))


#def createdata(request):
  # template = loader.get_template('JA.html')
  #data1 = request.POST['firstName'],
   #data2 = request.POST['lastName'],
   #data3 = request.POST['phone'],
   #data4 = request.POST['email'],
   #data5 = request.POST['address'],
   #data6 = request.POST['skills'],
   #data7 = request.POST['langguages'],
   #data8 = request.POST['AboutMe'],
   #data9 = request.POST['education'],
   #data10 = request.POST['exp'],
   #newjobapply = JA(firstname= data1, lastname=data2,phone=data3,email=data4,address=data5,skills=data6,langguanges=data7,AboutMe=data8,education=data9,exp=data10)
   #newjobapply.save()
   #return HttpResponseRedirect(reverse(index))