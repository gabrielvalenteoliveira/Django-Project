from django.shortcuts import render
from django.http import HttpResponse
from .models import User,Register
from .forms import RegisterForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
   registered = False
   register_form = RegisterForm()
   print('N')
   if request.method == 'POST':
      print('p')
      register_form = RegisterForm(request.POST)
      if register_form.is_valid():
         user = register_form.save(commit=False)
         user.set_password(user.password)
         user.save()
         registered = True
      else:
         return print(register_form.errors())
   else:
      register_form = RegisterForm()

   context = {'form': register_form, 'registered': registered}
   return render(request, 'register.html', context)