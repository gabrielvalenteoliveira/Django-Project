from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import User,Register
from .forms import RegisterForm, EditUserForm, LoginForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register(request):
   registered = False
   register_form = RegisterForm()
   if request.method == 'POST':
      register_form = RegisterForm(request.POST)
      if register_form.is_valid():
         user = register_form.save(commit=False)
         user.set_password(user.password)
         user.save()
         registered = True
         messages.success(request, ('Usuario criado com sucesso'))
         return redirect('home')
      else:
         messages.success(request, (f'Erro: com o campo: {register_form.errors}'))
         return redirect('register')
   else:
      context = {'form': register_form, 'registered': registered}
      return render(request, 'authenticate/register.html', context)

@csrf_exempt
def login_auth(request):
   form = LoginForm()
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request, user)
         messages.success(request, ('Usuario logado com sucesso'))
         return redirect('home')
      else:
         messages.success(request,('Erro: senha ou usuario inválidos'))
         return redirect('login')

   else:
      context = {'form':form}
      return render(request, 'authenticate/login.html', context)

def logout_user(request):
   logout(request)
   messages.success(request, ('Voce saiu do login'))
   return redirect('home')

def show_users(request):
   usersList = User.objects.all()
   context  = {'users':usersList}
   return render(request, 'authenticate/showUsers.html', context)

def delete_user(id):
   user_deleted = User.objects.get(id=id)
   user_deleted.delete()
   return redirect('showUsers')


def edit_user(request, id):
   if request.user.is_authenticated:
      current_user = User.objects.get(id=id)
      form = EditUserForm(instance=current_user)
      if request.method == 'POST':
         form = EditUserForm(data=request.POST, instance=current_user)
         if form.is_valid():
            form.save()
            messages.success(request, ('Usuario editado com sucesso'))
            return redirect('showUsers')
         else:
            messages.success(request, ('Erro ao editar usuario: ', form.errors))
            return redirect('showUsers')
      else:
         form = EditUserForm(instance=current_user)

      context = {'form': form}
      return render(request, 'authenticate/edit-user.html', context)
   
   else:
      messages.success(request, ('Você precisa fazer login para editar usuário'))
      return redirect('home')