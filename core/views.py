from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import User


def home(request):
    if 'username' in request.session:
        usuario = request.session['username']
    else:
        usuario = request.user.username
    return render (request, 'core/home.html', { 'usuario': usuario })

'''
def home(request):
    usuario = 'USUÁRIO' #request.user.username
    return render (request, 'core/home.html', { 'usuario': usuario })
'''
