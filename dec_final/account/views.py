from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import RegisterForm

# Create your views here.
def sign_out(request):
    logout(request)
    return redirect('/')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})



