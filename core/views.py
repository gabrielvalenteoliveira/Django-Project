from django.http import HttpResponse
from django.shortcuts import render


dictionary = {
   'Name': 'Gabriel',
   'Age': 18,
}

def home(request):
   context = {'var': dictionary}
   return render(request, 'home.html', context)