from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Character

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)
    name = forms.CharField(label="Nombre")

    error_messages = {
        'password_mismatch': "Las contraseñas no coinciden.",
        'password_too_short': "La contraseña es demasiado corta. Debe contener al menos 8 caracteres.",
        'password_common': "La contraseña es demasiado común.",
        'password_entirely_numeric': "La contraseña no puede ser completamente numérica.",
    }

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = "Requerido. 150 caracteres o menos. Solo letras, dígitos y @/./+/-/_."
        self.fields['password1'].help_text = "Tu contraseña no puede ser demasiado similar a tu otra información personal. Debe contener al menos 8 caracteres. No puede ser una contraseña común. No puede ser completamente numérica."


class CharacterForm(forms.ModelForm):
    name = forms.CharField(label='Nombre')
    level = forms.IntegerField(label='Nivel')
    exp = forms.IntegerField(label='Experiencia')
    race = forms.CharField(label='Raza')
    alignment = forms.CharField(label='Alineación')
    class1 = forms.CharField(label='Clase')
    strength = forms.IntegerField(label='Fuerza')
    dexterity = forms.IntegerField(label='Destreza')
    constitution = forms.IntegerField(label='Constitución')
    intelligence = forms.IntegerField(label='Inteligencia')
    wisdom = forms.IntegerField(label='Sabiduría')
    charisma = forms.IntegerField(label='Carisma')
    prof_bonus = forms.IntegerField(label='Bono de competencia')
    armor_class = forms.IntegerField(label='Clase de armadura')
    move_speed = forms.IntegerField(label='Velocidad de movimiento')
    
    class Meta:
        model = Character
        fields = [
            'name',
            'level',
            'exp',
            'race',
            'alignment',
            'class1',
            'strength',
            'dexterity',
            'constitution',
            'intelligence',
            'wisdom',
            'charisma',
            'prof_bonus',
            'armor_class',
            'move_speed',
        ]