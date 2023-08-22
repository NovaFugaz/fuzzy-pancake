"""
def stats

def spells

"""
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Note
from .models import UserProfile
from .forms import RegistrationForm
from .forms import CharacterForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def notas(request):
    if request.method == 'POST':
        
        if not request.user.is_authenticated:
            messages.warning(request, 'Necesitas iniciar sesión para guardar notas.')
            return redirect('/notas')
        
        title = request.POST['title']
        content = request.POST['content']
        user_profile = request.user.userprofile
        
        note = Note(title=title, content=content, user_profile=user_profile)
        note.save()
        
        return redirect('/notas')

    if request.user.is_authenticated:
        user_profile = request.user.userprofile
        notes = Note.objects.filter(user_profile=user_profile)
    else:
        notes = []

    return render(request, 'notas.html', {'notes': notes})

def index(request):
    return render (request, 'index.html', {'user': request.user})

def error(request):
    return render (request, 'error.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            name = form.cleaned_data['name']
            UserProfile.objects.create(user=user, name=name)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'base/register.html', {'form': form})

@login_required
def creator(request):
    user_profile = request.user.userprofile
    form = CharacterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            character = form.save(commit=False)
            character.user_profile = user_profile  # Set the user_profile
            character.save()
            return redirect('charlist')
    context = {'form': form}
    return render(request, 'creator.html', context)

def characterList(request):
    return render(request, 'characters/charlist.html')

def error(request):
    return HttpResponse("Warning!")

def success(request):
    return HttpResponse("YES!")